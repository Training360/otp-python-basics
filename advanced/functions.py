# *args    - Non keyword arguments (tuple)
# **kwargs - Keyword arguments     (dict)

def log_args(first, *argv):
    print(first)
    print(argv)


log_args('first', 'middle1', 'middle2', 'last')


def log_kwargs(**kwargv):
    print(kwargv)


log_kwargs(name='John Doe', language='arabic', age=33)


def query(**kwargv):
    query = 'SELECT * FROM products WHERE '
    for k, v in kwargv.items():
        query += f"{k}='{v}' AND "
    return query[:-5]


print(query(color='red', size='xl', company='adidas'))


def calculate_total_price(*products, **price_details):
    total_price = sum(p['quantity'] * p['price'] for p in products)
    if 'vat' in price_details:
        total_price *= 1 + (price_details['vat'] / 100)
    if 'discount' in price_details:
        total_price *= 1 - (price_details['discount'] / 100)
    return total_price


def calculate_total_price_2(products, vat=0, discount=0):
    total_price = sum(p['quantity'] * p['price'] for p in products)
    if vat != 0:
        total_price *= 1 + (vat / 100)
    if discount != 0:
        total_price *= 1 - (discount / 100)
    return total_price


print(calculate_total_price(
    {'name': 'vga', 'quantity': 3, 'price': 1000},
    {'name': 'monitor', 'quantity': 10, 'price': 345},
    {'name': 'cpu', 'quantity': 2, 'price': 560},
    vat=27, discount=10
))

print(calculate_total_price_2(
    [
        {'name': 'vga', 'quantity': 3, 'price': 1000},
        {'name': 'monitor', 'quantity': 10, 'price': 345},
        {'name': 'cpu', 'quantity': 2, 'price': 560}
    ],
    27, 10
))
