from random import randint, shuffle, choice, choices

number = randint(1, 100)
print(number)

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(numbers)

print(choice(numbers))
print(choices(numbers, weights=None, k=2))
