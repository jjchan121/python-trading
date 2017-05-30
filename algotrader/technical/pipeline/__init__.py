from algotrader.utils.time_series import DataSeries
from algotrader.technical import Indicator
import numpy as np
import pandas as pd
from collections import OrderedDict
from algotrader.utils import logger

class PipeLine(DataSeries):
    VALUE = 'value'

    __slots__ = (
        'cache',
        'numPipes',
        'length',
        'input_names',
        'input_names_pos',
        'input_names_and_series',
        'input_keys',
        '__curr_timestamp'
    )

    __transient__ = (
        'app_context',
        'inputs',
    )

    @staticmethod
    def get_name(indicator_name, inputs, input_key, *args):
        parts = []
        parts.extend(DataSeries.convert_to_list(PipeLine.get_input_name(inputs)))

        if input_key:
            parts.extend(DataSeries.convert_to_list(input_key))
        if args:
            parts.extend(args)
        content = ",".join(str(part) for part in parts)
        return '%s(%s)' % (indicator_name, content)

    @staticmethod
    def get_input_name(inputs):
        parts = []
        if isinstance(inputs, list):
            parts.extend([Indicator.get_input_name(i) for i in inputs])
        else:
            # parts.extend(Indicator.get_input_name(inputs))
            parts.append(Indicator.get_input_name(inputs))

        return ",".join(str(part) for part in parts)

    def __init__(self, name, inputs, input_keys, length=None, desc=None, fire_on_all = True, **kwargs):
        """
        :param name: Name of the Pipeline to be created
        :param inputs: list of DataSeries that want to sync to one Pipeline
        :param input_keys: Input Keys
        :param length: Lookback period of each inputs in constructing Pipeline
        :param desc: Description
        :param fire_on_all: If set to True, only fire a data slice when all inputs has updated and create one synced value
                            If set to False, whenever an input has changed timestamp, one update will be created with missing
                            input as Nan
        :param kwargs:
        """
        super(PipeLine, self).__init__(name=name, keys=None, desc=desc, **kwargs)

        input_names = []
        self.input_names_and_series = OrderedDict()
        if isinstance(inputs, list):
            for i in inputs:
                if isinstance(i, DataSeries):
                    input_name = DataSeries.get_name(i)
                    input_names.append(input_name)
                    self.input_names_and_series[input_name] = i
                elif isinstance(i, Indicator):
                    input_name = Indicator.get_name(i)
                    input_names.append(input_name)
                    self.input_names_and_series[input_name] = i
                elif isinstance(i, PipeLine):
                    input_name = PipeLine.get_name(i)
                    input_names.append(input_name)
                    self.input_names_and_series[input_name] = i
                else:
                    input_names.append(i)
        else:
            if isinstance(inputs, DataSeries):
                input_name = DataSeries.get_name(inputs)
                input_names.append(input_name)
                self.input_names_and_series[input_name] = inputs
            elif isinstance(inputs, Indicator):
                input_name = Indicator.get_name(inputs)
                input_names.append(input_name)
                self.input_names_and_series[input_name] = inputs
            elif isinstance(inputs, PipeLine):
                input_name = PipeLine.get_name(inputs)
                input_names.append(input_name)
                self.input_names_and_series[input_name] = inputs
            else:
                input_names.append(inputs)

        self.numPipes = len(input_names)
        self.length = length if length is not None else 1
        self.input_names = input_names
        self.input_names_pos = dict(zip(input_names,
                                        range(len(input_names))))

        self.input_keys = self._get_key(input_keys, None)
        # self.calculate = True
        self.__curr_timestamp = None
        self._flush_and_create()
        self.inputs = []
        self.cache = {} # OrderedDict()
        self.fire_on_all = fire_on_all
        # self.df = pd.DataFrame(index=range(self.length), columns=input_names)
        # self.cache = {} # key is input name, value is numpy array
        # self.update_all()

    def _start(self, app_context, *args, **kwargs):
        super(PipeLine, self)._start(self.app_context, *args, **kwargs)

        # if not hasattr(self, 'inputs') or not self.inputs:
        #     self.inputs = [self.app_context.inst_data_mgr.get_series(name) for name in self.input_names]
        missing_input_names = [k for k,v in self.input_names_and_series.iteritems() if v is None]
        for name in missing_input_names:
            self.input_names_and_series[k] = self.app_context.inst_data_mgr.get_series(name)

        self.inputs = self.input_names_and_series.values()
        self.app_context.inst_data_mgr.add_series(self)

        self.update_all()
        # for i in self.input_names_and_series.values():
        for i in self.inputs:
            i.start(app_context, *args, **kwargs)
            i.subject.subscribe(self.on_update)

    def _stop(self):
        pass

    def _flush_and_create(self):
        # self.df = pd.DataFrame(index=range(self.length), columns=self.input_names)
        # self.cache = OrderedDict(zip(self.input_names, [None for i in range(len(self.input_names))]))
        self.cache = {k : None for k in self.input_names}

    def _submit_cache(self):
        logger.debug("[%s] _submit_cache" % self.__class__.__name__)
        result = {}
        result['timestamp'] = self.__curr_timestamp
        result[PipeLine.VALUE] = self.cache
        self.add(result)


    def update_all(self):
        for input in self.inputs:
            data_list = input.get_data()
            for data in data_list:
                self.on_update(data)
                # if self.input_keys:
                #     filtered_data = {key: data[key] for key in self.input_keys}
                #     filtered_data['timestamp'] = data['timestamp']
                #     self.on_update(filtered_data)
                # else:
                #     self.on_update(data)

    def all_filled(self):
        """
        PipeLine specify function, check in all input in self.inputs have been updated
        :return:
        """
        has_none = np.sum(np.array([v is None for v in self.cache.values()]))
        return False if has_none > 0 else True
        # check_df = self.df.isnull()*1
        # return False if check_df.sum(axis=1).sum(axis=0) > 0 else True

    def on_update(self, data):
        logger.debug("[%s] on_update %s" % (self.__class__.__name__, data))
        if data['timestamp'] != self.__curr_timestamp:
            self.__curr_timestamp = data['timestamp']
            if not self.fire_on_all:
                self._submit_cache()
            self._flush_and_create()

        data_name = data['name']
        if data_name in self.input_names:
            j = self.input_names_pos[data_name]
            self.cache[data_name] = self.inputs[j].get_by_idx(
                keys=self.input_keys,
                idx=slice(-self.length, None, None))

        if self.fire_on_all and self.all_filled():
            self._submit_cache()
            # logger.debug("[%s] all_filled %s" % (self.__class__.__name__, data))
            # result = {}
            # result['timestamp'] = data['timestamp']
            # result[PipeLine.VALUE] = self.cache
            # self.add(result)

    def numPipes(self):
        return self.numPipes

    def shape(self):
        raise NotImplementedError()






