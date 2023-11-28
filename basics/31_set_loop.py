numbers = {1, 2, 3, 4, 5}

for i in numbers:
    print(i)

# print(len(numbers))
# Error, set is not indexed
# print(numbers[0])
# convert to list
# numbers_list = list(numbers)
# for i in range(len(numbers)):
#     print(numbers[i])

for i, v in enumerate(numbers):
    print(i, v)
