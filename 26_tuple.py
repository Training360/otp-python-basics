yearly_salaries = (120_000, 90_000, 75_000)
print(yearly_salaries[0])

# TypeError
# yearly_salaries[0] = 56_000

print(len(yearly_salaries))
print(yearly_salaries.count(120_000))
print(yearly_salaries.index(120_000))

print(type(yearly_salaries))

new_yearly_salary = (50_000,)

print(type(new_yearly_salary))

yearly_salaries += new_yearly_salary
print(yearly_salaries)

yearly_salaries_list = list(yearly_salaries)
yearly_salaries_list.extend([23_000, 45_000])
yearly_salaries = tuple(yearly_salaries_list)

location = (27.6782, -121.4155)
rgb = (255, 178, 69)


def user_factory(first_name, last_name, age):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    age = int(age)
    return first_name, last_name, age


user = user_factory('john', 'doe', '45')
print(user, type(user))

print((1, 2) + (3, 4))
print((1, 2) * 4)

names = ('John', 'Jane', 'Johnny', 'Judith')
print(names[2:4])

numbers = [1, 2, 3, 4, 5]
squares = tuple(i ** 2 for i in numbers)
print(squares)
