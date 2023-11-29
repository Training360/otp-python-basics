def read_file(filepath):
    with open(filepath, 'r') as file:
        books = []
        for line in file:
            id, title, author = line.rstrip().split(';')
            books.append({
                'id': int(id),
                'title': title,
                'author': author
            })
    return books


# better if create us append and update use write
def write_file(filepath, books):
    with open(filepath, 'w') as file:
        lines = ''
        for book in books:
            line = ';'.join(str(val) for val in book.values()) + '\n'
            lines += line
        # remove last \n
        file.write(lines)
