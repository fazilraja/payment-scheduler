import unittest
from date import Date
from calendarclass import Calendar
from term import Term, Frequency, TermUnit
from eom import EndOfMonthRule
from businessrule import BusinessDayRule

class TestDate(unittest.TestCase):

    def setUp(self):
        self.d1 = Date(1, 1, 2022)
        self.d2 = Date(2, 1, 2022)

    def test_init(self):
        self.assertEqual(self.d1.date.day, 1)
        self.assertEqual(self.d1.date.day, 1)
        self.assertEqual(self.d1.date.year, 2022)

    def test_get_day(self):
        self.assertEqual(self.d1.get_day(), 1)

    def test_get_month(self):
        self.assertEqual(self.d1.get_month(), 1)

    def test_get_year(self):
        self.assertEqual(self.d1.get_year(), 2022)

    # need to finish julian day
    def test_get_julian_day(self):
        pass

    def test_is_leap_year(self):
        d1 = Date(1, 1, 2020)
        self.assertTrue(d1.is_leap_year())

        self.assertFalse(self.d2.is_leap_year())

    # need to finish Calendar(Protocol)
    def test_is_bus_day(self):
        pass

    def test_repr(self):
        self.assertEqual(repr(self.d1), "Date(day=1, month=1, year=2022)")

    def test_str(self):
        self.assertEqual(str(self.d1), "1/1/2022")

    def test_add_int(self):
        d = Date(1, 1, 2022)
        result = d + 10
        expected = Date(11, 1, 2022)
        self.assertEqual(result, expected)

    def test_sub_int(self):
        d = Date(11, 1, 2022)
        result = d - 10
        expected = Date(1, 1, 2022)
        self.assertEqual(result, expected)

    def test_add_frequency(self):
        d = Date(1, 1, 2022)
        term = Term(1, "WEEK")
        freq = Frequency("D", term, 7)
        result = d + freq
        expected = Date(8, 1, 2022)
        self.assertEqual(result, expected)

    def test_sub_frequency(self):
        d = Date(8, 1, 2022)
        term = Term(1, "WEEK")
        freq = Frequency("D", term, 7)
        result = d - freq
        expected = Date(1, 1, 2022)
        self.assertEqual(result, expected)

    def test_add_termunit_week(self):
        d = Date(1, 1, 2022)
        term = Term(1, "WEEK")
        result = d + term
        expected = Date(8, 1, 2022)
        self.assertEqual(result, expected)

    def test_add_termunit_month(self):
        #jan 1st + 1 month = feb 1st
        d = Date(1, 1, 2022)
        term = Term(1, "MONTH")
        new_date = d + term
        expected_date = Date(1, 2, 2022)
        self.assertEqual(new_date, expected_date)

    def test_add_termunit_month2(self):
        #jan 31st + 1 month = mar 2nd 
        d = Date(31, 1, 2022)
        term = Term(1, "MONTH")
        new_date = d + term
        expected_date = Date(28, 2, 2022)
        self.assertEqual(new_date, expected_date)

    def test_sub_termunit_week(self):
        d = Date(8, 1, 2022)
        term = Term(1, "WEEK")
        result = d - term
        expected = Date(1, 1, 2022)
        self.assertEqual(result, expected)

    def test_sub_termunit_month(self):
        #feb 1st - 1 month = jan 1st 
        d = Date(1, 2, 2022)
        term = Term(1, "MONTH")
        new_date = d - term
        expected_date = Date(1, 1, 2022)
        self.assertEqual(new_date, expected_date)

    # def test_sub_termunit_month2(self):
    #     #mar 31st - 1 month = march 1  
    #     d = Date(31, 3, 2022)
    #     term = Term(1, "MONTH")
    #     new_date = d - term
    #     expected_date = Date(1, 3, 2022)
    #     self.assertEqual(new_date, expected_date)

    def test_sub_term_unit_year(self):
        d = Date(1, 1, 2024)
        term = Term(2, "YEAR")
        new_date = d - term
        expected_date = Date(1, 1, 2022)
        self.assertEqual(new_date, expected_date)

    def test_eq(self):
        d3 = Date(1, 1, 2022)
        self.assertFalse(self.d1 == self.d2)
        self.assertTrue(self.d1 == d3)

    def test_gt(self):
        self.assertFalse(self.d1.__gt__(self.d2))
        self.assertTrue(self.d2.__gt__(self.d1))

    def test_ge(self):
        self.assertFalse(self.d1.__ge__(self.d2))
        self.assertTrue(self.d2.__ge__(self.d1))
        self.assertTrue(self.d1.__ge__(self.d1))

    def test_lt(self):
        self.assertTrue(self.d1.__lt__(self.d2))
        self.assertFalse(self.d2.__lt__(self.d1))

    def test_le(self):
        self.assertTrue(self.d1.__le__(self.d2))
        self.assertFalse(self.d2.__le__(self.d1))
        self.assertTrue(self.d1.__le__(self.d1))

