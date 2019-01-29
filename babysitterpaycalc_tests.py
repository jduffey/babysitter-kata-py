from babysitterpaycalc import paycalc

def test_should_pay_12_for_one_regular_hour_shift():
    assert paycalc(5, 6) == 12
