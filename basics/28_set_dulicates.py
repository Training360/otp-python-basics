numbers = [1, 2, 3, 3, 5, 4, 1, 2, 3, 4, 3, 2]

# v1
# numbers_without_duplicates = []
#
# for i in numbers:
#     if i not in numbers_without_duplicates:
#         numbers_without_duplicates.append(i)
#
# print(numbers_without_duplicates)

# v2 - NOT USE IT
# numbers_without_duplicates = []
# a = [numbers_without_duplicates.append(i) for i in numbers if
#      i not in numbers_without_duplicates]

# print(numbers_without_duplicates)

numbers_without_duplicates = list(set(numbers))
print(numbers_without_duplicates)
