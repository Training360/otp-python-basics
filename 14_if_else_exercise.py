yearly_salary_list = [100_000, 120_000, 72_000, 54_000]
# greather or equal than high_salary_value
sum_high_salaries = 0
# smaller than high_salary_value
sum_low_salaries = 0
high_salary_value = 85_000

for salary in yearly_salary_list:
    if salary >= high_salary_value:
        sum_high_salaries += salary
    else:
        sum_low_salaries += salary

print(sum_high_salaries)
print(sum_low_salaries)

backend_languages = ['Java', 'Python', 'Php']
my_lang = 'Java'
if my_lang in backend_languages:
    print('Backend language')
else:
    print('Not a backend language')

temparature = 50
humidity = 70
rain = True

if temparature > 30 or humidity < 70 and not rain:
    print('Dry weather')

# not rain          False
# humidity < 70     False
#                   False and False = False
# temperature > 30  True
#                   False or True = True

if (temparature > 30 or humidity < 70) and not rain:
    print('Dry weather')

# temperature > 30      True
# humidity < 70         False
#                       True or False = True
# not rain              False
#                       True and False = False
