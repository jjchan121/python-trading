# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algotrader/model/market_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='algotrader/model/market_data.proto',
  package='algotrader.model',
  syntax='proto3',
  serialized_pb=_b('\n\"algotrader/model/market_data.proto\x12\x10\x61lgotrader.model\"\xc0\x02\n\x03\x42\x61r\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.algotrader.model.Bar.Type\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x13\n\x0bprovider_id\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x12\x10\n\x08utc_time\x18\x06 \x01(\x03\x12\x12\n\nbegin_time\x18\x07 \x01(\x03\x12\x0c\n\x04open\x18\t \x01(\x01\x12\x0c\n\x04high\x18\n \x01(\x01\x12\x0b\n\x03low\x18\x0b \x01(\x01\x12\r\n\x05\x63lose\x18\x0c \x01(\x01\x12\x0b\n\x03vol\x18\r \x01(\x01\x12\x11\n\tadj_close\x18\x0e \x01(\x01\x12\x15\n\ropen_interest\x18\x0f \x01(\x01\"3\n\x04Type\x12\x08\n\x04Time\x10\x00\x12\x08\n\x04Tick\x10\x01\x12\n\n\x06Volume\x10\x02\x12\x0b\n\x07\x44ynamic\x10\x03\"\x90\x01\n\x05Quote\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x10\n\x08utc_time\x18\x04 \x01(\x03\x12\x0b\n\x03\x62id\x18\x05 \x01(\x01\x12\x10\n\x08\x62id_size\x18\x06 \x01(\x01\x12\x0b\n\x03\x61sk\x18\x07 \x01(\x01\x12\x10\n\x08\x61sk_size\x18\x08 \x01(\x01\"o\n\x05Trade\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x10\n\x08utc_time\x18\x04 \x01(\x03\x12\r\n\x05price\x18\x05 \x01(\x01\x12\x0c\n\x04size\x18\x06 \x01(\x01\"\xd5\x02\n\x0bMarketDepth\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x10\n\x08utc_time\x18\x04 \x01(\x03\x12\x13\n\x0bmd_provider\x18\x05 \x01(\t\x12\x10\n\x08position\x18\x06 \x01(\x03\x12:\n\toperation\x18\x07 \x01(\x0e\x32\'.algotrader.model.MarketDepth.Operation\x12\x30\n\x04side\x18\x08 \x01(\x0e\x32\".algotrader.model.MarketDepth.Side\x12\r\n\x05price\x18\t \x01(\x01\x12\x0c\n\x04size\x18\n \x01(\x01\"\x18\n\x04Side\x12\x07\n\x03\x41sk\x10\x00\x12\x07\n\x03\x42id\x10\x01\"/\n\tOperation\x12\n\n\x06Insert\x10\x00\x12\n\n\x06Update\x10\x01\x12\n\n\x06\x44\x65lete\x10\x02\"b\n\x16\x42\x61rSubscriptionRequest\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x11\n\tfrom_date\x18\x03 \x01(\x03\x12\x0f\n\x07to_date\x18\x04 \x01(\x03\"d\n\x18QuoteSubscriptionRequest\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x11\n\tfrom_date\x18\x03 \x01(\x03\x12\x0f\n\x07to_date\x18\x04 \x01(\x03\"d\n\x18TradeSubscriptionRequest\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x11\n\tfrom_date\x18\x03 \x01(\x03\x12\x0f\n\x07to_date\x18\x04 \x01(\x03\"\x94\x01\n\x1eMarketDepthSubscriptionRequest\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x10\n\x08num_rows\x18\x03 \x01(\x05\x12\x16\n\x0emd_provider_id\x18\x04 \x01(\t\x12\x11\n\tfrom_date\x18\x05 \x01(\x03\x12\x0f\n\x07to_date\x18\x06 \x01(\x03\"\xa1\x02\n\x15\x42\x61rAggregationRequest\x12\x0f\n\x07inst_id\x18\x01 \x01(\t\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x45\n\ninput_type\x18\x03 \x01(\x0e\x32\x31.algotrader.model.BarAggregationRequest.InputType\x12/\n\x0boutput_type\x18\x04 \x01(\x0e\x32\x1a.algotrader.model.Bar.Type\x12\x13\n\x0boutput_size\x18\x05 \x01(\x05\"U\n\tInputType\x12\x07\n\x03\x42\x61r\x10\x00\x12\t\n\x05Trade\x10\x01\x12\x07\n\x03\x42id\x10\x02\x12\x07\n\x03\x41sk\x10\x03\x12\n\n\x06\x42idAsk\x10\x04\x12\n\n\x06Middle\x10\x05\x12\n\n\x06Spread\x10\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BAR_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='algotrader.model.Bar.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Time', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Tick', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Volume', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Dynamic', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=326,
  serialized_end=377,
)
_sym_db.RegisterEnumDescriptor(_BAR_TYPE)

