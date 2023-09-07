from typing import Dict, Iterable, Optional, Protocol, Tuple, Union, runtime_checkable
import datetime, calendar
from datetime import timedelta

@runtime_checkable
class DateProtocol(Protocol):
    """Protocol of Financial Date Class"""

    def get_day(self) -> int:
        pass

    def get_month(self) -> int:
        pass

    def get_year(self) -> int:
        pass

    def get_julian_day(self) -> int:
        pass

    def is_leap_year(self) -> bool:
        pass

    def is_bus_day(self, calendar_input: "CalendarProtocol") -> bool:
        pass

    def __repr__(self) -> str:
        pass

    # human readable function
    def __str__(self) -> str:
        pass

    # hash a number to create a dictionary
    def __hash__(self) -> int:
        pass

    # add something to date
    def __add__(self, other: Union[int, "FrequencyProtocol", "TermProtocol"]) -> "DateProtocol":
        pass

    def __sub__(self, other: Union[int, "FrequencyProtocol", "TermProtocol"]) -> "DateProtocol":
        pass

    def __eq__(self, other: "DateProtocol") -> bool:
        pass

    def __gt__(self, other: "DateProtocol") -> bool:
        pass

    def __ge__(self, other: "DateProtocol") -> bool:
        pass

    def __lt__(self, other: "DateProtocol") -> bool:
        pass

    def __le__(self, other: "DateProtocol") -> bool:
        pass
    
@runtime_checkable
class BusinessDayRuleProtocol(Protocol):
    """Protocol of Business Day Rule Representation"""

    # This is the protocol class 
    def get_next_business_day(self, calendar: 'CalendarProtocol') -> DateProtocol:
        pass
    # This is the protocol class
    def get_prev_business_day(self, calendar: 'CalendarProtocol') -> DateProtocol:
        pass
    # This is the protocol class
    def modi_business_day(self, calendar: 'CalendarProtocol')-> DateProtocol:
        pass
    # This is the protocol class
    def modi_prec_business_day(self, calendar: 'CalendarProtocol') -> DateProtocol:
        pass

@runtime_checkable
class EndofMonthRuleProtocol(Protocol):
    """Protocol of EndoofMonthRule Representation"""    

    def apply(self, d: DateProtocol, freq: "FrequencyProtocol") -> DateProtocol:
        pass
    
    # def add(self, other: Union[int, "Frequency", "Term"]) -> "Date":
    #     pass

@runtime_checkable
class FrequencyProtocol(Protocol):
    """Protocol of Frequency Representation"""

    name: str
    term: "TermProtocol"
    numerical: float

    @property
    def year_fraction(self) -> float:
        pass

    def __str__(self) -> str:
        pass

class CalendarProtocol(Protocol):
    """Protocol of Financial Calendar class"""


    def __eq__(self, other: "CalendarProtocol") -> bool:
        return str(self) == str(other)

    def __str__(self) -> str:
        pass

    def add_holiday(self, date_input: DateProtocol):
        pass

    def add_holidays(self, dates_input: Iterable[DateProtocol]):
        pass

    def is_weekend(self, date_input: DateProtocol) -> bool:
        pass

    def is_holiday(self, date_input: DateProtocol) -> bool:
        pass

    def is_bus_day(self, date_input: DateProtocol, ignore_weekend: bool, ignore_holidays: bool) -> bool:
        pass

    def is_leap_year(self, year: int) -> bool:
        pass

    def bus_to_cal_day(
            self,
            date_input: DateProtocol,
            term_input: "TermProtocol",
            business_day_rule: BusinessDayRuleProtocol,
            ignore_weekend: bool,
            ignore_holidays: bool,
    ) -> "TermProtocol":
        pass

    def business_days_between(
            self,
            start_date: DateProtocol,
            end_date: DateProtocol,
            ignore_weekend: bool,
            ignore_holidays: bool,
    ) -> int:
        pass

class TermUnitProtocol(Protocol):
    """Protocol of Term Unit Representation"""

    name: str
    code: str

    def __str__(self) -> str:
        pass

@runtime_checkable
class TermProtocol(Protocol):
    """Financial Term Class"""

    #gets paid every 7 weeks
    quantity: int #7
    unit: TermUnitProtocol #week

    CODE_TO_TERM_MAP: Dict[str, TermUnitProtocol]

    def __init__(
            self, quantity: int, unit: Union[TermUnitProtocol, str], lenient: bool = False
    ) -> None:
        pass

    @classmethod
    def from_str(cls, string: str, lenient: bool = False) -> "TermProtocol":
        pass

    def __str__(self) -> str:
        pass

    def __float__(self) -> float:
        pass

    def __repr__(self) -> str:
        pass

    def __hash__(self) -> int:
        pass

    def __add__(self, other: "TermProtocol") -> "TermProtocol":
        pass

    def __sub__(self, other: "TermProtocol") -> "TermProtocol":
        pass

    def __mul__(self, other: int) -> "TermProtocol":
        pass

    def __floordiv__(self, other: int) -> "TermProtocol":
        pass

    def __mod__(self, other: int) -> "TermProtocol":
        pass

    def __truediv__(self, other: int) -> "TermProtocol":
        pass

    def __eq__(self, other: "TermProtocol") -> bool:
        pass

    def __gt__(self, other: "TermProtocol") -> bool:
        pass

    def __ge__(self, other: "TermProtocol") -> bool:
        pass

    def __lt__(self, other: "TermProtocol") -> bool:
        pass

    def __le__(self, other: "TermProtocol") -> bool:
        pass

    def change_unit(
            self, new_unit: Union[TermUnitProtocol, str], lenient: bool = False
    ) -> None:
        pass

    def change_unit_copy(self, new_unit: Union[TermUnitProtocol, str], lenient: bool) -> "TermProtocol":
        pass
    
