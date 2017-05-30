import abc
import pandas as pd
from algotrader.config.config import Config


class FeedConfig(Config):
    __metaclass__ = abc.ABCMeta


class CSVFeedConfig(FeedConfig):
    __slots__ = (
        'path',
    )

    def __init__(self, path='../data/tradedata'):
        super(CSVFeedConfig, self).__init__(CSVFeedConfig.__class__.__name__)
        self.path = path


class PandasMemoryDataFeedConfig(FeedConfig):
    __slots__ = (
        'df',
    )

    def __init__(self, df=None):
        super(PandasMemoryDataFeedConfig, self).__init__(PandasMemoryDataFeedConfig.__class__.__name__)
        self.df = df if df is not None else pd.DataFrame()
