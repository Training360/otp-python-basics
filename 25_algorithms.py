def get_minimum(values):
    min_value = values[0]
    for i in range(1, len(values)):
        if values[i] < min_value:
            min_value = values[i]
    return min_value


# def get_minimum(values):
#     min_value = float('inf')
#     for i in values:
#         if i < min_value:
#             min_value = i
#     return min_value


val = [10, 20, 30, 40, 50]
print(get_minimum(val))

print(min(val))


def summa(values):
    sum_value = 0
    for i in values:
        sum_value += i
    return sum_value


val = [10, 20, 30, 40, 50]
print(summa(val))

print(sum(val))


def average(values):
    return summa(values) / len(values)


val = [10, 20, 30, 40, 50]
print(average(val))

print(sum(val) / len(val))


def count_value(values, search):
    counter = 0
    for i in values:
        if i == search:
            counter += 1
    return counter


val = [10, 20, 30, 40, 50, 20, 20]
print(count_value(val, 20))

print(val.count(20))


def get_index(values, element):
    for i in range(len(values)):
        if values[i] == element:
            return i
    # return -1


val = [10, 20, 30, 40, 50]
print(get_index(val, 20))

print(val.index(20))


def is_contains(values, search):
    for i in values:
        if i == search:
            return True
    return False


val = [10, 20, 30, 40, 50]
print(is_contains(val, 10))
print(is_contains(val, 100))

print(10 in val)
print(100 in val)
