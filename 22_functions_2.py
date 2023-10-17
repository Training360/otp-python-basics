global_variable = 'global'
print(global_variable)


def fn():
    local_variable = 'local'
    print(global_variable)
    print(local_variable)


fn()
# print(local_variable)

variable = 'var'


def fn2():
    # UnboundLocalError
    # print(variable)
    global variable
    variable = 'fn var'
    print(variable)


fn2()
print(variable)


def increase_counter(counter):
    counter += 1
    print(counter)


my_counter = 1
increase_counter(my_counter)
print(my_counter)


# def add_item_to_cart(item, cart):
#     cart.append(item)
#     return cart

def add_item_to_cart(item, cart):
    cart = cart[:]
    cart.append(item)
    return cart


shopping_cart = ['VGA', 'cooler']
print(add_item_to_cart('CPU', shopping_cart))
print(shopping_cart)
