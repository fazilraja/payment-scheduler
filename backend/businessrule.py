from protocols import BusinessDayRuleProtocol
from date import Date
from calendar import Calendar

class BusinessDayRule(BusinessDayRuleProtocol):
    
    def __init__(self, current_Date: Date) -> None:
        self.current_Date = current_Date

    
    def get_next_business_day(self, calendar: 'Calendar') -> Date:

        next_day = self.current_Date + 1
        while not calendar.is_bus_day(date_input=next_day, ignore_holidays=False, ignore_weekend=False):
            next_day = next_day + 1
        return next_day
    
    def get_prev_business_day(self, calendar: 'Calendar') -> Date:

        prev_day = self.current_Date.__sub__(1)
        while not calendar.is_bus_day(date_input=prev_day, ignore_holidays=False, ignore_weekend=False):
            prev_day = prev_day.__sub__(1)
        return prev_day
    
    def modi_business_day(self, calendar: 'Calendar') -> Date:

        next_day_buss = self.current_Date
        end_of_month = calendar.get_last_date_in_month(next_day_buss)
        if next_day_buss != end_of_month:
            next_day_buss = Date(next_day_buss.day.__add__(1), next_day_buss.month, next_day_buss.year)
        while not calendar.is_bus_day(date_input=next_day_buss, ignore_holidays=False, ignore_weekend=False):
            if next_day_buss == end_of_month:
                while not calendar.is_bus_day(date_input=next_day_buss, ignore_holidays=False, ignore_weekend=False):
                    next_day_buss = Date(next_day_buss.day.__sub__(1), next_day_buss.month, next_day_buss.year)
                break
            next_day_buss = Date(next_day_buss.day.__add__(1), next_day_buss.month, next_day_buss.year)
        return next_day_buss
    
    def modi_prec_business_day(self, calendar: 'Calendar') -> Date:

        prev_day_buss = self.current_Date

        if prev_day_buss.day == 1:
            # If the given date is the first day of the month and it's not a business day,
            # return the next business day in the same month.
            while not calendar.is_bus_day(date_input=prev_day_buss, ignore_holidays=False, ignore_weekend=False):
                prev_day_buss = Date(prev_day_buss.day.__add__(1), prev_day_buss.month, prev_day_buss.year)
        else:
            # Find the previous business day, skipping holidays and weekends, without going to the previous month.
            prev_day_buss = Date(prev_day_buss.day.__sub__(1), prev_day_buss.month, prev_day_buss.year)
            while not calendar.is_bus_day(date_input=prev_day_buss, ignore_holidays=False, ignore_weekend=False):
                if prev_day_buss.day == 1:                
                # If the previous business day is the first day of the month and it's not a business day,
                # find the next business day in the same month.
                    while not calendar.is_bus_day(date_input=prev_day_buss, ignore_holidays=False, ignore_weekend=False):
                        prev_day_buss = Date(prev_day_buss.day.__add__(1), prev_day_buss.month, prev_day_buss.year)
                    break
                prev_day_buss = Date(prev_day_buss.day.__sub__(1), prev_day_buss.month, prev_day_buss.year)

                if prev_day_buss.day < 1:
                    prev_month = prev_day_buss.month - 1 if prev_day_buss.month > 1 else 12
                    prev_year = prev_day_buss.year if prev_day_buss.month > 1 else prev_day_buss.year - 1
                    last_day_prev_month = calendar.get_last_date_in_month(Date(1, prev_month, prev_year)).day
                    prev_days_buss = Date(last_day_prev_month, prev_month, prev_year)


        return prev_day_buss