class TestBusinessDayRule(unittest.TestCase):

    def setUp(self):
        # Create a calendar for testing with specific holidays and weekends
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
            Date(3, 4, 2023), # test date for [def test_get_Prec_Bus(self)]
            Date(28, 4, 2023), # test date for [def test_get_Mod_Foll_Bus(self)] 
            Date(25, 12, 2023) # Christmas Day
        ]
        us_weekend = [5, 6]
        self.us_calendar = Calendar("US", us_weekend, us_holidays)

    def test_init(self):
        d1=Date(1,1,2023)
        date=BusinessDayRule(d1)
        self.assertEqual(date.current_Date, d1)
        
    ## works
    def test_getFollBus(self):
        d1=Date(3,7,2023)
        date=BusinessDayRule(d1)
        next_bus_day=date.get_next_business_day(self.us_calendar)
        cor_bus=Date(5,7,2023)
        self.assertEqual(next_bus_day, cor_bus)

    ## works!
    def test_getPrevBus(self):
        d1=Date(26,12,2023)
        date=BusinessDayRule(d1)
        next_bus_day=date.get_prev_business_day(self.us_calendar)
        cor_bus=Date(22,12,2023)
        self.assertEqual(next_bus_day, cor_bus)

    ## works!
    def test_get_Mod_Foll_Bus(self):
        d1=Date(28,4,2023)
        date=BusinessDayRule(d1)
        next_bus_day=date.modi_business_day(self.us_calendar)
        cor_bus=Date(27,4,2023)
        self.assertEqual(next_bus_day, cor_bus)
    ## works
    def test_get_Prec_Bus(self):
        d1=Date(3,4,2023)
        date=BusinessDayRule(d1)
        next_bus_day=date.modi_prec_business_day(self.us_calendar)
        cor_bus=Date(4,4,2023)
        self.assertEqual(next_bus_day, cor_bus)

