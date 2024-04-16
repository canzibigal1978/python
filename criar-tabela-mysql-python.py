import mysql.connector

try:
    # criar conexao ao banco de dados
    con = mysql.connector.connect(
        host="localhost",
        user="fbigal",
        password="Fcb#91820460",
        database="db_MeusLivros"
    )

    # Declaracao SQL a ser executada
    criar_tabela_SQL = """CREATE TABLE  tbl_produtos(
                            IdProduto int(11) not null,
                            NomeProduto varchar(70) not null,
                            preco float not null,
                            quantidade tinyint not null,
                            primary key (IdProduto)); """

    
    # Criar cursor e executar sql no banco de dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de produtos criada com sucesso!")
except mysql.connector.Error as erro:
    print ("Falha ao criar tabela no mysql: ()", format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao mysql finalizada")
