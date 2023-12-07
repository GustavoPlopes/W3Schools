import mysql.connector

# Para conectar ao meu banco de dados
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# "Para criar uma base de dados"
# # mycursor.execute('CREATE DATABASE mydatabase')

# "Para mostrar o banco de dados selecionado"
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# "Cria tabelas"
# mycursor.execute("CREATE TABLE customers (name VARCHAR(30), address VARCHAR(40))")

# "Criar em uma tabela existente"
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# "Para preencher uma tabela no MySQL, use a instrução “INSERT INTO”"
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# "Para comitar e as alterações serem feitas"
# mydb.commit()

# "Mostrar se foi inserido na tabela"
# print(mycursor.rowcount, "record inserted.")

# "Para inserir várias linhas em uma tabela, use o executemany()método
# O segundo parâmetro do executemany()método é uma lista de tuplas, contendo os dados que você deseja inserir"
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ("Peter", "Lowstreet 4"),
#     ("Amy", "Apple st 62"),
#     ("Hannah", "Mountain 21")
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

# "Exibe as tabelas criadas"
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Ble Village")
# mycursor.execute(sql, val)
# mydb.commit()
# Print para exibir o numero do id inserido na nova linha da tabela
# print("1 record inserted, ID:", mycursor.lastrowid)

# ""Exibe todos os dados da tabela selecionada, Usamos o fetchall() método que busca todas as""
# linhas da última instrução executada.
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# "Para selecionar apenas algumas colunas em uma tabela"
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x

# "Se você estiver interessado apenas em uma linha, poderá usar o fetchone()método.
# O fetchone()método retornará a primeira linha do resultado"
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)

# Exibe registro apenas de onde o endereço foi encontrado
# sql = ("SELECT * FROM customers "
#        "WHERE address = 'Apple st 62'")
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#  "selecionar os registros que começam, incluem ou terminam com uma determinada letra ou frase."
# sql = ("SELECT * FROM customers "
#        "WHERE address LIKE '%way%'")
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# Isso evita injeções de SQL, que é uma técnica comum de hacking na Web para destruir ou
# usar indevidamente seu banco de dados. O módulo mysql.connector possui métodos para escapar dos valores da consulta:
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Lowstreet 4",)
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# Use a instrução ORDER BY para classificar o resultado em ordem crescente ou decrescente.
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)