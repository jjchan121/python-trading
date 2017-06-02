from algotrader.event.order import OrdAction
from algotrader.strategy.strategy import Strategy
from algotrader.trading.instrument_data import inst_data_mgr
from algotrader.utils import logger
from algotrader.technical.pipeline import PipeLine
from algotrader.technical.pipeline.cross_sessional_apply import Average, Abs, Sum, Log, Delta
from algotrader.technical.pipeline.pairwise import Divides, Minus
import numpy as np

class CrossSectionalMR(Strategy):
    def __init__(self, stg_id, portfolio, instruments, qty,
                 trading_config, ref_data_mgr=None):
        super(CrossSectionalMR, self).__init__(stg_id, portfolio, instruments, trading_config, ref_data_mgr)
        self.day_count = 0
        self.order = None
        self.qty = qty
        bars = [inst_data_mgr.get_series("Bar.%s.Time.86400" % instru) for instru in instruments]
        self.close = PipeLine('closes', bars, input_key='close')
        self.log_close = Log(self.close, input_key=PipeLine.VALUE)
        self.returns = Minus(self.log_close, Delta(self.log_close, length=1))
        self.avg_returns = Average(self.returns, input_key=PipeLine.VALUE)
        self.deviation = Minus(self.returns, self.avg_returns)
        self.abs_deviation = Abs(self.deviation, input_key=PipeLine.VALUE)
        self.weight = Divides(Minus(self.avg_returns, self.returns), Sum(Abs(self.abs_deviation)))
        self.prev_weight = np.zeros((1, len(instruments)), dtype='float32')

    def on_bar(self, bar):
        pass

