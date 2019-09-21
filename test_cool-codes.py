import pytest
from fractions import simplify_fraction
def test_simplify_fraction():
    assert simplify_fraction(2,4) == (1,2)
    assert simplify_fraction(124,4) == (31,1)
    assert simplify_fraction(1,2) == (1,2)

from fractions import greatest_common_divisor 
def test_gcd():
    assert greatest_common_divisor(3,4) == 1
    assert greatest_common_divisor(12,6) == 6
    assert greatest_common_divisor(222468, 542) == 2

from make_last_false import make_last_false, make_last_false_while
def test_make_last_false():
    assert list(make_last_false(0)) == [False]
    assert list(make_last_false(1)) == [True, False]
    assert list(make_last_false(5)) == [True, True, True, True, True, False]

from multiple_inheritance import Clock
def test_clock():
    time = Clock(23,1,1)
    assert str(time) == '23:1:1'
    time.tick()
    assert repr(time) == 'Clock(23, 1, 2)'

    with pytest.raises(Exception) as e_time:
        Clock(24,1,1)
        Clock(23,60,1)
        Clock(23,45,60)
    

from multiple_inheritance import Calendar
def test_calendar():
    date = Calendar(1984, 4, 17)
    assert str(date) == '17.4.1984'
    Calendar.date_style = 'American'
    assert str(date) == '4.17.1984'
    date.advance()
    assert repr(date) == 'Calendar(1984, 4, 18)'

    with pytest.raises(Exception) as e_date:
        Calendar(1984, 13, 17)
        Calendar(1984, 2, 30)

    # set date_style back to default
    Calendar.date_style = 'British'

from multiple_inheritance import CalendarClock
def test_calendarclock():
    time = CalendarClock(1984, 4, 17, 14, 37, 21)
    assert str(time) == '14:37:21 17.4.1984'
    assert repr(time) == 'CalendarClock(1984, 4, 17, 14, 37, 21)'

    with pytest.raises(Exception) as e_timedate:
        CalendarClock(1984, 13, 17, 14, 37, 21)
        CalendarClock(1984, 4, 43, 14, 37, 21)
        CalendarClock(1984, 4, 17, 34, 37, 21)
        CalendarClock(1984, 4, 17, 14, 60, 21)
        CalendarClock(1984, 4, 17, 14, 37, 70)
