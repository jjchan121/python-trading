'''
Created on 4/16/16
@author = 'jason'
'''

from algotrader.app import Application
from algotrader.config.app import ApplicationConfig, LiveTradingConfig
from algotrader.config.broker import IBConfig
from algotrader.config.persistence import PersistenceConfig
from algotrader.event.market_data import BarSize, BarType
from algotrader.provider.broker import Broker
from algotrader.provider.subscription import BarSubscriptionType
from algotrader.trading.context import ApplicationContext
from algotrader.trading.ref_data import RefDataManager
from algotrader.utils import logger
from algotrader.utils.clock import Clock


class ATSRunner(Application):
    def __init__(self):
        pass

    def init(self):
        logger.info("starting ATS")
        self.app_config = self.app_context.app_config
        self.portfolio = self.app_context.portf_mgr.get_or_new_portfolio(self.app_config.portfolio_id, 1000000)


        self.initial_result = self.portfolio.get_result()

        self.app_context.add_startable(self.portfolio)

        self.strategy = self.app_context.stg_mgr.get_or_new_stg(self.app_config)
        self.app_context.add_startable(self.strategy)

    def run(self):
        self.app_context.start()
        self.strategy.start(self.app_context)

        logger.info("ATS started, presss Ctrl-C to stop")

from algotrader.strategy.simple_market_making import SimpleMarketMaking

def main():
    broker_config = IBConfig(client_id=2)
    live_trading_config = LiveTradingConfig(id=None,
                                            stg_id="nativeMM",
                                            stg_cls='algotrader.strategy.simple_market_making.SimpleMarketMaking',
                                            portfolio_id='test',
                                            instrument_ids=['SPY@ARCA'],
                                            subscription_types=[
                                                BarSubscriptionType(bar_type=BarType.Time, bar_size=BarSize.M1)],
                                            feed_id=Broker.IB,
                                            broker_id=Broker.IB,
                                            ref_data_mgr_type = RefDataManager.DB,
                                           # clock_type = Clock.RealTime,
                                            persistence_config =PersistenceConfig())#,
                                            # configs = [broker_config])

    app_context = ApplicationContext(app_config=live_trading_config)
    ATSRunner().start(app_context)


if __name__ == "__main__":
    main()
