numbers = {1, 2, 3, 3}
print(numbers)

# TypeError
# print(numbers[0])

numbers.add(4)
print(numbers)
# KeyError
# numbers.remove(10)
# print(numbers)

# no error if the set does not contains element
numbers.discard(3)
print(numbers)

numbers.pop()
print(numbers)

numbers.update((6, 7, 8))
print(numbers)
