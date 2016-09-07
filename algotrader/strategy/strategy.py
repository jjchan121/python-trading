from algotrader import Startable, HasId
from algotrader.config.trading import BacktestingConfig
from algotrader.event.event_bus import EventBus
from algotrader.event.event_handler import MarketDataEventHandler, ExecutionEventHandler
from algotrader.event.order import OrdAction, OrdType, TIF, NewOrderRequest, OrderReplaceRequest, \
    OrderCancelRequest
from algotrader.provider.persistence import Persistable
from algotrader.provider.subscription import SubscriptionKey, HistDataSubscriptionKey
from algotrader.trading.position import PositionHolder
import abc

class Strategy(PositionHolder, ExecutionEventHandler, MarketDataEventHandler, Persistable, Startable, HasId):

    __slots__ = (
        'stg_id',
        'trading_config',
        'next_ord_id',
        'ord_req',
        'order',
    )

    def __init__(self, stg_id=None, app_context=None, trading_config=None):
        super(Strategy, self).__init__()
        self.stg_id = stg_id
        self.app_context = app_context
        self.trading_config = trading_config
        self.ord_req = {}
        self.order = {}

    def __get_next_ord_id(self):
        return self.app_context.seq_mgr.get_next_sequence(self.id())

    def _start(self):
        self.ref_data_mgr = self.app_context.ref_data_mgr
        self.portfolio = self.app_context.portf_mgr.get_portfolio(self.trading_config.portfolio_id)
        self.feed = self.app_context.feed_mgr.get(self.trading_config.feed_id) if self.trading_config else None
        self.broker = self.app_context.broker_mgr.get(self.trading_config.broker_id)

        self.instruments = self.ref_data_mgr.get_insts(self.trading_config.instrument_ids)
        self.clock = self.app_context.get_clock(self.trading_config.clock_type)
        self.event_subscription = EventBus.data_subject.subscribe(self.on_next)
        self._subscribe_market_data(self.instruments)

        self.portfolio.start()
        self.broker.start()
        self.feed.start()

    def _stop(self):
        if self.event_subscription:
            self.event_subscription.dispose()

    def _subscribe_market_data(self, instruments):
        for instrument in instruments:
            for subscription_type in self.trading_config.subscription_types:
                if isinstance(self.trading_config, BacktestingConfig):

                    sub_key = HistDataSubscriptionKey(inst_id=instrument.inst_id,
                                                      provider_id=self.trading_config.feed_id,
                                                      subscription_type=subscription_type,
                                                      from_date=self.trading_config.from_date,
                                                      to_date=self.trading_config.to_date)

                else:
                    sub_key = SubscriptionKey(inst_id=instrument.inst_id,
                                              provider_id=self.trading_config.feed_id,
                                              subscription_type=subscription_type)
                self.feed.subscribe_mktdata(sub_key)

    def id(self):
        return self.stg_id

    def on_bar(self, bar):
        super(Strategy, self).on_bar(bar)

    def on_quote(self, quote):
        super(Strategy, self).on_quote(quote)

    def on_trade(self, trade):
        super(Strategy, self).on_trade(trade)

    def on_market_depth(self, market_depth):
        super(Strategy, self).on_market_depth(market_depth)

    def on_ord_upd(self, ord_upd):
        if ord_upd.cl_id == self.stg_id:
            super(Strategy, self).on_ord_upd(ord_upd)

    def on_exec_report(self, exec_report):
        if exec_report.cl_id == self.stg_id:
            super(Strategy, self).on_exec_report(exec_report)
            ord_req = self.ord_req[exec_report.cl_ord_id]
            direction = 1 if ord_req.action == OrdAction.BUY else -1
            if exec_report.last_qty > 0:
                self.add_position(exec_report.inst_id, exec_report.cl_id, exec_report.cl_ord_id,
                                  direction * exec_report.last_qty)
                self.update_position_price(exec_report.timestamp, exec_report.inst_id, exec_report.last_price)

    def market_order(self, inst_id, action, qty, tif=TIF.DAY, oca_tag=None, params=None):
        return self.new_order(inst_id=inst_id, action=action, type=OrdType.MARKET, qty=qty, limit_price=0.0, tif=tif,
                              oca_tag=oca_tag, params=params)

    def limit_order(self, inst_id, action, qty, price, tif=TIF.DAY, oca_tag=None, params=None):
        return self.new_order(inst_id=inst_id, action=action, type=OrdType.LIMIT, qty=qty, limit_price=price, tif=tif,
                              oca_tag=oca_tag, params=params)

    def stop_order(self):
        # TODO
        pass

    def stop_limit_order(self):
        # TODO
        pass

    def close_position(self, inst_id):
        # TODO
        pass

    def close_all_positions(self):
        # TODO
        pass

    def new_order(self,
                  inst_id=None, action=None, type=None,
                  qty=0, limit_price=0,
                  stop_price=0, tif=TIF.DAY, oca_tag=None, params=None):
        req = NewOrderRequest(timestamp=self.clock.now(),
                              cl_id=self.stg_id,
                              cl_ord_id=self.__get_next_ord_id(),
                              portf_id=self.portfolio.portf_id,
                              broker_id=self.trading_config.broker_id,
                              inst_id=inst_id,
                              action=action,
                              type=type,
                              qty=qty,
                              limit_price=limit_price,
                              stop_price=stop_price,
                              tif=tif,
                              oca_tag=oca_tag,
                              params=params)
        self.ord_req[req.cl_ord_id] = req
        order = self.portfolio.send_order(req)
        self.order[order.cl_ord_id] = order
        self.get_position(order.inst_id).add_order(order)
        return order

    def cancel_order(self, cl_ord_id=None):
        req = OrderCancelRequest(timestamp=self.clock.now(),
                                 cl_id=self.stg_id, cl_ord_id=cl_ord_id)
        order = self.portfolio.cancel_order(req)
        return order

    def replace_order(self, cl_ord_id=None, type=None, qty=None, limit_price=None, stop_price=None, tif=None):
        req = OrderReplaceRequest(timestamp=self.clock.now(),
                                  cl_id=self.stg_id, cl_ord_id=cl_ord_id, type=type, qty=qty, limit_price=limit_price,
                                  stop_price=stop_price, tif=tif)
        order = self.portfolio.replace_order(req)
        return order

    def get_portfolio(self):
        return self.portfolio
