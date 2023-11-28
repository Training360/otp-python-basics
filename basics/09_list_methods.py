yearly_salary_list = [100_000, 120_000, 72_000, 54_000]

# CRUD
# hozzáad a végéhez
yearly_salary_list.append(66_000)
print(yearly_salary_list)
# t9bb elemet ad hozzá, összetett adatszerkezetet vár paraméternként
yearly_salary_list.extend([88_000, 91_000])
print(yearly_salary_list)
# egy elemet add hozzá, a megadott indexű helyre teszi
yearly_salary_list.insert(2, 99_990)
print(yearly_salary_list)

# adott indexű elemet töröl ki
del yearly_salary_list[0]
print(yearly_salary_list)
# adtott érték első előfordulásának törlése
yearly_salary_list.remove(54_000)
print(yearly_salary_list)
# utolsó elem törlése
yearly_salary_list.pop()
print(yearly_salary_list)
# adott érték darabszáma
print(yearly_salary_list.count(120_000))

yearly_salary_list.sort()
print(yearly_salary_list)
yearly_salary_list.sort(reverse=True)
print(yearly_salary_list)

names = ['John', '"the dead"' , 'Doe']
print(' '.join(names))


