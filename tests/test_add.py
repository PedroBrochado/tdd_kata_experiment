from main import add


def test_calculate_empty_string_returns_zero():
    assert add("") == 0
