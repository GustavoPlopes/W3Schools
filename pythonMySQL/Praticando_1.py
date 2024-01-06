import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mydatabase'
)

mycursor = mydb.cursor()

# - Cria o Banco de dados -
# mycursor.execute('CREATE DATABASE mydatabase')

# - Exibe todos os bancos de dados já criados -
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

#  - Cria uma tabela no banco de dados incluindo suas respectivas colunas -
# mycursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(100))')

# - Exibe todas as tabelas criadas no banco de dados -
# mycursor.execute('SHOW TABLES')
# for x in mycursor:
#     print(x)

# - Para adicionar uma nova coluna a uma tabela - 
# mycursor.execute('ALTER TABLE customers ADD COLUMN email_address VARCHAR(60)')

# - Exclui uma coluna desejada -
# mycursor.execute('ALTER TABLE customers DROP email_address')

# - Para inserir os dados de cada coluna da tabela selecionada -
# sql = 'INSERT INTO customers (name,address) VALUES(%s,%s)'
# val = 'John', 'Highway 21'
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted")

# - Insere varios dados ao mesmo tempo - 
# sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple St 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael','Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'Was inserted.')
# - Simplificando - 
# mycursor.executemany(
#     'INSERT INTO customers (name, address) VALUES (%s, %s)',
#     [('Gustavo', 'Taguatinga'),
#      ('Maria', 'Ceilandia')]
#                      )
# mydb.commit()
# print(mycursor.rowcount,'Was inserted.')

# - Função mycursor.lastrowid usada no print para exibir o id da linha que acabou de botar na coluna -
# mycursor.execute('INSERT INTO customers (name, address) VALUES (%s, %s)',
#                  ('Michelle', 'Blue Village'))
# mydb.commit()
# print(f'1 tecord inserted, ID: { mycursor.lastrowid}')

# - Exibe todos as linhas da tabela customers - 
# mycursor.execute('SELECT * FROM customers')
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# - Simplificando - 
# mycursor.execute('SELECT * FROM customers')
# for x in mycursor:
#     print(x)

# - Exibe apenas as colunas selecionadas de cada linha - 
# mycursor.execute('SELECT name, address FROM customers')
# for x in mycursor:
#     print(x)

# - Método fetchone retorna apenas a primeira linha -
# mycursor.execute('SELECT * FROM customers')
# myresult = mycursor.fetchone()
# print(myresult)

# - O método WHERE filtra uma seleção para exibir apenas a linha seleção - 
# mycursor.execute("SELECT * FROM customers WHERE address = 'Park Lane 38'")
# for x in mycursor:
#     print(x)

# - Método para buscar e exibir pela coluna desejada e apenas os egistros que começam, incluem ou terminam com uma determinada letra ou frase.
# mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# - Serve como o método de cima, mas é mais seguro contra hackers -
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2",)
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# - Classifica as linhas de uma tabela em ordem crescente
# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# - Classifica em odem decrescente   
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# - Exclui registros de uma tabela existente usando a instrução “DELETE FROM”, todo registro que conter o valor passado será excluído, caso a clausula WHERE não for inserida todos os registros serão excluídos.
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, 'record(s) deleted')
# -
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2",)
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, 'Was deleted.')


# mycursor.execute('CREATE TABLE para_deletar (name VARCHAR (30))')
# - Exclui uma tabela interira existente
# sql = "DROP TABLE para_deletar"
# mycursor.execute(sql)

# - Se a tabela já foi excluída excluida ou por qualquer outro motivo não existe, pode usar a palavra-chave IF EXISTS para evitar erros. -
# sql = "DROP TABLE IF EXISTS para_deletar"
# mycursor.execute(sql)

#  - Altera a parte desejada de um registro para uma nova -
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, 'record(s) affected')
# -----------------------
# sql = "UPDATE customers SET name = 'Jairo' WHERE name = 'Gustavo'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, 'record(s) affected.')

# - Forma mais segura de fazer a alteração -
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ('Valley 345',  'Canyon 123')
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'record(s) affected.')

# - Limita quantas linhas de registros retonam -
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# - Limita quantas linhas de registros retonam e a partir de qual linha começa-
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 5")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)



