yearly_salary_list = [100_000, 120_000, 72_000, 54_000, 85_000, 150_000, 71_000]

print('from the 2', yearly_salary_list[2:])
print('to the 2', yearly_salary_list[:2])
print('from the 2 to 4', yearly_salary_list[2:4])
print('from the 1 to 6 step = 2', yearly_salary_list[1:6:2])
print('reverse, step = 2', yearly_salary_list[::-2])
print('last element', yearly_salary_list[-1])
print('copy', yearly_salary_list[:])

updated_salaries = [110_000, 75_000]
yearly_salary_list[2:4] = updated_salaries
print(yearly_salary_list)
