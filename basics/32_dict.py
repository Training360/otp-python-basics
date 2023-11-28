user = {
    'name': 'John Doe',
    'age': 30
}

print(type(user))

dict_duplicated_keys = {'name': 'John', 'name': 'Jane'}
print(dict_duplicated_keys)

user['name'] = 'Jane Doe'
print(user['name'])

user['job'] = 'teacher'
print(user)

user.update({'age': 31, 'name': 'Mrs. Jane Smith', 'hobby': 'sleeping'})
print(user)

user.pop('hobby')
print(user)
