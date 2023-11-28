yearly_salary_list = [100_000, 120_000, 72_000, 54_000]
max_salary = 100_000

for i in yearly_salary_list:
    if i > max_salary:
        break
    print(i)

for i in yearly_salary_list:
    if i > max_salary:
        continue
    print(i)
