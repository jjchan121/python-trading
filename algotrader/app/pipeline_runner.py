

from datetime import date

from algotrader.app import Application
from algotrader.chart.plotter import StrategyPlotter
from algotrader.config.app import ApplicationConfig, ScreenConfig
from algotrader.config.persistence import PersistenceConfig
from algotrader.event.market_data import BarSize, BarType
from algotrader.provider.broker import Broker
from algotrader.provider.feed import Feed
from algotrader.provider.subscription import BarSubscriptionType
from algotrader.trading.context import ApplicationContext
from algotrader.trading.ref_data import RefDataManager
from algotrader.utils.clock import Clock
from algotrader.provider.broker import Broker
from algotrader.config.feed import CSVFeedConfig, PandasMemoryDataFeedConfig
from algotrader.config.persistence import MongoDBConfig
from algotrader.config.builder import *
from algotrader.strategy.pipeline_holder import PipelineHolder
from algotrader.technical.pipeline import PipeLine
from algotrader.technical.ma import SMA

class PipeLineRunner(Application):
    def __init__(self, pipeline_holder):
        self.app_config = None
        self.pipeline_holder = pipeline_holder

    def init(self):
        self.app_config = self.app_context.app_config
        self.app_context.add_startable(self.pipeline_holder)

    def run(self):
        self.app_context.start()
        self.pipeline_holder.start(self.app_context)


class AlphaFormulaScreen(PipelineHolder):
    def __init__(self, pipe_id=None, pipe_configs=None):
        super(AlphaFormulaScreen, self).__init__(pipe_id=pipe_id, pipe_configs=pipe_configs)

    def _start(self, app_context, **kwargs):
        super(AlphaFormulaScreen, self)._start(app_context)

        if not self.app_context.app_config.instrument_ids:
            self.instruments = self.ref_data_mgr.get_all_insts()
        else :
            self.instruments = self.ref_data_mgr.get_insts(self.app_context.app_config.instrument_ids)
        # self.instruments = self.ref_data_mgr.get_all_insts()

        bars = [self.app_context.inst_data_mgr.get_series(
            "Bar.%s.Time.86400" % i.inst_id) for i in self.instruments]

        for b in bars:
            b.start(app_context)

        # smas = [SMA(bar, 'close', length=5) for bar in bars]
        # for s in smas:
        #     s.start(app_context)

        # sma5 = PipeLine('SMA5', smas, input_keys='close')
        closes = PipeLine('closes', bars, input_keys='close')
        closes.start(app_context)
        #volumes = PipeLine('volumes', bars, input_keys='volume')

        # sma5.start(app_context)
        #closes.start(app_context)
        #volumes.start(app_context)
        self.pipelines = {'closes' : closes}
                          #'volumes' : volumes}

        # super(AlphaFormulaScreen, self).pipelines = {'closes' : closes,
        #                                              'volumes' : volumes}



def main():

    file = "/home/jason/data/etf.pkl"
    import pandas as pd
    import pickle
    df_dict = {}

    with open(file, 'rb') as f:
        df_dict = pickle.load(f)

    # for k,df in df_dict.iteritems():
    #     df['Symbol'] = k
    #     df['BarSize'] = int(BarSize.D1)

    screen = AlphaFormulaScreen(pipe_id='alpha_formula1', pipe_configs=None)

    screen_config = ScreenConfig(id="test_screen", pipe_id="pipe1",
                                 instrument_ids=[3348, 8984, 5998],
                                 subscription_types=[
                                     BarSubscriptionType(bar_type=BarType.Time, bar_size=BarSize.D1)
                                 ],
                                 feed_id=Feed.PandasMemory,
                                 #feed_id=Feed.CSV,
                                 from_date=date(2011,12,1),
                                 to_date=date.today(),
                                 pipe_configs=None,
                                 ref_data_mgr_type=RefDataManager.DB,
                                 clock_type=Clock.Simulation,
                                 persistence_config= backtest_in_memory_config(),
                                 provider_configs=[MongoDBConfig(), PandasMemoryDataFeedConfig(df_dict)])
                                 #provider_configs=[MongoDBConfig(), CSVFeedConfig(path='../../data/tradedata')])

    app_context = ApplicationContext(app_config=screen_config)

    runner = PipeLineRunner(screen)
    runner.start(app_context)
    print runner.pipeline_holder.pipelines["closes"].get_panel()


if __name__ == "__main__":
    main()
