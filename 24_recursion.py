def gcd_loop(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd_loop(10, 1115))


def gcd_rec(a, b):
    return a if b == 0 else gcd_rec(b, a % b)


print(gcd_rec(10, 1115))

num = 0  # false
if num:
    print('true')

strin = ''  # false
if strin:
    print('true')

lst = []  # false
if lst:
    print('true')
