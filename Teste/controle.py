from PyQt5 import uic,QtWidgets
import mysql.connector
"from reportlab.pdfgen import canvas"

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="fbigal",
    password="Fcb#91820460",
    database="cadastro_usuarios"
)
def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM usuarios")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM usuarios WHERE id="+ str(valor_id))
    usuario = cursor.fetchall()
    tela_editar.show()

    numero_id = valor_id

    tela_editar.lineEdit.setText(str(usuario[0][0]))
    tela_editar.lineEdit_2.setText(str(usuario[0][1]))
    tela_editar.lineEdit_3.setText(str(usuario[0][2]))
    tela_editar.lineEdit_4.setText(str(usuario[0][3]))
    tela_editar.lineEdit_5.setText(str(usuario[0][4]))
    tela_editar.lineEdit_6.setText(str(usuario[0][5]))
    tela_editar.lineEdit_7.setText(str(usuario[0][6]))
    tela_editar.lineEdit_8.setText(str(usuario[0][7]))
    

def salvar_dados_editados():
    #pega o numero do id
    global numero_id

    #valor no lineEdit para alteração
    codigo = tela_editar.lineEdit_2.text()
    nome = tela_editar.lineEdit_3.text()
    idade = tela_editar.lineEdit_4.text()
    telefone = tela_editar.lineEdit_5.text()
    endereco = tela_editar.lineEdit_6.text()
    responsavel = tela_editar.lineEdit_7.text()
    atividade = tela_editar.lineEdit_8.text()

    #atualiza os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE usuarios SET codigo = '{}', nome = '{}', idade = '{}', telefone = '{}', endereco = '{}', responsavel = '{}', atividade = '{}' WHERE id = {}".format(codigo, nome, idade, telefone, endereco, responsavel, atividade, numero_id))

    #atualiza janelas
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()


def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM usuarios")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM usuarios WHERE id="+ str(valor_id))    


def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM usuarios"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_usuarios.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Usuarios cadastrados:")
    pdf.setFont("Times-Bold", 15)

    pdf.drawString(10,750, "ID")
    pdf.drawString(35,750, "CODIGO")
    pdf.drawString(110,750, "NOME")
    pdf.drawString(170,750, "IDADE")
    pdf.drawString(230,750, "TELEFONE")
    pdf.drawString(340,750, "RESPONSAVEL")
    pdf.drawString(460,750, "ATIVIDADE")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(35,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(170,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(230,750 - y, str(dados_lidos[i][4]))
        pdf.drawString(340,750 - y, str(dados_lidos[i][5]))
        pdf.drawString(460,750 - y, str(dados_lidos[i][6]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()

    atividade = ""
    
    print("Código:",linha1)
    print("Nome:",linha2)
    print("Idade:",linha3)
    print("Telefone:",linha4)
    print("Endereço:",linha5)
    print("Responsavel:",linha6)

    if formulario.radioButton.isChecked():
        print(" A Atividade Reforço foi selecionanda")
        atividade = "Reforço"
    elif formulario.radioButton_2.isChecked():
        print(" A Atividade Violão foi selecionanda")
        atividade = "Violão"
    elif formulario.radioButton_3.isChecked():
        print(" A Atividade Teatro foi selecionanda")
        atividade = "Teatro"
    elif formulario.radioButton_4.isChecked():
        print(" A Atividade Desenho foi selecionanda")
        atividade = "Desenho"
    elif formulario.radioButton_5.isChecked():
        print(" A Atividade Pilates foi selecionanda")
        atividade = "Pilates"
    elif formulario.radioButton_6.isChecked():
        print(" A Atividade Jiu-Jitsu foi selecionanda")
        atividade = "Jiu-Jitsu"
              
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO usuarios (codigo, nome, idade, telefone, endereco, responsavel, atividade) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    dados = (str(linha1), str(linha2),str(linha3),str(linha4),str(linha5),str(linha6), atividade)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    
def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM usuarios"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(8)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 8):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
tela_editar=uic.loadUi("menu_editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)
segunda_tela.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados_editados)

formulario.show()
app.exec()

# criando a tabela

""" create table usuarios (
id INT NOT NULL AUTO_INCREMENT,
codigo INT,
nome VARCHAR(50),
idade INT,
telefone VARCHAR(15),
endereco VARCHAR(50),
responsavel VARCHAR(50),
atividade VARCHAR(25),
PRIMARY KEY (id)
);
 """
# inserindo registros na tabela

""" INSERT INTO usuarios (codigo, nome, idade, telefone, endereco, responsavel) VALUES (001, "Loren", 15, "11 98765-4321", "Rua Petro","Nathalia Lopes"); """