class TestEndofMonthRule(unittest.TestCase):

    def setUp(self):
        # Create a calendar for testing with specific holidays and weekends
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
            Date(14, 4, 2023), # test date
            Date(13, 4, 2023), # test date
            Date(25, 12, 2023) # Christmas Day
        ]
        us_weekend = [5, 6]
        self.us_calendar = Calendar("US", us_weekend, us_holidays)
        
    def test_apply(self):

        ## custom day term: 30 or 30+ -> will return last day of the current month after incrementing days
        ## for example, if given date is: 31 Jan, adding 30 days will give me March 2
        ## it will return 31 March, 2023 when EOM_RULE is "ACTIVE", otherwise, it will give March 2, 2023
        d1 = Date(31, 1, 2023)
        rule = EndOfMonthRule(self.us_calendar, active=True)

        term = Term(quantity=30, unit="DAY")
        freq = Frequency(name="Daily", term=term, numerical=1)

        d1_corr = rule.apply(d1, freq)
        corr_nextMonthDate = Date(31, 3, 2023)
        self.assertEqual(d1_corr, corr_nextMonthDate)
    
        ## DAY TERM WORKS!
        d2 = Date(31, 1, 2023)
        rule = EndOfMonthRule(self.us_calendar, active=True)

        term = Term(quantity=28, unit="DAY")
        freq = Frequency(name="Daily", term=term, numerical=1)

        d2_corr = rule.apply(d2, freq)
        corr_nextMonthDate = Date(28, 2, 2023)
        self.assertEqual(d2_corr, corr_nextMonthDate)

        ## WEEK TERM WORKS!
        d3 = Date(17, 4, 2023)
        rule = EndOfMonthRule(self.us_calendar, active=True)

        term = Term(quantity=5, unit="WEEK")
        freq = Frequency(name="Weekly", term=term, numerical=1)

        d3_corr = rule.apply(d3, freq)
        corr_nextMonthDate = Date(31, 5, 2023)
        self.assertEqual(d3_corr, corr_nextMonthDate)

        ## MONTH TERM WORKS!
        d4 = Date(30, 1, 2023)
        rule = EndOfMonthRule(self.us_calendar, active=True)

        term = Term(quantity=2, unit="MONTH")
        freq = Frequency(name="Monthly", term=term, numerical=1)

        d4_corr = rule.apply(d4, freq)
        corr_nextMonthDate = Date(31, 3, 2023)
        self.assertEqual(d4_corr, corr_nextMonthDate)

        ## YEAR
        d5 = Date(1, 2, 2023)
        rule = EndOfMonthRule(self.us_calendar, active=True)

        term = Term(quantity=5, unit="YEAR")
        freq = Frequency(name="Yearly", term=term, numerical=1)

        d5_corr = rule.apply(d5, freq)
        corr_nextMonthDate = Date(29, 2, 2028)
        self.assertEqual(d5_corr, corr_nextMonthDate)

class TestFrequency(unittest.TestCase):
    def test_init(self):
        freq = Frequency("weekly", 1, 2)

class TestCalendar(unittest.TestCase):
    
        def test_init(self):
            holidays = [Date(12, 3, 2002)]
            weekends = [6, 7]
            name = "test"
            c = Calendar(name, weekends, holidays)
            self.assertEqual(c.weekend, weekends)
            self.assertEqual(c.holidays, holidays)
    
        def test_repr(self):
            holidays = [Date(12, 3, 2002)]
            weekends = [6, 7]
            name = "test"
            c = Calendar(name, weekends, holidays)
            self.assertEqual(repr(c), "Calendar(name=%r, weekend=%r, holidays=%r)" % (name, weekends, holidays))
    
    
        def test_add_holiday(self):
            holidays= [Date(12, 3, 2002)]
            weekends = [6, 7]
            name = "test"
            c = Calendar(name, weekends, holidays)
            c.add_holidays(Date(1, 1, 2022))
            # add Date to holidays
            holidays.append(Date(1, 1, 2022))
            self.assertEqual(c.holidays, holidays)
    
        def test_is_holidays(self):
            holidays = [Date(12, 3, 2002)]
            weekends = [6, 7]
            name = "test"
            c = Calendar(name, weekends, holidays)
            c.add_holidays(Date(1, 1, 2022))
            self.assertTrue(c.is_holiday(Date(12, 3, 2002)))
            self.assertFalse(c.is_holiday(Date(2, 1, 2022)))
    
        def test_is_bus_day(self):
            holidays = [Date(12, 3, 2002)]
            weekends = [6, 7]
            name = "test"
            c = Calendar(name, weekends, holidays)
            c.add_holidays(Date(1, 1, 2022))
            self.assertFalse(c.is_bus_day(holidays[0], False, False))
            self.assertTrue(c.is_bus_day(Date(1, 1, 2022), False, False))

# #class TestTermUnit(unittest.TestCase):

# #class TestTerm(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()