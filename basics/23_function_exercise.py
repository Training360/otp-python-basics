def calculate_gross_price(price, vat_percent):
    return price * (1 + vat_percent / 100)


def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)


def calculate_final_price(price, vat_percent=27, discount_percent=0):
    discount_price = price if discount_percent == 0 else apply_discount(price, discount_percent)
    return calculate_gross_price(discount_price, vat_percent)


def calc(price, vat_percent=27, discount_percent=0):
    discount_price = price * (1 - discount_percent / 100)
    return discount_price * (1 + vat_percent / 100)
