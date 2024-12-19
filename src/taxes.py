def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float, tax_rate: float) -> float:
    '''Вычисляет стоимость товара с учетом налога и возвращать результат'''

    if price < 0:
        raise ValueError('Неверная цена')
    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')
    result = price * (100.0 + tax_rate) / 100.0
    return result