_MARKETDEPTH_SIDE = _descriptor.EnumDescriptor(
  name='Side',
  full_name='algotrader.model.MarketDepth.Side',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Ask', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Bid', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=908,
  serialized_end=932,
)
_sym_db.RegisterEnumDescriptor(_MARKETDEPTH_SIDE)

_MARKETDEPTH_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='algotrader.model.MarketDepth.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Insert', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Update', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Delete', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=934,
  serialized_end=981,
)
_sym_db.RegisterEnumDescriptor(_MARKETDEPTH_OPERATION)

_BARAGGREGATIONREQUEST_INPUTTYPE = _descriptor.EnumDescriptor(
  name='InputType',
  full_name='algotrader.model.BarAggregationRequest.InputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Bar', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Trade', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Bid', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ask', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BidAsk', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Middle', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Spread', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1643,
  serialized_end=1728,
)
_sym_db.RegisterEnumDescriptor(_BARAGGREGATIONREQUEST_INPUTTYPE)


_BAR = _descriptor.Descriptor(
  name='Bar',
  full_name='algotrader.model.Bar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.Bar.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='algotrader.model.Bar.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='algotrader.model.Bar.size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.Bar.provider_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='algotrader.model.Bar.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utc_time', full_name='algotrader.model.Bar.utc_time', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='begin_time', full_name='algotrader.model.Bar.begin_time', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='algotrader.model.Bar.open', index=7,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='algotrader.model.Bar.high', index=8,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='algotrader.model.Bar.low', index=9,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='algotrader.model.Bar.close', index=10,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vol', full_name='algotrader.model.Bar.vol', index=11,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adj_close', full_name='algotrader.model.Bar.adj_close', index=12,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_interest', full_name='algotrader.model.Bar.open_interest', index=13,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BAR_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=377,
)


_QUOTE = _descriptor.Descriptor(
  name='Quote',
  full_name='algotrader.model.Quote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.Quote.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.Quote.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='algotrader.model.Quote.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utc_time', full_name='algotrader.model.Quote.utc_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid', full_name='algotrader.model.Quote.bid', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_size', full_name='algotrader.model.Quote.bid_size', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask', full_name='algotrader.model.Quote.ask', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_size', full_name='algotrader.model.Quote.ask_size', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=524,
)


_TRADE = _descriptor.Descriptor(
  name='Trade',
  full_name='algotrader.model.Trade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.Trade.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.Trade.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='algotrader.model.Trade.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utc_time', full_name='algotrader.model.Trade.utc_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='algotrader.model.Trade.price', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='algotrader.model.Trade.size', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=637,
)


_MARKETDEPTH = _descriptor.Descriptor(
  name='MarketDepth',
  full_name='algotrader.model.MarketDepth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.MarketDepth.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.MarketDepth.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='algotrader.model.MarketDepth.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utc_time', full_name='algotrader.model.MarketDepth.utc_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='md_provider', full_name='algotrader.model.MarketDepth.md_provider', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='algotrader.model.MarketDepth.position', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='algotrader.model.MarketDepth.operation', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='side', full_name='algotrader.model.MarketDepth.side', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='algotrader.model.MarketDepth.price', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='algotrader.model.MarketDepth.size', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MARKETDEPTH_SIDE,
    _MARKETDEPTH_OPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=981,
)


_BARSUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='BarSubscriptionRequest',
  full_name='algotrader.model.BarSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.BarSubscriptionRequest.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.BarSubscriptionRequest.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='algotrader.model.BarSubscriptionRequest.from_date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='algotrader.model.BarSubscriptionRequest.to_date', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=983,
  serialized_end=1081,
)


_QUOTESUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='QuoteSubscriptionRequest',
  full_name='algotrader.model.QuoteSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.QuoteSubscriptionRequest.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.QuoteSubscriptionRequest.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='algotrader.model.QuoteSubscriptionRequest.from_date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='algotrader.model.QuoteSubscriptionRequest.to_date', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1083,
  serialized_end=1183,
)


_TRADESUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='TradeSubscriptionRequest',
  full_name='algotrader.model.TradeSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.TradeSubscriptionRequest.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.TradeSubscriptionRequest.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='algotrader.model.TradeSubscriptionRequest.from_date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='algotrader.model.TradeSubscriptionRequest.to_date', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1185,
  serialized_end=1285,
)


_MARKETDEPTHSUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='MarketDepthSubscriptionRequest',
  full_name='algotrader.model.MarketDepthSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.MarketDepthSubscriptionRequest.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.MarketDepthSubscriptionRequest.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_rows', full_name='algotrader.model.MarketDepthSubscriptionRequest.num_rows', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='md_provider_id', full_name='algotrader.model.MarketDepthSubscriptionRequest.md_provider_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='algotrader.model.MarketDepthSubscriptionRequest.from_date', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='algotrader.model.MarketDepthSubscriptionRequest.to_date', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1288,
  serialized_end=1436,
)


