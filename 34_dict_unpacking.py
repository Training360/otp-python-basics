user = {
    'name': 'Gizi néni',
    'age': 72,
    'job': 'teacher',
    'nationality': 'Hungary'
}

name, age, job, nationality = user.values()
print(name, age, job, nationality)

cart_net_prices = {'VGA': 1000, 'CPU': 500, 'Monitor': 300}
cart_gross_prices = {k: v * 1.27 for k, v in cart_net_prices.items()}
print(cart_gross_prices)
