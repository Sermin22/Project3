import pytest
from src.taxes import calculate_taxes, calculate_tax

@pytest.fixture
def prices():
    return [100, 200, 300]


@pytest.mark.parametrize("tax_rate, expected", [
    (10, [110, 220, 330]),
    (15, [115, 230, 345]),
    (20, [120, 240, 360])

])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate = -1)


def test_calculate_taxes_invalid_tax_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0, -1], tax_rate = 10)


@pytest.mark.parametrize("price, tax_rate, expected", [
    ([100.0, 10.0, 110.0]),
    ([50.0, 5.0, 52.5])
])

def test_calculate_tax(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


def test_calculate_tax_price_minus():
    with pytest.raises(ValueError):
        calculate_tax(-0.1, tax_rate = 10)


def test_calculate_tax_tax_rate_incorrect():
    with pytest.raises(ValueError):
        calculate_tax(100.0, -0.1)

def test_calculate_tax_tax_rate_incorrect_2():
    with pytest.raises(ValueError):
        calculate_tax(100.0, 100.0)

def test_calculate_tax_tax_rate_incorrect_3():
    with pytest.raises(ValueError):
        calculate_tax(100.0, 100.1)