_BARAGGREGATIONREQUEST = _descriptor.Descriptor(
  name='BarAggregationRequest',
  full_name='algotrader.model.BarAggregationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_id', full_name='algotrader.model.BarAggregationRequest.inst_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='algotrader.model.BarAggregationRequest.provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_type', full_name='algotrader.model.BarAggregationRequest.input_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_type', full_name='algotrader.model.BarAggregationRequest.output_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_size', full_name='algotrader.model.BarAggregationRequest.output_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BARAGGREGATIONREQUEST_INPUTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1439,
  serialized_end=1728,
)

_BAR.fields_by_name['type'].enum_type = _BAR_TYPE
_BAR_TYPE.containing_type = _BAR
_MARKETDEPTH.fields_by_name['operation'].enum_type = _MARKETDEPTH_OPERATION
_MARKETDEPTH.fields_by_name['side'].enum_type = _MARKETDEPTH_SIDE
_MARKETDEPTH_SIDE.containing_type = _MARKETDEPTH
_MARKETDEPTH_OPERATION.containing_type = _MARKETDEPTH
_BARAGGREGATIONREQUEST.fields_by_name['input_type'].enum_type = _BARAGGREGATIONREQUEST_INPUTTYPE
_BARAGGREGATIONREQUEST.fields_by_name['output_type'].enum_type = _BAR_TYPE
_BARAGGREGATIONREQUEST_INPUTTYPE.containing_type = _BARAGGREGATIONREQUEST
DESCRIPTOR.message_types_by_name['Bar'] = _BAR
DESCRIPTOR.message_types_by_name['Quote'] = _QUOTE
DESCRIPTOR.message_types_by_name['Trade'] = _TRADE
DESCRIPTOR.message_types_by_name['MarketDepth'] = _MARKETDEPTH
DESCRIPTOR.message_types_by_name['BarSubscriptionRequest'] = _BARSUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['QuoteSubscriptionRequest'] = _QUOTESUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['TradeSubscriptionRequest'] = _TRADESUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['MarketDepthSubscriptionRequest'] = _MARKETDEPTHSUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['BarAggregationRequest'] = _BARAGGREGATIONREQUEST

Bar = _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), dict(
  DESCRIPTOR = _BAR,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.Bar)
  ))
_sym_db.RegisterMessage(Bar)

Quote = _reflection.GeneratedProtocolMessageType('Quote', (_message.Message,), dict(
  DESCRIPTOR = _QUOTE,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.Quote)
  ))
_sym_db.RegisterMessage(Quote)

Trade = _reflection.GeneratedProtocolMessageType('Trade', (_message.Message,), dict(
  DESCRIPTOR = _TRADE,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.Trade)
  ))
_sym_db.RegisterMessage(Trade)

MarketDepth = _reflection.GeneratedProtocolMessageType('MarketDepth', (_message.Message,), dict(
  DESCRIPTOR = _MARKETDEPTH,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.MarketDepth)
  ))
_sym_db.RegisterMessage(MarketDepth)

BarSubscriptionRequest = _reflection.GeneratedProtocolMessageType('BarSubscriptionRequest', (_message.Message,), dict(
  DESCRIPTOR = _BARSUBSCRIPTIONREQUEST,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.BarSubscriptionRequest)
  ))
_sym_db.RegisterMessage(BarSubscriptionRequest)

QuoteSubscriptionRequest = _reflection.GeneratedProtocolMessageType('QuoteSubscriptionRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUOTESUBSCRIPTIONREQUEST,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.QuoteSubscriptionRequest)
  ))
_sym_db.RegisterMessage(QuoteSubscriptionRequest)

TradeSubscriptionRequest = _reflection.GeneratedProtocolMessageType('TradeSubscriptionRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRADESUBSCRIPTIONREQUEST,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.TradeSubscriptionRequest)
  ))
_sym_db.RegisterMessage(TradeSubscriptionRequest)

MarketDepthSubscriptionRequest = _reflection.GeneratedProtocolMessageType('MarketDepthSubscriptionRequest', (_message.Message,), dict(
  DESCRIPTOR = _MARKETDEPTHSUBSCRIPTIONREQUEST,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.MarketDepthSubscriptionRequest)
  ))
_sym_db.RegisterMessage(MarketDepthSubscriptionRequest)

BarAggregationRequest = _reflection.GeneratedProtocolMessageType('BarAggregationRequest', (_message.Message,), dict(
  DESCRIPTOR = _BARAGGREGATIONREQUEST,
  __module__ = 'algotrader.model.market_data_pb2'
  # @@protoc_insertion_point(class_scope:algotrader.model.BarAggregationRequest)
  ))
_sym_db.RegisterMessage(BarAggregationRequest)


# @@protoc_insertion_point(module_scope)
