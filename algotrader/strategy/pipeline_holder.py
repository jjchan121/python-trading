from algotrader import Startable, HasId
from algotrader.event.event_bus import EventBus
from algotrader.event.event_handler import MarketDataEventHandler
from algotrader.provider.persistence import Persistable
from algotrader.provider.subscription import SubscriptionKey, HistDataSubscriptionKey, MarketDataSubscriber
from algotrader.trading.position import PositionHolder
from algotrader.config.app import BacktestingConfig


class PipelineHolder(PositionHolder, MarketDataEventHandler, Persistable, Startable, HasId, MarketDataSubscriber):
    """
    A class used to replay historical data and hold pipelines for analysis before running a backtesting
    """
    __slots__ = (
        'pipe_id',
        'pipe_configs',
        'app_context',
        'app_config',
        'ref_data_mgr',
        'feed',
        'clock',
        'event_subscription',
        'instruments',
        'pipelines'
    )

    __transient__ = (
        'app_context',
        'app_config',
        'ref_data_mgr',
        'feed',
        'clock',
        'event_subscription',
        'instruments'
    )

    def __init__(self, pipe_id=None, pipe_configs=None):
        super(PipelineHolder, self).__init__()
        self.pipe_id = pipe_id
        self.pipe_configs = pipe_configs
        self.pipelines = {}

    def __get_next_ord_id(self):
        return str(self.app_context.seq_mgr.get_next_sequence(self.id()))

    def get_pipe_config_value(self, key, default_value=None):
        if self.pipe_configs:
            return self.pipe_configs.get(key, default_value)
        return default_value

    def get_pipelines(self):
        return self.pipelines

    def _start(self, app_context, **kwargs):
        self.app_context.stg_mgr.add(self)
        self.app_config = self.app_context.app_config
        self.pipe_configs = self.app_config.pipe_configs if self.app_config.pipe_configs  else self.pipe_configs # if the pass-in app context.app_config contains strategy config, use that one, otherwises use the persisted one.
        self.ref_data_mgr = self.app_context.ref_data_mgr
        self.feed = self.app_context.provider_mgr.get(self.app_config.feed_id) if self.app_config else None

        if not self.app_context.app_config.instrument_ids:
            self.instruments = self.ref_data_mgr.get_all_insts()
        else :
            self.instruments = self.ref_data_mgr.get_insts(self.app_context.app_config.instrument_ids)
        self.clock = self.app_context.clock
        self.event_subscription = EventBus.data_subject.subscribe(self.on_next)

        if self.feed:
            self.feed.start(app_context)

        if isinstance(self.app_config, BacktestingConfig):
            self.subscript_market_data(self.feed, self.instruments, self.app_config.subscription_types,
                                       self.app_config.from_date, self.app_config.to_date)
        else:
            self.subscript_market_data(self.feed, self.instruments, self.app_config.subscription_types)

    def _stop(self):
        if self.event_subscription:
            self.event_subscription.dispose()

    def _subscribe_market_data(self, feed, instruments, subscription_types):
        for instrument in instruments:
            for subscription_type in subscription_types:
                if isinstance(self.app_config, BacktestingConfig):

                    sub_key = HistDataSubscriptionKey(inst_id=instrument.inst_id,
                                                      provider_id=self.app_config.feed_id,
                                                      subscription_type=subscription_type,
                                                      from_date=self.app_config.from_date,
                                                      to_date=self.app_config.to_date)

                else:
                    sub_key = SubscriptionKey(inst_id=instrument.inst_id,
                                              provider_id=self.app_config.feed_id,
                                              subscription_type=subscription_type)
                self.feed.subscribe_mktdata(sub_key)

    def id(self):
        return self.pipe_id

    def on_bar(self, bar):
        super(PipelineHolder, self).on_bar(bar)


