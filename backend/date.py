from protocols import DateProtocol
import datetime
from datetime import timedelta
import calendar
from typing import Union

class Date(DateProtocol):

    def __init__(self, day: int, month: int, year: int) -> None:
        self.date = datetime.date(year, month, day)
        self.day = day
        self.month = month
        self.year = year
        

    def get_weekday(self) -> int:
        return self.date.weekday()
    
    def get_day(self) -> int:
        # get day of the month of datetime object
        return self.date.day

    def get_month(self) -> int:
        return self.date.month

    def get_year(self) -> int:
        return self.date.year
    
    def get_julian_day(self) -> int:
        import juliandate
        return juliandate.from_gregorian(self.date.year, self.date.month, self.date.day)

    def is_leap_year(self) -> bool:
        return calendar.isleap(self.date.year)

    def is_bus_day(self, calendar_input) -> bool:
        from calendar import Calendar
        return calendar_input.is_bus_day(self)

    def __repr__(self) -> str:
        return f"Date(day={self.date.day}, month={self.date.month}, year={self.date.year})"

    def __str__(self) -> str:
        return f"{self.date.day}/{self.date.month}/{self.date.year}"

    def __hash__(self) -> int:
        return hash(str(self.date.day) + str(self.date.month) + str(self.date.year))

    def __add__(self, other) -> "Date":
        from dateutil.relativedelta import relativedelta
        from term import Term, Frequency
        from calendarclass import Calendar
        if isinstance(other, int):
            delta = other
            new_date = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=delta)
            return Date(new_date.day, new_date.month, new_date.year)
        elif isinstance(other, Frequency):
            delta = other.numerical
            new_date = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=delta)
            return Date(new_date.day, new_date.month, new_date.year)
        elif isinstance(other, Term):
            delta = other.quantity
            if other.unit.name == "week":
                delta = delta * 7
                new_date = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=delta)
                return Date(new_date.day, new_date.month, new_date.year)
            elif other.unit.name == "month":
                try:
                    new_date = datetime.date(self.year, self.month, self.day) + relativedelta(months=other.quantity)
                    return Date(new_date.day, new_date.month, new_date.year)
                except ValueError:
                    delta = Calendar.monthrange(self.year, self.month)[1]
                    new_date = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=delta)
                    return Date(new_date.day, new_date.month, new_date.year)
            elif other.unit.name == "year":
                new_date = datetime.date(self.year, self.month, self.day) + relativedelta(years=other.quantity)
                return Date(new_date.day, new_date.month, new_date.year)
        else:
            raise TypeError(f"Cannot add {type(other)} to {type(self)}")
        
    def __sub__(self, other) -> "Date":
        from dateutil.relativedelta import relativedelta
        from term import Term, Frequency
        from calendar import Calendar
        from dateutil.relativedelta import relativedelta
        if isinstance(other, int):
            delta = other
            new_date = datetime.date(self.year, self.month, self.day) - datetime.timedelta(days=delta)
            return Date(new_date.day, new_date.month, new_date.year)
        elif isinstance(other, Frequency):
            delta = other.numerical
            new_date = datetime.date(self.year, self.month, self.day) - datetime.timedelta(days=delta)
            return Date(new_date.day, new_date.month, new_date.year)
        elif isinstance(other, Term):
            delta = other.quantity
            if other.unit.name == "week":
                delta = delta * 7
                new_date = datetime.date(self.year, self.month, self.day) - datetime.timedelta(days=delta)
                return Date(new_date.day, new_date.month, new_date.year)
            elif other.unit.name == "month":
                try:
                    new_date = datetime.date(self.year, self.month, self.day) - relativedelta(months=other.quantity)
                    return Date(new_date.day, new_date.month, new_date.year)
                except ValueError:
                    delta = Calendar.monthrange(self.year, self.month)[1]
                    new_date = datetime.date(self.year, self.month, self.day) - datetime.timedelta(days=delta)
                    return Date(new_date.day, new_date.month, new_date.year)
            elif other.unit.name == "year":
                new_date = datetime.date(self.year, self.month, self.day) - relativedelta(years=other.quantity)
                return Date(new_date.day, new_date.month, new_date.year)
        else:
            raise TypeError(f"Cannot add {type(other)} to {type(self)}")


    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) == (other.year, other.month, other.day)
        return False

    def __gt__(self, other: "Date") -> bool:
        return self.date > other.date

    def __ge__(self, other: "Date") -> bool:
        return self.date >= other.date

    def __lt__(self, other: "Date") -> bool:
        return self.date < other.date

    def __le__(self, other: "Date") -> bool:
        return  self.date <= other.date