from protocols import CalendarProtocol
from date import Date
import calendar
import datetime
class Calendar(CalendarProtocol):

    # Monday = 0, Sunday = 6 for weekend input
    def __init__(self, name: str, weekend: list[int], holidays: list[Date]) -> None:
        self.name = name
        self.weekend = weekend
        self.holidays = holidays
    

    # given the year and month return the first integer of the month and the number of days in the month
    def monthrange(self, year: int, month: int) -> tuple[int, int]:
        # create date of first day of month
        date_input = Date(day=1, month=month, year=year)

        #get the weekday of the first day of the month
        weekday = date_input.get_weekday()

        # get the number of days in the month
        num_days = calendar.monthrange(year, month)[1]

        return [weekday, num_days]
    
    # return holidays
    def get_holidays(self) -> list[Date]:
        return self.holidays
    
    # check if two calendars are equal
    def __eq__(self, other: "Calendar"):
        if set(self.weekend) == set(other.weekend) and set(self.holidays) == set(other.holidays):
            return True
        return False

    # string representation of calendar
    def __str__(self) -> str:
        return "Calendar %s with holidays: %s and weekends: %s" % (self.name, self.holidays, self.weekend)

    # string representation of calendar for debugging
    def __repr__(self):
        return "Calendar(name=%r, weekend=%r, holidays=%r)" % (self.name, self.weekend, self.holidays)

    # add a holiday to the calendar
    def add_holiday(self, date_input: Date):
        self.holidays.append(Date)

    # check if year is leap year
    def is_leap_year(self, year: int) -> bool:
    
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False
    
    # check if a date is a weekend
    def is_weekend(self, date_input: Date) -> bool:
        if date_input.date.weekday() in self.weekend:
            return True
        return False
    
    def get_last_date_in_month(self, date_input: Date) -> int:
        days_in_month = calendar.monthrange(date_input.get_year(), date_input.get_month())[1]
        return_date = Date(days_in_month, date_input.get_month(), date_input.get_year())
        return return_date
    
    # check if a date is a holiday
    def is_holiday(self, date_input: Date) -> bool:
        if date_input in self.holidays:
            return True
        return False
    
    # check if a date is a business day
    def is_bus_day(self, date_input: Date, ignore_weekend: bool, ignore_holidays: bool) -> bool:
        if ignore_weekend and ignore_holidays:
            return True
        elif ignore_weekend:
            return not self.is_holiday(date_input)
        elif ignore_holidays:
            return not self.is_weekend(date_input)
        else:
            return not self.is_weekend(date_input) and not self.is_holiday(date_input)
    
    # convert a business day to a calendar day
    def bus_to_cal_day(
            self,
            date_input: Date,
            term_input,
            business_day_rule,
            ignore_weekend: bool,
            ignore_holidays: bool,
    ):
        if self.is_bus_day(date_input, ignore_weekend, ignore_holidays):
            return date_input
        else:
            if business_day_rule == "forward":
                while not self.is_bus_day(date_input, ignore_weekend, ignore_holidays):
                    date_input += term_input
            elif business_day_rule == "backward":
                while not self.is_bus_day(date_input, ignore_weekend, ignore_holidays):
                    date_input -= term_input
            else:
                raise ValueError(f"Invalid Business Day Rule: {business_day_rule}")
            return date_input
        
    # calculate the number of business days between two dates
    def business_days_between(
            self,
            start_date: Date,
            end_date: Date,
            ignore_weekend: bool,
            ignore_holidays: bool,
    ) -> int:
        from term import Term
        if start_date > end_date:
            raise ValueError("Start date must be before end date")
        else:
            count = 0
            while start_date < end_date:
                if self.is_bus_day(start_date, ignore_weekend, ignore_holidays):
                    count += 1
                start_date += Term(1, "day")
            return count
    
    # convert a business day to a calendar day
    def bus_to_cal_day(
            self,
            date_input: Date,
            term_input,
            business_day_rule,
            ignore_weekend: bool,
            ignore_holidays: bool,
    ):
        if self.is_bus_day(date_input, ignore_weekend, ignore_holidays):
            return date_input
        else:
            if business_day_rule == "forward":
                while not self.is_bus_day(date_input, ignore_weekend, ignore_holidays):
                    date_input += term_input
            elif business_day_rule == "backward":
                while not self.is_bus_day(date_input, ignore_weekend, ignore_holidays):
                    date_input -= term_input
            else:
                raise ValueError(f"Invalid Business Day Rule: {business_day_rule}")
            return date_input
        
    
    # def business_days(self, start: Date, end: Date, freq: str, endOfMonth: bool):
    #     print("start: ", start, "end: ", end, "freq: ", freq, "endOfMonth: ", endOfMonth)
        
    #     if start.__gt__(end):
    #         raise ValueError("Start date must be before end date")
        
    #     if freq == "daily":
    #         increment = 1
    #     elif freq == "weekly":
    #         increment = datetime.timedelta(days=7)

    #     business_days = []

    #     while start.__le__(end):
    #         if us_calendar.is_bus_day(start, ignore_weekend=True, ignore_holidays=True):
    #             business_days.append(start)
    #         start += increment

    #     return business_days