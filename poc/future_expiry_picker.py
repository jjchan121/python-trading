"""
Created on 11/17/16
Author = jchan
"""
__author__ = 'jchan'

from math import pi
from pymongo import MongoClient
from algotrader.utils.ser_deser import JsonSerializer, MsgPackSerializer, MapSerializer
import pandas as pd
from algotrader.event.market_data import Bar
from itertools import chain
from algotrader.utils.date_utils import DateUtils
from algotrader.config.persistence import MongoDBConfig, PersistenceConfig
from algotrader.provider.persistence import PersistenceMode
from algotrader.provider.persistence.data_store import DataStore
from algotrader.trading.ref_data import RefDataManager, \
    DBRefDataManager, Instrument, Currency, Exchange, InstType
from algotrader.utils.clock import Clock
from algotrader.config.app import ApplicationConfig
from algotrader.trading.context import ApplicationContext

def get_default_app_context():
    config = MongoDBConfig()
    persistence_config = PersistenceConfig(None,
                                           DataStore.Mongo, PersistenceMode.RealTime,
                                           DataStore.Mongo, PersistenceMode.RealTime,
                                           DataStore.Mongo, PersistenceMode.RealTime,
                                           DataStore.Mongo, PersistenceMode.RealTime)

    app_config = ApplicationConfig("POC",
                                   RefDataManager.DB,
                                   Clock.Simulation,
                                   persistence_config,
                                   config)

    # app_config = ApplicationConfig(None, None, None, persistence_config,
    #                                config)
    return ApplicationContext(app_config=app_config)




context = get_default_app_context()
client = MongoClient('localhost', 27017)

store = context.provider_mgr.get(DataStore.Mongo)
store.start(app_context=context)

ref_data_mgr = context.ref_data_mgr
ref_data_mgr.start(app_context=context)


import datetime
reval_date = datetime.datetime(2014, 12, 15, 0, 0, 0)
#instruments = [ref_data_mgr.get_inst(symbol='VXF2015'), ref_data_mgr.get_inst(symbol='VXJ2015'), ref_data_mgr.get_inst(symbol='VXZ2015')]
instruments = ref_data_mgr.get_all_insts()

import re
re.match('VX.[0-9]', 'VXF2016')
vix_futures = [instru for instru in instruments if instru.type == 'FUT' and re.match("VX.[0-9]{4}$",instru.symbol)]


# for i in instruments:
#     (i.expiry_date - reval_date).days
#
# ins.expiry_date - reval_date
#
# ins = instruments[0]

def future_expirydays_calculator(instruments):
    return {i.inst_id: (i.expiry_date - reval_date).days for i in instruments}


caldict = future_expirydays_calculator(vix_futures)

filtered_ins = [k for k, v in caldict.iteritems() if v < 90 and v > 0]

inst = ref_data_mgr.get_inst(symbol='VIX')

font_contract = ref_data_mgr.get_inst(inst_id= filtered_ins[0])

import pandas as pd
atts = ['symbol', 'expiry_date', 'inst_id', 'name']
df = pd.DataFrame([[getattr(i, j) for j in atts] for i in vix_futures], columns = atts)
df['days'] = df['expiry_date'].apply(lambda x : (x - reval_date).days)
df['days']