# print()
# len()
# type()
# input()
#
# ''.join()
# [].append()

print(dir(__builtins__))


def greeting(name):
    print(f'Hi {name}')


greeting('John')
greeting('Jane')
print(greeting('T360'), type(greeting('T360')))


# TypeError
# greeting()

def even_or_odd(number):
    # v0
    # if number % 2 == 0:
    #     return 'even'
    # else:
    #     return 'odd'

    # v1
    # if number % 2 == 0:
    #     return 'even'
    # return 'odd'

    # v2
    # result = 'even' if number % 2 == 0 else 'odd'
    # return result

    # v3
    return 'even' if number % 2 == 0 else 'odd'
    # other prog languages
    # return number % 2 == 0 ? 'even' : 'odd'


print(even_or_odd(10))
print(even_or_odd(11))
print(even_or_odd(11))


def calulate_gross_price(price, vat_percent=27):
    return price * (1 + vat_percent / 100)


result = calulate_gross_price(100, 27)
print(result)

print(calulate_gross_price(10_000))
print(calulate_gross_price(20_000))


# def add_item_to_basket(item, basket=[]):
#     basket.append(item)
#     return basket

def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


# print(add_item_to_basket('VGA', ['CPU', 'Cooler']))
print(add_item_to_basket('VGA'))
print(add_item_to_basket('CPU'))
print(add_item_to_basket('Cooler'))
