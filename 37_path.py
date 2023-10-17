from os import path, getcwd

print('getcwd(): ', getcwd())
print('__file__: ', __file__)
print('abspath: ', path.abspath(__file__))  # = __file__
print('dirname: ', path.dirname(__file__))  # = getcwd()
print('basename: ', path.basename(__file__))
print(path.join(path.dirname(__file__), 'files', 'text.txt'))
