import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    database='db_MeusLivros',
    user='fbigal',
    password='Fbc#15111978'
    )

if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySql versão ',db_info)
    cursor =con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('conectado ao bando de dados ',linha)

if con.is_connected():
    cursor.close()
    con.close()
    print('conexão ao mysql foi encerrada')

