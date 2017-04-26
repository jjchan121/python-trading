from __future__ import absolute_import # IntelliJ/ Pycharm workaround http://stackoverflow.com/questions/38569992/pycharm-import-runtimewarning-after-updating-to-2016-2
import math
from gevent.ares import result
import collections
import talib
from datetime import datetime
from unittest import TestCase
import numpy as np
import datetime
from algotrader.technical import Indicator
from algotrader.technical.pipeline import PipeLine
from algotrader.technical.pipeline.rank import Rank
from algotrader.technical.pipeline.cross_sessional_apply import Average, Abs, Tail, Sign, DecayLinear, Scale
from algotrader.technical.pipeline.cross_sessional_apply import Sum as GSSum
from algotrader.technical.pipeline.make_vector import MakeVector
from algotrader.technical.pipeline.pairwise import Minus
from algotrader.technical.talib_wrapper import SMA
from algotrader.config.app import ApplicationConfig
from algotrader.trading.context import ApplicationContext


class PipelineTest(TestCase):
    def setUp(self):
        self.app_context = ApplicationContext()

    def assertDictEqual(self, d1, d2, msg=None): # assertEqual uses for dicts
        for k,v1 in d1.iteritems():
            self.assertIn(k, d2, msg)
            v2 = d2[k]
            if(isinstance(v1, collections.Iterable) and
                   not isinstance(v1, basestring)):
                self.assertItemsEqual(v1, v2, msg)
            else:
                self.assertEqual(v1, v2, msg)
        return True

    def test_name(self):

        bar = self.app_context.inst_data_mgr.get_series("bar")
        bar.start(self.app_context)
        sma3 = SMA(bar, input_key='close', length=3)
        sma20 = SMA(bar, input_key='close', length=20)
        sma50 = SMA(bar, input_key='close', length=50)
        sma3.start(self.app_context)
        sma20.start(self.app_context)
        sma50.start(self.app_context)

        rank = Rank([sma3, sma20, sma50], input_key='close')
        rank.start(self.app_context)
        self.assertEquals("Rank(SMA('bar',close,3),SMA('bar',close,20),SMA('bar',close,50),close)",
            rank.name)

        bar0 = self.app_context.inst_data_mgr.get_series("bar0")
        bar1 = self.app_context.inst_data_mgr.get_series("bar1")
        bar2 = self.app_context.inst_data_mgr.get_series("bar2")
        bar3 = self.app_context.inst_data_mgr.get_series("bar3")
        bar0.start(self.app_context)
        bar1.start(self.app_context)
        bar2.start(self.app_context)
        bar3.start(self.app_context)
        barlist = [bar0, bar1, bar2, bar3]

        avg = Average([bar0, bar1, bar2, bar3], input_key='close')
        gssum = GSSum([bar0, bar1, bar2, bar3], input_key='close')
        basket = MakeVector([bar0, bar1, bar2, bar3], input_key='close')
        # TODO: the name printed by pipeline now break the "parse" machnism so we have to review it
        self.assertEquals("Average('bar0','bar1','bar2','bar3',close)", avg.name)
        self.assertEquals("Sum('bar0','bar1','bar2','bar3',close)", gssum.name)
        self.assertEquals("MakeVector('bar0','bar1','bar2','bar3',close)", basket.name)

        bar4 = self.app_context.inst_data_mgr.get_series("bar4")
        bar5 = self.app_context.inst_data_mgr.get_series("bar5")
        bar6 = self.app_context.inst_data_mgr.get_series("bar6")
        bar7 = self.app_context.inst_data_mgr.get_series("bar7")
        basket2 = MakeVector([bar4, bar5, bar6, bar7], input_key='close')

        cross_basket_spread = Minus(basket2, basket)



    def test_empty_at_initialize(self):
        close = self.app_context.inst_data_mgr.get_series("bar")
        close.start(self.app_context)
        sma3 = SMA(close, input_key='close', length=3)
        sma20 = SMA(close, input_key='close', length=20)
        sma50 = SMA(close, input_key='close', length=50)

        sma3.start(self.app_context)
        sma20.start(self.app_context)

        rank = Rank([sma3, sma20, sma50], input_key='close')
        rank.start(self.app_context)
        self.assertEquals(0, len(rank.get_data()))

    def test_shape(self):
        close = self.app_context.inst_data_mgr.get_series("bar")
        close.start(self.app_context)

        sma3 = SMA(close, input_key='close', length=3)
        sma20 = SMA(close, input_key='close', length=20)
        sma50 = SMA(close, input_key='close', length=50)

        sma3.start(self.app_context)
        sma20.start(self.app_context)
        sma50.start(self.app_context)

        rank = Rank([sma3, sma20, sma50], input_key='close')
        rank.start(self.app_context)

        self.assertAlmostEqual([1, 3], rank.shape(), 5)
        # try:
        #     np.testing.assert_almost_equal(np.array([1, 3]), rank.shape(), 5)
        # except AssertionError as e:
        #     self.fail(e.message)

    def test_with_spread(self):
        bar0 = self.app_context.inst_data_mgr.get_series("bar0")
        bar1 = self.app_context.inst_data_mgr.get_series("bar1")
        bar2 = self.app_context.inst_data_mgr.get_series("bar2")
        bar3 = self.app_context.inst_data_mgr.get_series("bar3")

    def __np_assert_almost_equal(self, target, output, precision=10):
        try:
            np.testing.assert_almost_equal(target, output, precision)
        except AssertionError as e:
            self.fail(e.message)


    def test_sync(self):
        bar0 = self.app_context.inst_data_mgr.get_series("bar0")
        bar1 = self.app_context.inst_data_mgr.get_series("bar1")
        bar2 = self.app_context.inst_data_mgr.get_series("bar2")
        bar3 = self.app_context.inst_data_mgr.get_series("bar3")
        bar4 = self.app_context.inst_data_mgr.get_series("bar4")
        bar5 = self.app_context.inst_data_mgr.get_series("bar5")
        bar6 = self.app_context.inst_data_mgr.get_series("bar6")
        bar7 = self.app_context.inst_data_mgr.get_series("bar7")

        bar0.start(self.app_context)
        bar1.start(self.app_context)
        bar2.start(self.app_context)
        bar3.start(self.app_context)
        bar4.start(self.app_context)
        bar5.start(self.app_context)
        bar6.start(self.app_context)
        bar7.start(self.app_context)

        basket = PipeLine('Basket', [bar0, bar1, bar2, bar3], input_keys='close')
        basket2 = PipeLine('Basket2', [bar4, bar5, bar6, bar7], input_keys='close')

        basket.start(self.app_context)
        basket2.start(self.app_context)

        basket_open = PipeLine('Opens', [bar0, bar1, bar2, bar3], input_keys='open')
        basket_open2 = PipeLine('Opens2', [bar4, bar5, bar6, bar7], input_keys='open')
        # cross_basket_spread = Minus(basket2, basket, input_key=PipeLine.VALUE)

        basket_open.start(self.app_context)
        basket_open2.start(self.app_context)
        # cross_basket_spread.start(self.app_context)



        t1 = datetime.datetime.now()
        bar0.add({"timestamp": t1, "close": 80.0, "open": 0})
        # self.assertListEqual(nan_arr.tolist(),  basket.now()["value"])
        self.assertTrue(math.isnan(basket.now()))
        # self.assertEqual(basket.missing_value, basket.now())
        # self.__np_assert_almost_equal(nan_arr, np.array(basket.now()["value"]))

        bar1.add({"timestamp": t1, "close": 95.0, "open": 0})
        # self.assertListEqual(nan_arr.tolist(),  basket.now()["value"])
        self.assertTrue(math.isnan(basket.now()))
        # self.__np_assert_almost_equal(nan_arr, basket.now()["value"])

        bar2.add({"timestamp": t1, "close": 102.0, "open": 0})
        self.assertTrue(math.isnan(basket.now()))
        # self.assertListEqual(nan_arr.tolist(),  basket.now()["value"])
        # self.__np_assert_almost_equal(nan_arr, np.array(basket.now()["value"]))

        basket_slice = {"'bar0'": [80],
                        "'bar1'": [95.0],
                        "'bar2'": [102.0],
                        "'bar3'": [105.0]}

        bar3.add({"timestamp": t1, "close": 105.0, "open": 0})
        # print (basket.now())
        self.assertEqual(basket_slice, basket.now()["value"])
        # print basket.get_panel().ix[-1]

        bar4.add({"timestamp": t1, "close": 102.0, "open": 0})
        bar5.add({"timestamp": t1, "close": 95.0, "open": 0})
        bar6.add({"timestamp": t1, "close": 107.0, "open": 0})
        bar7.add({"timestamp": t1, "close": 101.0, "open": 0})

        # sync_vec2 = np.array([[102.0, 95.0, 107.0, 101.0]])
        sync_vec2 = [[102.0, 95.0, 107.0, 101.0]]
        basket_slice2 = {"'bar4'": [102.0],
                         "'bar5'": [95.0],
                         "'bar6'": [107.0],
                         "'bar7'": [101.0],
                         }

        self.assertEqual(basket_slice2, basket2.now()["value"] )



    # def test_nan_before_size(self):
    def test_with_multiple_bar(self):
        bar0 = self.app_context.inst_data_mgr.get_series("bar0")
        bar1 = self.app_context.inst_data_mgr.get_series("bar1")
        bar2 = self.app_context.inst_data_mgr.get_series("bar2")
        bar3 = self.app_context.inst_data_mgr.get_series("bar3")

        bar0.start(self.app_context)
        bar1.start(self.app_context)
        bar2.start(self.app_context)
        bar3.start(self.app_context)

        barlist = [bar0, bar1, bar2, bar3]

        rank = Rank(barlist, input_key='close')
        avg = Average(barlist, input_key='close')
        gssum = GSSum(barlist, input_key='close')
        absv = Abs(barlist, input_key='close')
        tail = Tail(barlist, lb=94, ub=103, newval=101, input_key='close')
        signvec = Sign(barlist, input_key='close')
        decaylinear = DecayLinear(barlist, length=3, input_key='close')
        scale = Scale(barlist, input_key='close')

        rank.start(self.app_context)
        avg.start(self.app_context)
        gssum.start(self.app_context)
        absv.start(self.app_context)
        tail.start(self.app_context)
        signvec.start(self.app_context)
        decaylinear.start(self.app_context)
        scale.start(self.app_context)

        t1 = datetime.datetime.now()
        bar_t1_array = np.array([80, 95, 102, 105])
        bar0.add({"timestamp": t1, "close": bar_t1_array[0], "open": 0})
        bar1.add({"timestamp": t1, "close": bar_t1_array[1], "open": 0})
        bar2.add({"timestamp": t1, "close": bar_t1_array[2], "open": 0})
        bar3.add({"timestamp": t1, "close": bar_t1_array[3], "open": 0})

        # self.assertEquals([{"timestamp": t1,
        #                     "name": "'Rank('bar0','bar1','bar2','bar3',close)'",
        #                     "value": np.arange(4)/3.0}],
        #                   rank.get_data())

        rank_target = np.arange(4)/3.0
        rank_target = rank_target.reshape((1,4))
        avg_target = 95.5 # for those return scala, it is a scala
        sum_target = 382.0
        abs_target = np.array([[80.0, 95.0, 102.0, 105.0]])
        tail_target = np.array([[80.0, 101.0, 101.0, 105.0]])
        signvec_target = np.array([[1.0, 1.0, 1.0, 1.0]])
        scale_target = bar_t1_array / np.sum(bar_t1_array)
        scale_target = scale_target.reshape(1, 4)

        # self.__np_assert_almost_equal(abs_target, absv.now()["value"])
        # self.__np_assert_almost_equal(rank_target, rank.get_data()[0]["value"], 5)
        # self.__np_assert_almost_equal(avg_target, avg.get_data()[0]["value"], 5)
        # self.__np_assert_almost_equal(sum_target, gssum.get_data()[0]["value"], 5)
        # self.__np_assert_almost_equal(tail_target, tail.get_data()[0]["value"], 5)
        # self.__np_assert_almost_equal(signvec_target, signvec.get_data()[0]["value"], 5)
        # self.__np_assert_almost_equal(scale_target, scale.get_data()[0]["value"], 5)

        self.assertAlmostEqual(abs_target.tolist(), absv.now()["value"])
        self.assertAlmostEqual(abs_target.tolist(), absv.get_data()[0]["value"], 5)
        self.assertAlmostEqual(rank_target.tolist(), rank.get_data()[0]["value"], 5)
        self.assertAlmostEqual(avg_target, avg.get_data()[0]["value"], 5)
        self.assertAlmostEqual(sum_target, gssum.get_data()[0]["value"], 5)
        self.assertAlmostEqual(tail_target.tolist(), tail.get_data()[0]["value"], 5)
        self.assertAlmostEqual(signvec_target.tolist(), signvec.get_data()[0]["value"], 5)
        self.assertAlmostEqual(scale_target.tolist(), scale.get_data()[0]["value"], 5)

        t2 = t1 + datetime.timedelta(0, 3)
        bar_t2_array = np.array([85, 98, 101.5, 103])
        bar0.add({"timestamp": t2, "close": bar_t2_array[0], "open": 0})
        bar1.add({"timestamp": t2, "close": bar_t2_array[1], "open": 0})
        bar2.add({"timestamp": t2, "close": bar_t2_array[2], "open": 0})
        bar3.add({"timestamp": t2, "close": bar_t2_array[3], "open": 0})

        t3 = t2 + datetime.timedelta(0, 3)
        bar_t3_array = np.array([87, 91, 107.0, 115])
        bar0.add({"timestamp": t3, "close": bar_t3_array[0], "open": 0})
        bar1.add({"timestamp": t3, "close": bar_t3_array[1], "open": 0})
        bar2.add({"timestamp": t3, "close": bar_t3_array[2], "open": 0})
        bar3.add({"timestamp": t3, "close": bar_t3_array[3], "open": 0})

        stack = np.vstack([bar_t1_array, bar_t2_array, bar_t3_array])
        decaylinear_target = np.dot(np.arange(3, 0, -1), stack)/np.sum(np.arange(3, 0, -1))
        scale_target = bar_t3_array / np.sum(bar_t3_array)
        scale_target = scale_target.reshape(1, 4)
        self.assertAlmostEqual(decaylinear_target.tolist(), decaylinear.now(keys=PipeLine.VALUE))
        self.assertAlmostEqual(scale_target.tolist(), scale.now(keys=PipeLine.VALUE))
        # self.__np_assert_almost_equal(decaylinear_target, decaylinear.now(keys=PipeLine.VALUE))
        # self.__np_assert_almost_equal(scale_target, scale.now(keys=PipeLine.VALUE))


    def test_with_multi_bar_multi_indicator(self):
        bar0 = self.app_context.inst_data_mgr.get_series("bar0")
        bar1 = self.app_context.inst_data_mgr.get_series("bar1")

        bar0.start(self.app_context)
        bar1.start(self.app_context)

        sma_2_bar0 = SMA(bar0, "close", 2)
        sma_4_bar0 = SMA(bar0, "close", 4)
        sma_3_bar1 = SMA(bar1, "close", 3)

        sma_2_bar0.start(self.app_context)
        sma_4_bar0.start(self.app_context)
        sma_3_bar1.start(self.app_context)

        rank = Rank([sma_2_bar0, sma_3_bar1, sma_4_bar0], input_key=Indicator.VALUE)
        rank.start(self.app_context)

        t = datetime.datetime.now()
        bar0.add({"timestamp": t, "close": 80.0, "open": 0})
        bar1.add({"timestamp": t, "close": 95.0, "open": 0})

        nan_arr = np.empty([1,3])
        nan_arr[:] = np.nan
        # self.assertListEqual(nan_arr.tolist(), rank.now()["value"])
        self.__np_assert_almost_equal(nan_arr, np.array(rank.now()["value"]))

        t = t + datetime.timedelta(0, 3)
        bar0.add({"timestamp": t, "close": 85.0, "open": 0})
        bar1.add({"timestamp": t, "close": 93.0, "open": 0})
        target = nan_arr
        target[0, 0] = 0.
        self.__np_assert_almost_equal(target, np.array(rank.now()["value"]))

        t = t + datetime.timedelta(0, 3)
        bar0.add({"timestamp": t, "close": 86.0, "open": 0})
        bar1.add({"timestamp": t, "close": 91.0, "open": 0})
        target[0, 1] = 0.5
        self.__np_assert_almost_equal(target.tolist(), rank.now()["value"])
        # self.__np_assert_almost_equal(target, rank.now()["value"])

        t = t + datetime.timedelta(0, 3)
        bar0.add({"timestamp": t, "close": 90.0, "open": 0})
        bar1.add({"timestamp": t, "close": 95.0, "open": 0})
        target = np.array([[0.5, 1.0, 0.]])

        # self.assertAlmostEqual(target.tolist(), rank.now()["value"])
        self.__np_assert_almost_equal(target, np.array(rank.now()["value"]))

    def test_with_multi_bar_multi_indicator_with_tail_start(self):
        bar0 = self.app_context.inst_data_mgr.get_series("bar0")
        bar1 = self.app_context.inst_data_mgr.get_series("bar1")

        bar0.start(self.app_context)
        bar1.start(self.app_context)

        # sma_2_bar0 = SMA(bar0, "close", 2)
        # sma_4_bar0 = SMA(bar0, "close", 4)
        # sma_3_bar1 = SMA(bar1, "close", 3)

        #
        # sma_2_bar0.start(self.app_context)
        # sma_4_bar0.start(self.app_context)
        # sma_3_bar1.start(self.app_context)

        # rank = Rank([sma_2_bar0, sma_3_bar1, sma_4_bar0], input_key=Indicator.VALUE)
        rank = Rank([SMA(bar0, "close", 2), SMA(bar1, "close", 3), SMA(bar0, "close", 4)], input_key=Indicator.VALUE)
        rank.start(self.app_context) # only start at the tail is enough

        t = datetime.datetime.now()
        bar0.add({"timestamp": t, "close": 80.0, "open": 0})
        bar1.add({"timestamp": t, "close": 95.0, "open": 0})

        nan_arr = np.empty([1,3])
        nan_arr[:] = np.nan
        # self.assertListEqual(nan_arr.tolist(), rank.now()["value"])
        self.__np_assert_almost_equal(nan_arr, np.array(rank.now()["value"]))

        t = t + datetime.timedelta(0, 3)
        bar0.add({"timestamp": t, "close": 85.0, "open": 0})
        bar1.add({"timestamp": t, "close": 93.0, "open": 0})
        target = nan_arr
        target[0, 0] = 0.
        self.__np_assert_almost_equal(target, np.array(rank.now()["value"]))

        t = t + datetime.timedelta(0, 3)
        bar0.add({"timestamp": t, "close": 86.0, "open": 0})
        bar1.add({"timestamp": t, "close": 91.0, "open": 0})
        target[0, 1] = 0.5
        self.__np_assert_almost_equal(target, np.array(rank.now()["value"]))

        t = t + datetime.timedelta(0, 3)
        bar0.add({"timestamp": t, "close": 90.0, "open": 0})
        bar1.add({"timestamp": t, "close": 95.0, "open": 0})
        target = np.array([[0.5, 1.0, 0.]])

        # self.assertAlmostEqual(target.tolist(), rank.now()["value"])
        self.__np_assert_almost_equal(target, np.array(rank.now()["value"]))

