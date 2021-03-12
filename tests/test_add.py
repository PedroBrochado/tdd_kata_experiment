from main import add


def test_calculate_empty_string_returns_zero():
    assert add("") == 0


def test_calculate_single_number_string_returns_sum():
    assert add("1") == 1


def test_calculate_two_number_string_returns_sum():
    assert add("1,2") == 3



