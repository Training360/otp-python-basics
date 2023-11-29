import csv
from os import path


def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        print([row for row in reader])


read_csv(path.join(path.dirname(__file__), 'data.csv'))

filepath = path.join(path.dirname(__file__), 'users.csv')
headers = ['id', 'name', 'location']
rows = [
    ['1', 'John', 'Heaven'],
    ['2', 'Jane', 'Hell'],
    ['3', 'Jesus', 'Earth'],
]


def write_to_csv(file, head, data):
    with open(file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(head)
        csv_writer.writerows(data)


write_to_csv(filepath, headers, rows)

users = [
    {'name': 'John', 'age': 52},
    {'name': 'Jane', 'age': 22},
    {'name': 'Johnny', 'age': 20},
]


def write_dict_list_to_csv(file: str, dict_list: list) -> None:
    fields = dict_list[0].keys()
    with open(file, 'w', newline='') as file:
        write = csv.DictWriter(file, fieldnames=fields)
        write.writeheader()
        write.writerows(dict_list)


write_dict_list_to_csv(path.join(path.dirname(__file__), 'users2.csv'), users)
