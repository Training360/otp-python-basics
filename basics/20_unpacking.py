# first_name = 'John'
# last_name = 'Doe'
# age = 30

first_name, last_name, age = 'John', 'Doe', 30

a = 10
b = 20

a, b = b, a
print(a, b)

abc = 'abcdef'
# a = abc[0]
# b = abc[1]
# c = abc[2]
a, b, c, *others = abc

print(a, b, c, others)

name = 'John'
f, *_, l = name
print(f, l, _)

user = ['Gergely', 'Gáll', 'mentor']
first_name, last_name, job = user
print(first_name, last_name, job)

grades = [1, [2, 3, 4], 5, [4, 5, 3, 1]]
a, b, c, d = grades
print(a, b, c, d)

a, (b, c, d), e, (f, g, h, i) = grades
print(a, b, c, d, e, f, g, h, i)
