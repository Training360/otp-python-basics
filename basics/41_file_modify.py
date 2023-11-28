from os import chdir, path

chdir(path.join(path.dirname(__file__), 'files'))

with open('text.txt', 'w', encoding='utf-8') as file:
    content = ['new line 1', 'new line 2']
    for i in content:
        file.write(i + '\n')

with open('text.txt', 'w', encoding='utf-8') as file:
    content = ['new line 1', 'new line 2']
    lines = '\n'.join(content)
    file.write(lines)

with open('text.txt', 'a', encoding='utf-8') as file:
    content = ['append new line 1', 'append new line 2']
    lines = '\n'.join(content)
    file.write('\n' + lines)
