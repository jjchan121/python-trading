import time
from datetime import date, timedelta

from algotrader.event.order import *
from algotrader.provider import *
from algotrader.provider.broker.ib.ib_broker import IBBroker
from algotrader.utils import logger


class EventPrinter(ExecutionEventHandler, MarketDataEventHandler):
    def __init__(self):
        EventBus.data_subject.subscribe(self.on_next)
        EventBus.execution_subject.subscribe(self.on_next)

    def on_ord_upd(self, ord_upd):
        logger.info(ord_upd)

    def on_exec_report(self, exec_report):
        logger.info(exec_report)

    def on_bar(self, bar):
        logger.info(bar)

    def on_quote(self, quote):
        logger.info(quote)

    def on_trade(self, trade):
        logger.info(trade)

    def on_market_depth(self, market_depth):
        logger.info(market_depth)

today = date.today()

def sub_hist_data(broker, inst_id, day_ago):
    sub_key = HistDataSubscriptionKey(inst_id=inst_id, provider_id=IBBroker.ID, data_type=Bar, bar_size=BarSize.D1, from_date=(today - timedelta(days=day_ago)), to_date=today)
    broker.subscribe_mktdata(sub_key)
    return sub_key


def sub_realtime_bar(broker, inst_id):
    sub_key = SubscriptionKey(inst_id=inst_id, provider_id=IBBroker.ID, data_type=Bar, bar_size=BarSize.S5)
    broker.subscribe_mktdata(sub_key)
    return sub_key


def sub_realtime_trade(broker, inst_id):
    sub_key = SubscriptionKey(inst_id=inst_id, provider_id=IBBroker.ID, data_type=Trade, bar_size=BarSize.S1)
    broker.subscribe_mktdata(sub_key)
    return sub_key

def sub_realtime_quote(broker, inst_id):
    sub_key = SubscriptionKey(inst_id=inst_id, provider_id=IBBroker.ID, data_type=Quote, bar_size=BarSize.S1)
    broker.subscribe_mktdata(sub_key)
    return sub_key



def test_sub_hist_bar(broker):
    print "### requesting hist bar"
    sub_key = sub_hist_data(broker, 3, 5)
    time.sleep(5)
    print "### cancelling hist bar"
    broker.unsubscribe_mktdata(sub_key)
    time.sleep(2)

def test_sub_realtime_bar(broker):
    print "### requesting realtime bar"
    sub_key = sub_realtime_bar(broker, 3)
    time.sleep(20)
    print "### cancelling realtime bar"
    broker.unsubscribe_mktdata(sub_key)
    time.sleep(2)


def test_sub_realtime_trade(broker):
    print "### requesting realtime trade"
    sub_key = sub_realtime_trade(broker, 3)
    time.sleep(20)
    print "### cancelling realtime trade"
    broker.unsubscribe_mktdata(sub_key)
    time.sleep(2)

def test_sub_realtime_quote(broker):
    print "### requesting realtime quote"
    sub_key = sub_realtime_quote(broker, 3)
    time.sleep(20)
    print "### cancelling realtime quote"
    broker.unsubscribe_mktdata(sub_key)
    time.sleep(2)


def test_mkt_order(broker):
    order = Order(cl_ord_id=1, instrument=3, action=OrdAction.BUY, type=OrdType.MARKET, qty=1000)
    broker.on_order(order)
    time.sleep(10)


def test_lmt_order_update_cancel(broker):
    order = Order(cl_ord_id=1, instrument=3, action=OrdAction.BUY, type=OrdType.LIMIT, qty=1000, limit_price=100)
    broker.on_order(order)
    time.sleep(10)

    order = Order(cl_ord_id=1, instrument=3, action=OrdAction.BUY, type=OrdType.LIMIT, qty=1000, limit_price=200)
    broker.on_ord_update_req(order)
    time.sleep(10)

    broker.on_ord_cancel_req(order)
    time.sleep(10)



if __name__ == "__main__":
    broker = IBBroker()
    broker.start()
    printer = EventPrinter()

    test_lmt_order_update_cancel(broker)