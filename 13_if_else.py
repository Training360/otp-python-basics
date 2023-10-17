yearly_salary_in_usd = 100_000
high_salary_value = 120_000

print('start')

if yearly_salary_in_usd > high_salary_value:
    print('High salary')
else:
    print('Low salary')

print('end')

grade = int(input('Adj meg egy osztályzatot: '))

# <, >, <=, >=, ==, !=, in
if grade == 1:
    print('Elégtelen')
elif grade == 2:
    print('Elégséges')
elif grade == 3:
    print('Közepes')
elif grade == 4:
    print('Jó')
elif grade == 5:
    print('Jeles')
else:
    print('Ez nem osztályzat')

# match case van
