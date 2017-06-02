"""
Created on 11/22/16
Author = jchan
"""
__author__ = 'jchan'


'''Simple example of requesting using the SWIG generated TWS wrapper to
request contract details from Interactive Brokers.

'''
import gevent
from gevent.event import Event
from gevent import monkey
from datetime import datetime
# from threading import Event
from swigibpy import EWrapper, EPosixClientSocket, Contract

monkey.patch_all(Event=True)


WAIT_TIME = 10.0


###


class ContractDetailsExample(EWrapper):
    '''Callback object passed to TWS, these functions will be called directly
    by TWS.

    '''

    def __init__(self):
        super(ContractDetailsExample, self).__init__()
        self.got_contract = Event()

    def orderStatus(self, id, status, filled, remaining, avgFillPrice, permId,
                    parentId, lastFilledPrice, clientId, whyHeld):
        pass

    def openOrder(self, orderID, contract, order, orderState):
        pass

    def nextValidId(self, orderId):
        '''Always called by TWS but not relevant for our example'''
        pass

    def openOrderEnd(self):
        '''Always called by TWS but not relevant for our example'''
        pass

    def managedAccounts(self, openOrderEnd):
        '''Called by TWS but not relevant for our example'''
        pass

    def contractDetailsEnd(self, reqId):
        print("Contract details request complete, (request id %i)" % reqId)

    def contractDetails(self, reqId, contractDetails):
        print("Contract details received (request id %i):" % reqId)
        print("callable: %s" % contractDetails.callable)
        print("category: %s" % contractDetails.category)
        print("contractMonth: %s" % contractDetails.contractMonth)
        print("convertible: %s" % contractDetails.convertible)
        print("coupon: %s" % contractDetails.coupon)
        print("industry: %s" % contractDetails.industry)
        print("liquidHours: %s" % contractDetails.liquidHours)
        print("longName: %s" % contractDetails.longName)
        print("marketName: %s" % contractDetails.marketName)
        print("minTick: %s" % contractDetails.minTick)
        print("nextOptionPartial: %s" % contractDetails.nextOptionPartial)
        print("orderTypes: %s" % contractDetails.orderTypes)
        print("priceMagnifier: %s" % contractDetails.priceMagnifier)
        print("putable: %s" % contractDetails.putable)
        if contractDetails.secIdList is not None:
            for secId in contractDetails.secIdList:
                print("secIdList: %s" % secId)
        else:
            print("secIdList: None")

        print("subcategory: %s" % contractDetails.subcategory)
        print("tradingHours: %s" % contractDetails.tradingHours)
        print("timeZoneId: %s" % contractDetails.timeZoneId)
        print("underConId: %s" % contractDetails.underConId)
        print("evRule: %s" % contractDetails.evRule)
        print("evMultiplier: %s" % contractDetails.evMultiplier)

        contract = contractDetails.summary

        print("\nContract Summary:")
        print("exchange: %s" % contract.exchange)
        print("symbol: %s" % contract.symbol)
        print("secType: %s" % contract.secType)
        print("currency: %s" % contract.currency)
        print("tradingClass: %s" % contract.tradingClass)
        if contract.comboLegs is not None:
            for comboLeg in contract.comboLegs:
                print("comboLegs: %s - %s" %
                      (comboLeg.action, comboLeg.exchange))
        else:
            print("comboLegs: None")

        print("\nBond Values:")
        print("bondType: %s" % contractDetails.bondType)
        print("couponType: %s" % contractDetails.couponType)
        print("cusip: %s" % contractDetails.cusip)
        print("descAppend: %s" % contractDetails.descAppend)
        print("issueDate: %s" % contractDetails.issueDate)
        print("maturity: %s" % contractDetails.maturity)
        print("nextOptionDate: %s" % contractDetails.nextOptionDate)
        print("nextOptionType: %s" % contractDetails.nextOptionType)
        print("notes: %s" % contractDetails.notes)
        print("ratings: %s" % contractDetails.ratings)
        print("validExchanges: %s" % contractDetails.validExchanges)

        self.got_contract.set()


# Instantiate our callback object
callback = ContractDetailsExample()

# Instantiate a socket object, allowing us to call TWS directly. Pass our
# callback object so TWS can respond.
tws = EPosixClientSocket(callback)

# Connect to tws running on localhost
port = 4001
# port = 7496
if not tws.eConnect("", port, 42):
    raise RuntimeError('Failed to connect to TWS')

# Simple contract for GOOG
contract = Contract()
contract.exchange = "SMART"
contract.symbol = "GOOG"
contract.secType = "STK"
contract.currency = "USD"
today = datetime.today()

print("Requesting contract details...")

# Perform the request
tws.reqContractDetails(
    42,                                         # reqId,
    contract,                                   # contract,
)

print("\n====================================================================")
print(" Contract details requested, waiting %ds for TWS responses" % WAIT_TIME)
print("====================================================================\n")


try:
    callback.got_contract.wait(timeout=WAIT_TIME)
except KeyboardInterrupt:
    pass
finally:
    if not callback.got_contract.is_set():
        print('Failed to get contract within %d seconds' % WAIT_TIME)

    print("\nDisconnecting...")
    tws.eDisconnect()

