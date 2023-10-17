user = {
    'name': 'Gizi néni',
    'age': 72,
    'job': 'teacher',
    'nationality': 'Hungary'
}

for i in user:
    print(i, user[i])

for i, v in enumerate(user):
    print(i, v)

# print(len(user))
# for i in range(len(user)):
#     # KeyError
#     print(user[i])

print('keys:', user.keys())
print('values:', user.values())
print('items:', user.items())

for i in user.values():
    print(i)

for i, v in user.items():
    print(i, v)
