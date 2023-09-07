import holidays
import re
from date import Date
from calendarclass import Calendar
from businessrule import BusinessDayRule
from term import Term, TermUnit

class PaymentSchedule:
    def __init__(self, start_date: str, end_date: str, frequency, calendar_name: str, business_day_rule, eom_rule):
        """
        :param start_date: Given a string in format 'YYYY-MM-DD', create a Date object that is the start date of the schedule
        :param end_date: Given a string in format 'YYYY-MM-DD', create a Date object that is the end date 
        :param frequency: Frequency object Weekly, Biweekly, Monthly, Bimonthly, Quaterly, Semi-Annually, Annually
        :param calendar_name: name of the calendar to create, name must be supported by holidays library: us, aus, brazil, germany, india, sa
        :param business_day_rule: String
        :param eom_rule: Boolean
        """
        startYear, startMonth, startDay = map(int, start_date.split('-'))
        self.start_date = Date(startDay, startMonth, startYear) # Initialize Date object

        endYear, endMonth, endDay = map(int, end_date.split('-'))
        self.end_date = Date(endDay, endMonth, endYear)

        self.frequency = PaymentSchedule.freq_to_term(frequency) # Initialize Frequency object (this will need to be parsed (It can be 1D, 1w or Weekly, Monthly, etc.))
        self.country_holidays = holidays.getCountryHolidays(calendar_name, startYear, endYear) 

        self.calendar = Calendar(calendar_name, [5,6], list(self.country_holidays.keys())) # Create a calendar with no weekends and only the provided holidays
        self.business_day_rule = business_day_rule # String
        self.end_of_month_rule = eom_rule # Boolean
        self.payment_dates = [] # Initialize an empty list of payment dates 

    def generate_payment_dates(self):
        # Create a clone of the start date
        current_date = self.start_date
        while (current_date < self.end_date):
            current_date = current_date + self.frequency # Add frequency to date
            adjusted_date = current_date # Initialize to current date's value (Purpose of this variable is so that we do not directly edit current_date which would invalidate the while loop's condition)
            if (self.end_of_month_rule): # Only way this is active on frontend is if start date is last day of month and Frequency is a multiple of 'Month'
                adjusted_date = self.calendar.get_last_date_in_month(adjusted_date) # Move to last day of month if active

            # if it is not a business day
            holiday_or_weekend = not self.calendar.is_bus_day(adjusted_date, False, False)
                        
            # create a business day rule
            business = BusinessDayRule(adjusted_date)
            
            if (self.business_day_rule == 'No Adjustment' or not holiday_or_weekend):
                # If 'No Adjustment' or not a holiday/weekend, we do not apply a business day rule
                pass
            # The elif cases below imply it IS a holiday/weekend since the if statement above would be executed otherwise            
            elif (self.business_day_rule == 'Following'):
                adjusted_date = business.get_next_business_day(self.calendar)
            elif (self.business_day_rule == 'Preceding'):
                adjusted_date = business.get_prev_business_day(self.calendar)
            elif (self.business_day_rule == 'Modified Following'):
                adjusted_date = business.modi_business_day(self.calendar)
            elif (self.business_day_rule == 'Modified Preceding'):
                adjusted_date = business.modi_prec_business_day(self.calendar)

            if (adjusted_date <= self.end_date): # Make sure the adjusted date is within range of end date
                self.payment_dates.append(adjusted_date)
                
        return self.payment_dates

    def get_holidays(self):
        return self.country_holidays

    def freq_to_term(frequency: str) :
        """
        From the frontend the frequency is given as a string
        :param frequency: String, Weekly, Biweekly, Monthly, Bimonthly, Quarterly, Semi-Annually, Annually, or unique string such as 23d 3w 4m 5y etc
        :return: Term object
        """

        # for unique strings
        pattern = r'^(?P<quantity>\d+)(?P<unit>[dwmyDWMY]$)'

        # for premade 
        if frequency == 'Weekly':
            return Term(1, TermUnit("week", "w"))
        elif frequency == 'Biweekly':
            return Term(2, TermUnit("week", "w"))
        elif frequency == 'Monthly':
            return Term(1, TermUnit("month", "m"))
        elif frequency == 'Bimonthly':
            return Term(2, TermUnit("month", "m"))
        elif frequency == 'Quarterly':
            return Term(3, TermUnit("month", "m"))
        elif frequency == 'Semi-Annually':
            return Term(6, TermUnit("month", "m"))
        elif frequency == 'Annually':
            return Term(1, TermUnit("year", "y"))
        
        # # create regex for unique strings
        elif re.fullmatch(pattern, frequency):

            match = re.fullmatch(pattern, frequency)
            quantity = int(match.group('quantity'))
            unit = match.group('unit')
            # make unit lowercase
            unit = unit.lower()

            # for days we just return quantity as we are adding integers for it, no need for term object
            if unit == 'd':
                return quantity
            elif unit == 'w':
                return Term(quantity, TermUnit("week", "w"))
            elif unit == 'm':
                return Term(quantity, TermUnit("month", "m"))
            elif unit == 'y':
                return Term(quantity, TermUnit("year", "y"))
        else:
            raise ValueError('Frequency not supported')

if __name__ == '__main__':
    start_date = "2023-1-2"
    # end_date = "2023-2-1"
    # frequency = "7D"
    # country = "United States"
    # business_day_rule = "Following"
    # us_holidays = [
    #         Date(1, 1, 2023), # New Year's Day
    #         Date(16, 1, 2023), # Martin Luther King Jr. Day
    #         Date(20, 2, 2023), # Presidents' Day
    #         Date(29, 5, 2023), # Memorial Day
    #         Date(4, 7, 2023), # Independence Day
    #         Date(4, 9, 2023), # Labor Day
    #         Date(9, 10, 2023), # Columbus Day
    #         Date(11, 11, 2023), # Veterans Day
    #         Date(23, 11, 2023), # Thanksgiving Day
    #         Date(25, 12, 2023) # Christmas Day
    #         ]
    # calendar_test = Calendar("United States", [5,6], us_holidays)
    # eom_rule = False
    # c = PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
    # print(c.generate_payment_dates())