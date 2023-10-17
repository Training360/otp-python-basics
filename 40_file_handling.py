from os import chdir, path

chdir(path.join(path.dirname(__file__), 'files'))

# file = open('text.txt', 'r')
# file.close()
with open('text.txt', 'r') as file:
    print(file.read())

with open('text.txt', 'r') as file:
    print(file.readline())

with open('text.txt', 'r') as file:
    print(file.readlines())

with open('text.txt', 'r') as file:
    for line in file:
        for char in line:
            print('chr:', char)

with open('text.txt', 'r') as file:
    print(file.readlines())
    file.seek(0)
    print(file.readline())
