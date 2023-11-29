import crud_operation
import file_handler
from lang import HU
from os import path

PATH = path.join(path.dirname(__file__), 'database', 'books.csv')

books = file_handler.read_file(PATH)


def list_books():
    print(books)


def find_book():
    # better if use isdigit and not converted directly
    id = int(input('Add meg a keresendő könyv ID-ját: '))
    print(crud_operation.find_item(id, books))


def update_book():
    id = int(input('Add meg a módosítandó könyv ID-ját: '))
    book = crud_operation.find_item(id, books)
    if book is not None:
        # title = input('Add meg a könyv új címét: ')
        # author = input('Add meg a könyv új szerződkét: ')
        keys = list(book.keys())
        keys.remove('id')
        for key in keys:
            data = input(f'Add meg az új {HU[key]} mező értékét: ')
            if data:
                book.update({key: data})
        crud_operation.update_item(id, book, books)
        file_handler.write_file(PATH, books)
        print('A könyvet sikeresen frissítettük.')
    else:
        print('Nincs ilyen Id-jú könyv!')


def create_book():
    keys = list(books[0].keys())
    keys.remove('id')
    book = {}
    for key in keys:
        data = input(f'Add meg a(z) {HU[key]} mező értékét: ')
        book.update({key: data})
    crud_operation.create_item(book, books)
    file_handler.write_file(PATH, books)
    print('A könyv létrehozva!')


def remove_book():
    id = int(input('Add meg a eltávolítandó könyv ID-ját!'))
    result = crud_operation.remove_item(id, books)
    # if item exits
    if result is not None:
        file_handler.write_file(PATH, books)
        print('A könyvet sikeresen töröltük.')
    else:
        print('Nincs ilyen Id-jú könyv')
