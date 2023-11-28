name = 'John Doe'
# function
print(len(name))
print('First character:', name[0])
# IndexError
# print('First character:', name[8])

# TypeError
# name[0] = 'j'

print(f'uppercase name: {name.upper()}')
print(f'lowercase name: {name.lower()}')
print(name)
# name = name.upper()
print(f'is lowercase?: {name.islower()}')
print(f'count of "o"?: {name.count("o")}')
print(f'replace "o" to "O": {name.replace("o", "O")}')

print(float('100.000,5'.replace('.', '').replace(',','.')))

number_separator = 10_000_000
print(type(number_separator))

PI = 3.14159
print('The pi value is: {:.2f}'.format(PI))

value = 10000000.1012
print(f'{value:_}'.replace('_', ' '))
