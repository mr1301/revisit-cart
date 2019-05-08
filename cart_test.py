import pytest
from cart import to_usd

def test_to_usd():
    result = to_usd(5)
    assert result == "4"
