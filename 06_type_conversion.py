first_name = 'John'
last_name = 'Doe'
# version 1
full_name = 'My full name is: ' + first_name + ' ' + last_name
print(full_name)
# version 2
full_name = 'My full name is: {0} {1}'.format(first_name, last_name)
print(full_name)
# version 3
full_name = f'My full name is {first_name} {last_name}'
print(full_name)

print('Hello' * 2)

yearly_salary_in_usd = '100000'
yearly_salary_in_usd_int = int('100000')
print(yearly_salary_in_usd_int, type(yearly_salary_in_usd_int))

PI = '3.14159'
pi_float = float(PI)
print(type(pi_float))

str_num = str(1000)
print(str_num, type(str_num))

print(r'Juhu \n \t etc')
