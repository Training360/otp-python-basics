import mariadb

connection = mariadb.connect(
    user='employees',
    password='employees',
    host='localhost',
    port=3306,
    database='employees'
)

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE if not exists employees (
#     id bigint not null auto_increment,
#     emp_name varchar(100),
#     primary key (id))''')

# cursor.execute("INSERT INTO employees(emp_name) VALUES (?)", ("John Doe",))
# cursor.execute("INSERT INTO employees(emp_name) VALUES (?)", ("Jane Doe",))

cursor.execute("SELECT * FROM employees")
result = cursor.fetchall()
print(result)

connection.commit()

# row = cursor.fetchone()
# print(row)
