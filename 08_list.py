sample_list = [10, 10.10, 'str', True, None, [1,2,3], 10, 10]
print(sample_list[0])
sample_list[0] = 'Ten'
print(sample_list)

sample_list = []
print(sample_list)

yearly_salary_list = [100_000, 120_000, 72_000, 54_000]
print(len(yearly_salary_list))
yearly_salary_list_2 = [110_000, 42_000]

print(yearly_salary_list + yearly_salary_list_2)
print(yearly_salary_list * 2)
print(100_000 in yearly_salary_list)

