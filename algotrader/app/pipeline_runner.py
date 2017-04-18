

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
from algotrader.config.feed import CSVFeedConfig
from algotrader.config.persistence import MongoDBConfig
from algotrader.config.builder import *
from algotrader.strategy.pipeline_holder import PipelineHolder
from algotrader.technical.pipeline import PipeLine

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

        # if not self.app_context.app_config.instrument_ids:
        #     self.instruments = self.ref_data_mgr.get_all_insts()
        # else :
        #     self.instruments = self.ref_data_mgr.get_insts(self.app_context.app_config.instrument_ids)
        self.instruments = self.ref_data_mgr.get_all_insts()

        bars = [self.app_context.inst_data_mgr.get_series(
            "Bar.%s.Time.300" % i.inst_id) for i in self.instruments]

        closes = PipeLine('closes', bars, input_keys='close')
        volumes = PipeLine('volumes', bars, input_keys='volume')

        self.pipelines = {'closes' : closes,
                          'volumes' : volumes}

        # super(AlphaFormulaScreen, self).pipelines = {'closes' : closes,
        #                                              'volumes' : volumes}



def main():

    file = "/Users/jchan/workspace/data/etf.pkl"
    import pandas as pd
    import pickle
    df_dict = {}

    with open(file, 'rb') as f:
        df_dict = pickle.load(f)

    screen = AlphaFormulaScreen(pipe_id='alpha_formula1', pipe_configs=None)

    screen_config = ScreenConfig(id="test_screen", pipe_id="pipe1", instrument_ids=None,
                                 subscription_types=[
                                     BarSubscriptionType(bar_type=BarType.Time, bar_size=BarSize.D1)
                                 ],
                                 feed_id=Feed.PandasMemory,
                                 from_date=date(2010,1,1),
                                 to_date=date.today(),
                                 pipe_configs=None,
                                 ref_data_mgr_type=RefDataManager.DB,
                                 clock_type=Clock.Simulation,
                                 provider_configs=PandasMemoryDataFeedConfig(df_dict))

    app_context = ApplicationContext(app_config=screen_config)

    runner = PipeLineRunner(screen)
    runner.start(app_context)
    print runner.pipeline_holder


if __name__ == "__main__":
    main()
