from protocols import EndofMonthRuleProtocol
from calendarclass import Calendar
import calendar
from date import Date
from datetime import timedelta
class EndOfMonthRule(EndofMonthRuleProtocol):

    def __init__(self, calendar: "Calendar", active=True):
        self.active = active
        self.calendar = calendar

    def apply(self, d, freq):
        from date import Date
        unit = freq.term.unit.code
        quantity = freq.term.quantity
        
        # if not self.active and unit in {'d', 'w'} and quantity < 30:
        # Add the frequency to the date based on the unit
        # d = self._add_frequency(d, unit, quantity)
        # return Date(day=d.day, month=d.month, year=d.year)


        if unit == 'd':
    
            d = self._add_frequency(d, unit, quantity)
            end_of_month = self.calendar.get_last_date_in_month(Date(day=d.day, month=d.month, year=d.year))
            d = Date(day=d.day, month=d.month, year=d.year)  # Convert datetime.date to Date object

            if not self.active and quantity < 30:
                return d
            elif self.active and quantity < 30:
                return d
            elif not self.active and quantity >= 30:
                return d
            else:
                return end_of_month
            
        if unit == 'w':
            d = self._add_frequency(d, unit, quantity)
            end_of_month = self.calendar.get_last_date_in_month(Date(day=d.day, month=d.month, year=d.year))
            d = Date(day=d.day, month=d.month, year=d.year)  # Convert datetime.date to Date object

            if not self.active and quantity < 5:
                return d
            elif self.active and quantity < 5:
                return d
            elif not self.active and quantity >5:
                return d
            else:
                return end_of_month


        if unit == 'm':
            num = freq.term.quantity
            month = d.month - 1 + num
            year = d.year + month // 12
            month = month % 12 + 1

            if self.active and self.calendar.get_last_date_in_month(d):
                day = calendar.monthrange(year, month)[1]
            else:
                day = min(d.day, calendar.monthrange(year, month)[1])

            d = Date(day, month, year)
            return Date(day=d.day, month=d.month, year=d.year)

        if unit == 'y':
            d = self._add_frequency(d, unit, quantity)
            if not self.active:
                return Date(day = d.day, month = d.month, year = d.year)
            else:
                end_of_month = self.calendar.get_last_date_in_month(Date(day=d.day, month=d.month, year=d.year))
                return end_of_month

        

    def _add_frequency(self, d: "Date", unit, quantity):
        d = Date(d.day, d.month, d.year)
        if unit == 'd':
            d = d.date + timedelta(days=quantity)
        elif unit == 'w':
            d = d.date + timedelta(weeks=quantity)
        elif unit == 'm':
            month = d.month - 1 + quantity
            year = d.year + month // 12
            month = month % 12 + 1
            day = min(d.day, calendar.monthrange(year, month)[1])
            d = Date(day, month, year)
        elif unit == 'y':
            d = Date(d.day, d.month, d.year + quantity)
        else:
            raise ValueError(f"Unsupported frequency unit: {unit}")
        return d