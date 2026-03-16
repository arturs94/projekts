import pytest
from app import check_age, is_adult

def test_valid_age():
    assert check_age(18) == 18

def test_negative_age():
    with pytest.raises(ValueError):
        check_age(-5)

def test_non_integer_age():
    with pytest.raises(ValueError):
        check_age("18")

def test_is_adult():
    assert is_adult(20) == True
