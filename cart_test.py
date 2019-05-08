import pytest
from cart import to_usd

def test_to_usd():
    result = to_usd(5)
    assert result == "$5.00" # test USD sign

    result = to_usd(5.5)
    assert result == "$5.50" # test dec places

    result = to_usd(5.555444)
    assert result == "$5.56" #test rounding




 