import books

while True:
    # better if check the input value before convert to int
    command = int(input('''
    Válassz egy parancsot: 
    1. Könyvek kilistázása
    2. Könyv keresése 
    3. Könyv adatainak módosítása
    4. Új könyv beszúrása
    5. Könyv törlése
    6. Kilépés
    '''))
    if command == 1:
        books.list_books()
    elif command == 2:
        books.find_book()
    if command == 3:
        books.update_book()
    if command == 4:
        books.create_book()
    if command == 5:
        books.remove_book()
    if command == 6:
        break
    else:
        print('Érvénytelen parancs!')
