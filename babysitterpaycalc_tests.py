from babysitterpaycalc import paycalc

def test_should_pay_12_for_one_regular_hour_shift():
    assert paycalc(5, 6) == 12

def test_should_pay_24_for_two_regular_hours():
    assert paycalc(5, 7) == 24
