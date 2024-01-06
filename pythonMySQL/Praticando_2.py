import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mydatabase_2'
)

mycursor = mydb.cursor()

# mycursor.execute('CREATE DATABASE mydatabase_2')

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(40), fav INT(10))")

# sql = "INSERT INTO users (name, fav) VALUES(%s,%s)"
# val = [('John', 154),
#        ('Peter', 154),
#        ('Amy', 155),
#        ( 'Hannah', 156),
#        ('Michael', 156 )]

# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'record(s) inserted.')

# mycursor.execute('CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(40))')

# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = [('154', 'Chocolate Heaven'),
#        ('155', 'Tasty Lemons'),
#        ('156', 'Vanilla Dreams')]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'record(s) created')

# - Combina linhas de duas ou mais tabelas, com base em uma coluna relacionada entre elas, usando uma instrução JOIN.
# sql = "SELECT \
#     users.name AS user, \
#     products.name AS favorite \
#     FROM users \
#     INNER JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# - Mostrar todos os usuários, mesmo que eles não tenham um produto favorito, use a instrução LEFT JOIN -
# sql = "SELECT users.name, products.name FROM users \
#     LEFT JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

sql = "SELECT users.name, products.name FROM users \
    RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
for x in mycursor:
    print(x)






# mycursor.execute("SELECT * FROM users")
# for x in mycursor:
#     print(x)
    
# mycursor.execute("SELECT * FROM products")
# for x in mycursor:
#     print(x)


