import unittest
import payment
from date import Date
from calendarclass import Calendar
from term import Term, TermUnit

us_holidays = [
            Date(1, 1, 2023), # New Year's Day
            Date(16, 1, 2023), # Martin Luther King Jr. Day
            Date(20, 2, 2023), # Presidents' Day
            Date(29, 5, 2023), # Memorial Day
            Date(4, 7, 2023), # Independence Day
            Date(4, 9, 2023), # Labor Day
            Date(9, 10, 2023), # Columbus Day
            Date(11, 11, 2023), # Veterans Day
            Date(23, 11, 2023), # Thanksgiving Day
            Date(25, 12, 2023) # Christmas Day
            ]

class TestPaymentSchedule(unittest.TestCase):
    def test_init(self):
        start_date = "2023-1-2"
        end_date = "2023-2-1"
        frequency = "Weekly"
        country = "United States"
        business_day_rule = "Following"
        calendar_test = Calendar("United States", [5,6], us_holidays)
        eom_rule = False
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        self.assertEqual(c.start_date, Date(2, 1, 2023))
        self.assertEqual(c.end_date, Date(1, 2, 2023))
        self.assertEqual(c.frequency, Term(1, TermUnit("week", "w")))
        self.assertEqual(c.calendar, calendar_test)
        self.assertEqual(c.end_of_month_rule, False)
        self.assertEqual(c.business_day_rule, "Following")
        self.assertEqual(c.payment_dates, [])

    def test_generate_weekly_following(self):
        list_weekly = [Date(9, 1, 2023), Date(17, 1, 2023), Date(23, 1, 2023), Date(30, 1, 2023)]
        start_date = "2023-1-2"
        end_date = "2023-2-1"
        frequency = "Weekly"
        country = "United States"
        business_day_rule = "Following"
        eom_rule = False
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        payment_dates = c.generate_payment_dates()
        self.assertEqual(payment_dates, list_weekly)
    
    def test_generate_biweekly_following(self):
        start_date = "2023-1-2"
        end_date = "2023-2-1"
        frequency = "Biweekly"
        country = "United States"
        business_day_rule = "Following"
        eom_rule = False
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        payment_dates = c.generate_payment_dates()
        self.assertEqual(payment_dates, [Date(17, 1, 2023), Date(30, 1, 2023)])

    def test_generate_monthly_following(self):
        start_date = "2023-1-2"
        end_date = "2023-4-1"
        frequency = "Monthly"
        country = "United States"
        business_day_rule = "Following"
        eom_rule = False
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        payment_dates = c.generate_payment_dates()
        self.assertEqual(payment_dates, [Date(2, 2, 2023), Date(2, 3, 2023)])

    def test_generate_monthly_following_eom(self):
        start_date = "2023-1-2"
        end_date = "2023-4-1"
        frequency = "Monthly"
        country = "United States"
        business_day_rule = "Following"
        eom_rule = True
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        payment_dates = c.generate_payment_dates()
        self.assertEqual(payment_dates, [Date(28, 2, 2023), Date(31, 3, 2023)])

    def test_generate_weekly_preceding(self):
        start_date = "2023-1-2"
        end_date = "2023-2-1"
        frequency = "Weekly"
        country = "United States"
        business_day_rule = "Preceding"
        eom_rule = False
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        payment_dates = c.generate_payment_dates()
        self.assertEqual(payment_dates, [Date(day=9, month=1, year=2023), Date(day=13, month=1, year=2023), Date(day=23, month=1, year=2023), Date(day=30, month=1, year=2023)])

    def test_generate_monthly_preceding(self):
        start_date = "2023-1-2"
        end_date = "2023-4-1"
        frequency = "Monthly"
        country = "United States"
        business_day_rule = "Preceding"
        eom_rule = False
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        payment_dates = c.generate_payment_dates()
        self.assertEqual(payment_dates, [Date(day=2, month=2, year=2023), Date(day=2, month=3, year=2023), Date(day=31, month=3, year=2023)])

    def test_unique_freq_uppercase(self):
        start_date = "2023-1-2"
        end_date = "2023-2-1"
        frequency = "7D"
        country = "United States"
        business_day_rule = "Following"
        eom_rule = False
        c = payment.PaymentSchedule(start_date, end_date, frequency, country, business_day_rule, eom_rule)
        payment_dates = c.generate_payment_dates()
        self.assertEqual(payment_dates, [Date(9, 1, 2023), Date(17, 1, 2023), Date(23, 1, 2023), Date(30, 1, 2023)])


if __name__ == '__main__':
    unittest.main()