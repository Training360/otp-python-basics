name = 'John Doe'

# name[0]
# name[1]
# name[2]

for i in name:
    print(i)

net_prices = [1200, 1990, 12000, 875]

for i in net_prices:
    print(i)

# start, stop, step
for i in range(10, 0, -2):
    print(i)

for i in range(len(net_prices)):
    print(f'index: {i}, value: {net_prices[i]}')

for i, v in enumerate(net_prices):
    print(f'index: {i}, value: {v}')

vat_rate_in_percent = 27
gross_prices = []

for i in net_prices:
    # gross_price = i * (1 + vat_rate_in_percent / 100)
    # gross_prices.append(gross_price)
    gross_prices.append(i * (1 + vat_rate_in_percent / 100))

print(gross_prices)