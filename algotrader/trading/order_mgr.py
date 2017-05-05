from typing import List

from algotrader import Manager
from algotrader.event.event_handler import MarketDataEventHandler, OrderEventHandler, ExecutionEventHandler
from algotrader.model.market_data_pb2 import *
from algotrader.model.model_factory import ModelFactory
from algotrader.model.trade_data_pb2 import *
from algotrader.provider.persistence import PersistenceMode
from algotrader.trading.order import Order
from algotrader.utils.logging import logger


class OrderManager(Manager, OrderEventHandler, ExecutionEventHandler, MarketDataEventHandler):
    __slots__ = (
        'app_context',
        'order_dict',
        'ord_reqs_dict',
    )

    def __init__(self):
        super(OrderManager, self).__init__()
        self.order_dict = {}
        self.ord_reqs_dict = {}

    def _start(self, app_context):
        self.store = app_context.get_data_store()
        self.persist_mode = app_context.app_config.get_app_config("persistenceMode")
        self.load_all()
        self.subscriptions = []
        self.subscriptions.append(app_context.event_bus.data_subject.subscribe(self.on_market_data_event))
        self.subscriptions.append(app_context.event_bus.order_subject.subscribe(self.on_order_event))
        self.subscriptions.append(app_context.event_bus.execution_subject.subscribe(self.on_execution_event))

    def _stop(self):
        if self.subscriptions:
            for subscription in self.subscriptions:
                try:
                    subscription.dispose()
                except:
                    pass
        self.save_all()
        self.reset()

    def all_orders(self):
        return [order for order in self.order_dict.values()]

    def load_all(self):
        if hasattr(self, "store") and self.store:
            self.store.start(self.app_context)
            orders = self.store.load_all('orders')
            for order in orders:
                self.order_dict[order.id()] = order

            new_order_reqs = self.store.load_all('new_order_reqs')
            for new_order_req in new_order_reqs:
                self.ord_reqs_dict[self._cl_ord_id(new_order_req)] = new_order_req

    def save_all(self):
        if hasattr(self, "store") and self.store and self.persist_mode != PersistenceMode.Disable:
            for order in self.all_orders():
                self.store.save_order(order)

            for new_order_req in self.ord_reqs_dict.values():
                self.store.save_new_order_req(new_order_req)

    def reset(self):
        self.order_dict = {}
        self.ord_reqs_dict = {}

    def next_ord_id(self):
        return self.app_context.seq_mgr.get_next_sequence(self.id())

    def on_bar(self, bar: Bar) -> None:
        super(OrderManager, self).on_bar(bar)

    def on_quote(self, quote: Quote) -> None:
        super(OrderManager, self).on_quote(quote)

    def on_trade(self, trade: Trade) -> None:
        super(OrderManager, self).on_trade(trade)

    def on_market_depth(self, market_depth: MarketDepth) -> None:
        super(OrderManager, self).on_market_depth(market_depth)

    def on_ord_upd(self, ord_upd: OrderStatusUpdate) -> None:
        super(OrderManager, self).on_ord_upd(ord_upd)

        # persist
        if hasattr(self, "store") and self.store and self.persist_mode != PersistenceMode.RealTime:
            self.store.save_ord_status_upd(ord_upd)

        # update order
        order = self.order_dict["%s.%s" % (ord_upd.cl_id, ord_upd.cl_ord_id)]
        order.on_ord_upd(ord_upd)

        # # TODO wtf???
        # # enrich the cl_id and cl_ord_id
        # ord_upd.cl_id = order.cl_id()
        # ord_upd.cl_ord_id = order.cl_ord_id()

        # notify portfolio
        portfolio = self.app_context.portf_mgr.get_portfolio(order.portf_id())
        if portfolio:
            portfolio.on_ord_upd(ord_upd)
        else:
            logger.warn("portfolio [%s] not found for order cl_id [%s] cl_ord_id [%s]" % (
                order.portf_id(), order.cl_id(), order.cl_ord_id()))

        # notify stg
        stg = self.app_context.stg_mgr.get(order.cl_id())
        if stg:
            stg.oon_ord_upd(ord_upd)
        else:
            logger.warn(
                "stg [%s] not found for order cl_id [%s] cl_ord_id [%s]" % (
                    order.cl_id(), order.cl_id(), order.cl_ord_id()))

        # persist
        self._save_order(order)

    def on_exec_report(self, exec_report: ExecutionReport) -> None:
        super(OrderManager, self).on_exec_report(exec_report)

        # persist
        if hasattr(self, "store") and self.store and self.persist_mode != PersistenceMode.RealTime:
            self.store.save_exec_report(exec_report)

        # update order
        ord_id = self._cl_ord_id(exec_report)
        order = self.order_dict[ord_id]
        order.on_exec_report(exec_report)

        # notify portfolio
        portfolio = self.app_context.portf_mgr.get(order.portf_id())
        if portfolio:
            portfolio.on_exec_report(exec_report)
        else:
            logger.warn("portfolio [%s] not found for order cl_id [%s] cl_ord_id [%s]" % (
                order.portf_id(), order.cl_id(), order.cl_ord_id()))

        # notify stg
        stg = self.app_context.stg_mgr.get(order.cl_id())
        if stg:
            stg.on_exec_report(exec_report)
        else:
            logger.warn(
                "stg [%s] not found for order cl_id [%s] cl_ord_id [%s]" % (
                    order.cl_id(), order.cl_id(), order.cl_ord_id()))

            # persist
            # self._save_order(order)

    def send_order(self, new_ord_req: NewOrderRequest) -> Order:
        ord_id = self._cl_ord_id(new_ord_req)
        if ord_id in self.order_dict:
            raise Exception(
                "ClientOrderId has been used!! ord_id = %s" % (ord_id))

        # persist
        if hasattr(self, "store") and self.store and self.persist_mode != PersistenceMode.RealTime:
            self.store.save_new_order_req(new_ord_req)

        order = Order(ModelFactory.build_order_state_from_nos(new_ord_req))
        self.order_dict[ord_id] = order

        if order.broker_id():
            broker = self.app_context.provider_mgr.get(order.broker_id())
            if broker:
                broker.on_new_ord_req(new_ord_req)
            else:
                logger.warn("broker [%s] not found for order ord_id [%s]" % (
                    order.broker_id(), ord_id))

        # persist
        # self._save_order(order)

        return order

    def cancel_order(self, ord_cancel_req: OrderCancelRequest) -> Order:
        ord_id = self._cl_ord_id(ord_cancel_req)
        if not ord_id in self.order_dict:
            raise Exception("ClientOrderId not found!! ord_id = %s" % (
                ord_id))

        # persist
        if hasattr(self, "store") and self.store and self.persist_mode != PersistenceMode.RealTime:
            self.store.save_ord_cancel_req(ord_cancel_req)

        order = self.order_dict[ord_id]

        order.on_ord_cancel_req(ord_cancel_req)
        self.app_context.provider_mgr.get(order.broker_id()).on_ord_cancel_req(ord_cancel_req)

        # persist
        # self._save_order(order)

        return order

    def replace_order(self, ord_replace_req: OrderReplaceRequest) -> Order:
        ord_id = self._cl_ord_id(ord_replace_req)
        if not ord_id in self.order_dict:
            raise Exception("ClientOrderId not found!! ord_id = %s" % (
                ord_id))

        # persist
        if hasattr(self, "store") and self.store and self.persist_mode != PersistenceMode.RealTime:
            self.store.save_ord_replace_req(ord_replace_req)

        order = self.order_dict[ord_id]

        order.on_ord_replace_req(ord_replace_req)
        self.app_context.provider_mgr.get(order.broker_id()).on_ord_replace_req(ord_replace_req)

        # persist
        self._save_order(order)

        return order

    def id(self) -> str:
        return "OrderManager"

    def get_portf_orders(self, portf_id) -> List[Order]:
        return [order for order in self.order_dict.values() if order.portf_id() == portf_id]

    def get_strategy_orders(self, stg_id) -> List[Order]:
        return [order for order in self.order_dict.values() if order.cl_id() == stg_id]

    def get_portf_order_reqs(self, portf_id) -> List[NewOrderRequest]:
        return [new_ord_req for new_ord_req in self.ord_reqs_dict.values() if new_ord_req.portf_id == portf_id]

    def get_strategy_order_reqs(self, stg_id) -> List[NewOrderRequest]:
        return [new_ord_req for new_ord_req in self.ord_reqs_dict.values() if new_ord_req.cl_id == stg_id]

    def _save_order(self, order):
        if hasattr(self,
                   "store") and self.store and self.persist_mode != PersistenceMode.RealTime and self.persist_mode != PersistenceMode.Batch:
            self.store.save_order(order)

    def _cl_ord_id(self, item):
        return ModelFactory.build_cl_ord_id(item.cl_id, item.cl_ord_id)
