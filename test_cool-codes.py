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
    assert make_last_false_while(3)
