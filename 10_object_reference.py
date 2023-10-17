age = 30
age_copy = age

print(id(age))
print(id(age_copy))

age = 18
# print(age)
# print(age_copy)
print(id(age))
print(id(age_copy))

yearly_salary_list = [100_000, 120_000, 72_000, 54_000]
yearly_salary_list_copy = yearly_salary_list
print(id(yearly_salary_list))
print(id(yearly_salary_list_copy))

yearly_salary_list.append(111_000)
print(yearly_salary_list)
print(yearly_salary_list_copy)
print(id(yearly_salary_list))
print(id(yearly_salary_list_copy))

yearly_salary_list_copy.remove(72_000)
print(yearly_salary_list)
print(yearly_salary_list_copy)
print(id(yearly_salary_list))
print(id(yearly_salary_list_copy))

yearly_salary_list = [10, 20, 30]
print(yearly_salary_list)
print(yearly_salary_list_copy)
print(id(yearly_salary_list))
print(id(yearly_salary_list_copy))

names = ['Jane', 'John']
# names_copy = names.copy()
names_copy = names[:]
names.append('Johnny')
print(names, names_copy)
