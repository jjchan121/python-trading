from typing import Dict, List,Callable, Union

from algotrader.model.market_data_pb2 import *
from algotrader.model.protobuf_to_dict import *
from algotrader.model.ref_data_pb2 import *
from algotrader.model.ref_data_pb2 import *
from algotrader.model.time_series_pb2 import *


class RefDataModelFactory(object):
    def __add_to_dict(self, attribute: Callable, dict: Dict[str, str]):
        if dict:
            for key, value in dict.items():
                attribute[key] = value

    def __add_to_list(self, attribute: Callable, list_item: Union[list, tuple, int, str, bool, float, int]):
        if list_item:
            if not isinstance(list_item, (list, tuple)):
                list_item = [list_item]

            for item in list_item:
                if isinstance(item, (int, str, bool, float)):
                    attribute.append(item)
                elif item is dict:
                    attribute.add(**item)
                else:
                    attribute.add(**protobuf_to_dict(item))


                    ### ref data

    def build_instrument(self, symbol: str, type: int, primary_exch_id: str, ccy_id: str,
                         name: str = None, exch_ids: List[str] = None, sector: str = None, industry: str = None,
                         margin: float = None, tick_size: float = None,
                         underlying: Underlying = None, derivative: DrivativeTraits = None,
                         alt_symbols: Dict[str, str] = None, alt_ids: Dict[str, str] = None,
                         alt_sectors: Dict[str, str] = None, alt_industries: Dict[str, str] = None) -> Instrument:
        inst = Instrument()
        # inst.inst_id = 10
        inst.inst_id = symbol + '@' + primary_exch_id
        inst.symbol = symbol
        inst.name = name
        inst.type = type
        inst.primary_exch_id = primary_exch_id
        self.__add_to_list(inst.exch_ids, exch_ids)
        inst.ccy_id = ccy_id

        inst.sector = sector
        inst.industry = industry
        inst.margin = margin
        inst.tick_size = tick_size
        if underlying:
            inst.underlying.CopyFrom(underlying)
        if derivative:
            inst.derivative.CopyFrom(derivative)
        self.__add_to_dict(inst.alt_symbols, alt_symbols)
        self.__add_to_dict(inst.alt_ids, alt_ids)
        self.__add_to_dict(inst.alt_sectors, alt_sectors)
        self.__add_to_dict(inst.alt_industries, alt_industries)

        return inst

    def build_derivative_traits(self, option_type: int = None, option_style: int = None, strike: float = None,
                                exp_date: int = None,
                                multiplier: float = None) -> DrivativeTraits:
        deriv = DrivativeTraits()
        deriv.option_type = option_type
        deriv.option_style = option_style
        deriv.strike = strike
        deriv.exp_date = exp_date
        deriv.multiplier = multiplier

        return deriv

    def build_underlying(self, type: int, assets: List[Underlying.Asset]) -> Underlying:
        underlying = Underlying()
        underlying.type = type
        self.__add_to_list(underlying.assets, assets)

        return underlying

    def build_asset(self, inst_id: str, weight: float) -> Underlying.Asset:
        asset = Underlying.Asset()
        asset.inst_id = inst_id
        asset.weight = weight

        return asset

    def build_exchange(self, exch_id: str, name: str, country_id: str = None, trading_hours_id: str = None,
                       holidays_id: str = None,
                       alt_ids: Dict[str, str] = None) -> Exchange:
        exchange = Exchange()
        exchange.exch_id = exch_id
        exchange.name = name
        exchange.country_id = country_id
        exchange.trading_hours_id = trading_hours_id
        exchange.holidays_id = holidays_id
        self.__add_to_dict(exchange.alt_ids, alt_ids)
        return exchange

    def build_currency(self, ccy_id: str, name: str) -> Currency:
        currency = Currency()
        currency.ccy_id = ccy_id
        currency.name = name
        return currency

    def build_country(self, country_id: str, name: str, holidays_id: str = None) -> Country:
        country = Country()
        country.country_id = country_id
        country.name = name
        country.holidays_id = holidays_id
        return country

    def build_trading_holidays(self, holidays_id, holidays) -> HolidaySeries:
        holiday_series = HolidaySeries()
        holiday_series.holidays_id = holidays_id
        self.__add_to_list(holiday_series.holidays, holidays)
        return holiday_series

    def build_holiday(self, trading_date: int, type: int, start_date: int, end_date: int, start_time: int = None,
                      end_time: int = None,
                      desc: str = None) -> HolidaySeries.Holiday:
        holiday = HolidaySeries.Holiday()
        holiday.trading_date = trading_date
        holiday.type = type
        holiday.start_date = start_date
        holiday.end_date = end_date

        if start_time:
            holiday.start_time = start_time
        if end_time:
            holiday.end_time = end_time

        if desc:
            holiday.desc = desc
        return holiday

    def build_trading_hours(self, trading_hours_id: str, timezone_id: str,
                            sessions: TradingHours.Session) -> TradingHours:
        trading_hour = TradingHours()
        trading_hour.trading_hours_id = trading_hours_id
        trading_hour.timezone_id = timezone_id
        self.__add_to_list(trading_hour.sessions, sessions)
        return trading_hour

    def build_trading_session(self, start_weekdate: int, start_time: int, end_weekdate: int, end_time: int,
                              eod: bool) -> TradingHours.Session:
        session = TradingHours.Session()
        session.start_weekdate = start_weekdate
        session.start_time = start_time
        session.end_weekdate = end_weekdate
        session.end_time = end_time
        session.eod = eod

        return session

    def build_timezone(self, timezone_id: str) -> TimeZone:
        timezone = TimeZone()
        timezone.timezone_id = timezone_id
        return timezone
