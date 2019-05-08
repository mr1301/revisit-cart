import pytest
from cart import to_usd, tax_rate, find_product

def test_to_usd():
    result = to_usd(5)
    assert result == "$5.00" # test USD sign

    result = to_usd(5.5)
    assert result == "$5.50" # test dec places

    result = to_usd(5.555444)
    assert result == "$5.56" #test rounding

def test_tax_rate():
    assert(tax_rate) == 0.06

def test_find_product():
   products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]
   match_product = find_product("2",products)
   assert match_product["department"] == "pantry"

   with pytest.raises(IndexError):
       find_product("50",products)