if __name__ == "__main__":
    pass
    # # create a calendar for the United States
    # us_holidays = [
    # Date(1, 1, 2023), # New Year's Day
    # Date(16, 1, 2023), # Martin Luther King Jr. Day
    # Date(20, 2, 2023), # Presidents' Day
    # Date(29, 5, 2023), # Memorial Day
    # Date(4, 7, 2023), # Independence Day
    # Date(4, 9, 2023), # Labor Day
    # Date(9, 10, 2023), # Columbus Day
    # Date(11, 11, 2023), # Veterans Day
    # Date(23, 11, 2023), # Thanksgiving Day
    # Date(25, 12, 2023) # Christmas Day
    # ]

    # # mycalendar = calendar.calendar(2023)
    #print(mycalendar)
    # us_weekend = [5, 6]
    # date = Date(1, 1, 2023)
    # us_calendar = Calendar("US", us_weekend, us_holidays)

    # d1=Date(6,10,2023)
    # date=BusinessDayRule(d1)
    # next_bus_day=date.get_next_business_day(us_calendar)
    # cor_bus=Date(10,10,2023)
    # print(next_bus_day)
    # print(next_bus_day==cor_bus)
    # mycalendar = calendar.calendar(2023)
    # print(mycalendar)
    # us_weekend = [5, 6]
    # date = Date(1, 1, 2023)
    # us_calendar = Calendar("US", us_weekend, us_holidays)
    # print(us_calendar.is_weekend(date))
    # print(date.get_day())
    # print(date.get_month())
    # print(date.get_year())
    # print(us_calendar.get_last_date_in_month(date))

    # d1 = Date(1, 1, 2023)
    # d2 = Date(1, 1, 2023)
    # print(d1 == d2)

    # print(us_calendar.get_last_date_in_month(d1))

    # print(us_calendar.monthrange(2023, 2))
    # # create a calendar for Australia
    # aus_holidays = [
    # Date(1, 1, 2023), # New Year's Day
    # Date(26, 1, 2023), # Australia Day
    # Date(15, 4, 2023), # Good Friday
    # Date(18, 4, 2023), # Easter Monday
    # Date(25, 4, 2023), # Anzac Day
    # Date(25, 12, 2023), # Christmas Day
    # Date(26, 12, 2023) # Boxing Day
    # ]

    # aus_weekend = [5, 6]

    # aus_calendar = Calendar("AUS", aus_weekend, aus_holidays)

    # # create calendar for Brazil
    # brazil_holidays = [
    # Date(1, 1, 2023), # New Year's Day
    # Date(25, 2, 2023), # Carnaval
    # Date(21, 4, 2023), # Tiradentes' Day
    # Date(1, 5, 2023), # Labor Day
    # Date(7, 9, 2023), # Independence Day
    # Date(12, 10, 2023), # Nossa Senhora Aparecida Day
    # Date(2, 11, 2023), # All Souls' Day
    # Date(15, 11, 2023), # Proclamation of the Republic Day
    # Date(25, 12, 2023) # Christmas Day
    # ]

    # brazil_weekend = [5, 6]
    
    # brazil_calendar = Calendar("BRAZIL", brazil_weekend, brazil_holidays)

    # # create calendar for Germany
    # germany_holidays = [
    # Date(1, 1, 2023), # New Year's Day
    # Date(14, 4, 2023), # Good Friday
    # Date(17, 4, 2023), # Easter Monday
    # Date(1, 5, 2023), # Labor Day
    # Date(25, 12, 2023), # Christmas Day
    # Date(26, 12, 2023) # Boxing Day
    # ]

    # germany_weekend = [5, 6]

    # germany_calendar = Calendar("GERMANY", germany_weekend, germany_holidays)

    # # create calendar for India
    # india_holidays = [
    # Date(1, 1, 2023), # New Year's Day
    # Date(26, 1, 2023), # Republic Day
    # Date(2, 3, 2023), # Holi
    # Date(14, 4, 2023), # Good Friday
    # Date(15, 8, 2023), # Independence Day
    # Date(2, 10, 2023), # Gandhi
    # ]

    # india_weekend = [5, 6]

    # india_calendar = Calendar("INDIA", india_weekend, india_holidays)

    # # create calendar for South Africa
    # sa_holidays = [
    # Date(1, 1, 2023),  # New Year's Day
    # Date(21, 3, 2023),  # Human Rights Day
    # Date(14, 4, 2023),  # Good Friday
    # Date(17, 4, 2023),  # Family Day
    # Date(27, 4, 2023),  # Freedom Day
    # Date(1, 5, 2023),  # Workers' Day
    # Date(16, 6, 2023),  # Youth Day
    # Date(9, 8, 2023),  # National Women's Day
    # Date(24, 9, 2023),  # Heritage Day
    # Date(16, 12, 2023),  # Day of Reconciliation
    # Date(25, 12, 2023),  # Christmas Day
    # Date(26, 12, 2023),  # Day of Goodwill
    # ]

    # sa_weekend = [5, 6]

    # sa_calendar = Calendar("SA", sa_weekend, sa_holidays)

    # weekends = [6, 7]
    # calendar1 = Calendar(weekends, [date])
    # calendar2 = Calendar(weekends, [date])
    # print(calendar2 == calendar1)