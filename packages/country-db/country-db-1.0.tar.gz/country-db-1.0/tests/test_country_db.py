import pytest
from country_db import get

def test_get_by_name():
    country = get(name="India")
    assert country is not None
    assert country["CountryName"] == "India"
    assert country["Alpha2Code"] == "IN"

def test_get_by_alpha2_code():
    country = get(alpha2_code="US")
    assert country is not None
    assert country["CountryName"] == "United States of America"
    assert country["Alpha3Code"] == "USA"

def test_get_by_currency_code():
    country = get(currency_code="EUR")
    assert country is not None
    assert "Euro" in country["CurrencyName"]

def test_invalid_parameter():
    with pytest.raises(ValueError):
        get(invalid_param="test")

def test_no_parameters():
    with pytest.raises(ValueError):
        get()

def test_country_not_found():
    assert get(name="NonExistentCountry") is None