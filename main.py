from customtkinter import *
import database
import os

#Limpa o Terminal para Facilitar a Visualização de Informações
os.system("cls")

#Conecta no Banco de Dados
database.conecta_db()

#Criando a Janela
pysina = CTk()

#Definindo as Proporções
win_width, win_height = 1280, 720
pysina.geometry("{}x{}".format(win_width, win_height))

#Definindo o Nome da Aplicação
pysina.title("Pysina")

#Definindo o Tema da Janela
set_default_color_theme("green.json")

#Variáveis de Verificação 
introComplete = False
varComplete = False
condicionalComplete = False
arrayComplete = False
switch_var = StringVar(value = "off")

#----------------------------------------------------- PALETA DE CORES DO APP -----------------------------------------------------#

BACKGROUND_COLOR = "#282A36"
BOX_COLOR = "#44475A"
COMENT_COLOR = "#6272A4"
FOREGROUND_COLOR = "#F8F8F2"
BUTTON_COLOR = "#309A7B"
PRESSIONED_COLOR = "#64895C"
ORANGE_COLOR = "#FFB86C"

#----------------------------------------------------- CRIANDO JANELAS -----------------------------------------------------#

#Background
background = CTkFrame(master = pysina, fg_color = BACKGROUND_COLOR, width = 1920, height = 1080)
background.place(x = 0, y = 0)

#Box de Auxilio
box = CTkFrame(master = background, fg_color = BOX_COLOR, width = 1200, height = 600, border_color = BACKGROUND_COLOR, border_width = 2)
box_width, box_height = 1200, 600

#Janelas da Variavel
janela = CTkTabview(master = background, fg_color = BOX_COLOR, width = 1200, height = 600, border_color = BACKGROUND_COLOR, border_width = 2,)
janela.add("Inteiro")
janela.add("Float")
janela.add("String")
janela.add("Booleano")
janela.add("Constante")

#Box de Auxilio Arrays
boxArrays = CTkFrame(master = background, fg_color = BOX_COLOR, width = 1200, height = 600, border_color = BACKGROUND_COLOR, border_width = 2)

#Box de Login e Registro
boxLogin = CTkFrame(master = background, fg_color = BOX_COLOR, width = 500, height = 700, border_color = BACKGROUND_COLOR, border_width = 2)

#----------------------------------------------------- FUNÇÕES -----------------------------------------------------#

#Texto de suporte para Certo e Errado
acertouLabel = CTkLabel(master = box, wraplength = box_width - 90, text = "Acertou vamos para o próximo tópico a ser abordado", justify = LEFT, font = ("Arial", 18), text_color = BUTTON_COLOR)
errouLabel = CTkLabel(master = box, wraplength = box_width - 90, text = "Isso não está correto. Tente novamente", justify = LEFT, font = ("Arial", 18), text_color = ORANGE_COLOR)
contaNaoExiste = CTkLabel(master = boxLogin, wraplength = box_width - 90, text = "Essa Conta não existe, Tente novamente", justify = LEFT, font = ("Arial", 18), text_color = ORANGE_COLOR)
falta_algo = CTkLabel(master = boxLogin, wraplength = box_width - 90, text = "Preencha todos os campos", justify = LEFT, font = ("Arial", 18), text_color = ORANGE_COLOR)
senhaNãoEstaIgual = CTkLabel(master = boxLogin, wraplength = box_width - 90, text = "As senhas devem ser iguais", justify = LEFT, font = ("Arial", 18), text_color = ORANGE_COLOR)
nomeNãoCorreto = CTkLabel(master = boxLogin, wraplength = box_width - 90, text = "Os nomes de usuário devem ter no mínimo 4 letras", justify = LEFT, font = ("Arial", 18), text_color = ORANGE_COLOR)
erro = CTkLabel(master = boxLogin, wraplength = box_width - 90, text = "Arrume o Problema", justify = LEFT, font = ("Arial", 18), text_color = ORANGE_COLOR)

#Função para Retornar a Tela de Login
def returnToLogin_clique():
    boxLogin.place(x = 770, y = 11)
    CrieSuaConta.place(x = 50, y = 150)
    email.place(x = 50, y = 260)
    senha.place(x = 50, y = 310)
    exibirSenha.place(x = 50, y = 360)
    login_btn.place(x = 50, y = 410)
    naoTemConta.place(x = 55, y = 465)
    registre_btn.place(x = 240, y = 460)
    CrieSuaContaR.place_forget()
    nomeUsuario.place_forget()
    emailcad.place_forget()
    senhacad.place_forget()
    repitaSenha.place_forget()
    criarConta_btn.place_forget()
    returnToLogin_btn.place_forget()

#Função do Botão Criar Conta
def criarConta_clique():
    usuario = nomeUsuario.get()
    email_cadastrado = emailcad.get()
    senha_cadastrada = senhacad.get()
    senha_reescrita = repitaSenha.get()

    database.conecta_db()

    try:
        if (usuario == "" or email_cadastrado == "" or senha_cadastrada == "" or senha_reescrita == ""):
            falta_algo.place(x = 55, y = 600)
            falta_algo.after(2000, lambda: falta_algo.place_forget())
        elif (senha_cadastrada != senha_reescrita):
            senhaNãoEstaIgual.place(x = 55, y = 600)
            senhaNãoEstaIgual.after(2000, lambda: senhaNãoEstaIgual.place_forget())
        elif (len(usuario) < 4):
            nomeNãoCorreto.place(x = 55, y = 600)
            nomeNãoCorreto.after(2000, lambda: nomeNãoCorreto.place_forget())
        else:

            database.cursor.execute("""
            INSERT INTO user (Username, Email, Password, ConfPassword)
            VALUES (?, ?, ?, ?)""", (usuario, email_cadastrado, senha_cadastrada, senha_reescrita))

            database.conn.commit()
            print("Dados Cadastrados com Sucesso!")
            limpaCadastro()
            
    except:
        pass

#Função Exibir Senha
def switch_event():
    if switch_var.get() == "off":
        senha.configure(show = ("*"), font = ("Arial", 18))
        senhacad.configure(show = ("*"), font = ("Arial", 18))
        repitaSenha.configure(show = ("*"), font = ("Arial", 18))
    else:
        senha.configure(show = (), font = ("Arial", 18))
        senhacad.configure(show = (), font = ("Arial", 18))
        repitaSenha.configure(show = (), font = ("Arial", 18))

#Função do Botão de Login
def entrar_clique():
    email_login = email.get()
    senha_login = senha.get()

    database.conecta_db()

    database.cursor.execute("SELECT * FROM user WHERE (Email = ? AND Password = ?)", (email_login, senha_login))
    verifica_dados = database.cursor.fetchone() #Percorre a Tabela Usuários
    print(email_login, senha_login)
    print(verifica_dados)

    if email == "" or senha == "":
        falta_algo.place(x = 55, y = 550)
        falta_algo.after(2000, lambda: falta_algo.place_forget())

    elif (email_login in verifica_dados and senha_login in verifica_dados):
        titulo_pysina.place(x = 70, y = 80)
        sub_pysina.place(x = 72, y = 165)
        intro_btn.place(x = 74, y = 230)
        boxLogin.place_forget()
        CrieSuaConta.place_forget()
        email.place_forget()
        senha.place_forget()
        exibirSenha.place_forget()
        login_btn.place_forget()
        registre_btn.place_forget()
        limpaLogin()
    else:
        contaNaoExiste.place(x = 55, y = 500)
        contaNaoExiste.after(2000, lambda: contaNaoExiste.place_forget())

#Função de Remover Informações dos Campos de Cadastro
def limpaCadastro():
    nomeUsuario.delete(0, END)
    emailcad.delete(0, END)
    senhacad.delete(0, END)
    repitaSenha.delete(0, END)

#Função de Remover Informações dos Campos de Login
def limpaLogin():
    email.delete(0, END)
    senha.delete(0, END)

#Botão que Envia Para a Tela de Registro de Contas
def registre_clique():
    CrieSuaContaR.place(x = 50, y = 150)
    nomeUsuario.place(x = 50, y = 240)
    emailcad.place(x = 50, y = 290)
    senhacad.place(x = 50, y = 340)
    repitaSenha.place(x = 50, y = 390)
    exibirSenha.place(x = 50, y = 440)
    criarConta_btn.place(x = 50, y = 490)
    returnToLogin_btn.place(x = 50, y = 540)
    CrieSuaConta.place_forget()
    email.place_forget()
    senha.place_forget()
    registre_btn.place_forget()
    naoTemConta.place_forget()
    login_btn.place_forget()
    contaNaoExiste.place_forget()

#Envia você para a Pagina de Introdução ao Python
def intro_clique():
    box.place(x = 40, y = 80)
    returnToMenu.place(x = 40, y = 30)
    intro_title.place(x = 570, y = 30)
    introducao.place(x = 55, y = 40)
    printHello.place(x = 55, y = 230)
    confirme_btn.place(x = 55, y = 280)
    titulo_pysina.place_forget()
    sub_pysina.place_forget()
    intro_btn.place_forget()
    variaveis_btn.place_forget()
    condicional_btn.place_forget()
    condicional_label.place_forget()
    array_btn.place_forget()

#Função do Botão Que verifica se Você Acertou ou Errou A tela de Print
def confirmeClick():
    if printHello.get() == "print('Olá Mundo')":
        acertouLabel.place(x = 55, y = 350)
        acertouLabel.after(2000, lambda: acertouLabel.place_forget())
        acertouLabel.after(2050, lambda: proxComent())

    elif printHello.get() == 'print("Olá Mundo")':
        acertouLabel.place(x = 55, y = 350)
        acertouLabel.after(2000, lambda: acertouLabel.place_forget())
        acertouLabel.after(2050, lambda: proxComent())

    else:
        errouLabel.place(x = 55, y = 350)
        errouLabel.after(3000, lambda: errouLabel.place_forget())

#Função do Botão que verifica se você acertou ou errou a tela de comentarios
def confirmeClick2():
    global introComplete

    if printComent.get() == "#Eu programo com o Pysina.":
        acertouLabel.place(x = 55, y = 470)
        acertouLabel.after(2000, lambda: acertouLabel.place_forget())
        acertouLabel.after(2050, lambda: returnToClick())
        introComplete = True
        if introComplete == True:
            intro_btn.configure(fg_color = COMENT_COLOR, hover_color = "#566081")

    elif printComent.get() == "#Eu programo com o Pysina":
        acertouLabel.place(x = 55, y = 470)
        acertouLabel.after(2000, lambda: acertouLabel.place_forget())
        acertouLabel.after(2050, lambda: returnToClick())
        introComplete = True
        if introComplete == True:
            intro_btn.configure(fg_color = COMENT_COLOR, hover_color = "#566081")

    else:
        errouLabel.place(x = 55, y = 470)
        errouLabel.after(3000, lambda: errouLabel.place_forget())

#Função que confirma que você terminou o modulo variáveis
def confirmeClick3():
    global varComplete
    varComplete = True
    variaveis_btn.configure(fg_color = COMENT_COLOR, hover_color = "#566081")
    returnToClick()

#Função que confirma que você terminou o modulo condicionais
def confirmeClick4():
    global condicionalComplete
    condicionalComplete = True
    condicional_btn.configure(fg_color = COMENT_COLOR, hover_color = "#566081")
    returnToClick()

#Função que confirma que você terminou o modulo arrays
def confirmeClick5():
    global arrayComplete
    arrayComplete = True
    array_btn.configure(fg_color = COMENT_COLOR, hover_color = "#566081")
    returnToClick()

#Função que envia para os comentarios
def proxComent():
    box.place(x = 40, y = 80)
    returnToMenu.place(x = 40, y = 30)
    coment_title.place(x = 570, y = 30)
    coment.place(x = 50, y = 40)
    comentex.place(x = 50, y = 110)
    coment2.place(x = 50, y = 150)
    comentex2.place(x = 50, y = 200)
    coment3.place(x = 50, y = 320)
    printComent.place(x = 50, y = 360)
    confirme_btn2.place(x = 50, y = 410)
    introducao.place_forget()
    printHello.place_forget()
    confirme_btn.place_forget()
    intro_title.place_forget()
    condicional_label.place_forget()

#Envia você para a pagina de variáveis
def variable_clique():
    returnToMenu.place(x = 40, y = 30)
    variable_title.place(x = 570, y = 30)
    janela.place(x = 40, y = 60)
    variableLbl.place(x = 50, y = 40)
    variableex.place(x = 50, y = 145)
    variableLbl2.place(x = 50, y = 180)
    variableex2.place(x = 50, y = 265)
    variableLbl3.place(x = 50, y = 365)
    variableLbl4.place(x = 50, y = 40)
    variableex3.place(x = 50, y = 130)
    variableLbl5.place(x = 50, y = 165)
    variableLbl6.place(x = 50, y = 350)
    variableLbl7.place(x = 50, y = 40)
    variableex4.place(x = 50, y = 150)
    variableLbl8.place(x = 50, y = 250)
    variableex5.place(x = 50, y = 420)
    variableLbl9.place(x = 50, y = 40)
    variableex6.place(x = 50, y = 125)
    variableLbl10.place(x = 50, y = 160)
    variableex7.place(x = 50, y = 290)
    variableLbl11.place(x = 50, y = 410)
    variableLbl12.place(x = 50, y = 40)
    variableex8.place(x = 50, y = 235)
    variableLbl13.place(x = 50, y = 300)
    confirme_btn3.place(x = 50, y = 440)
    titulo_pysina.place_forget()
    sub_pysina.place_forget()
    intro_btn.place_forget()
    variaveis_btn.place_forget()
    intro_title.place_forget()
    condicional_btn.place_forget()
    array_btn.place_forget()
    if varComplete == True:
        confirme_btn3.place_forget()

#Função que envia para as condicionais
def condicional_clique():
    returnToMenu.place(x = 40, y = 30)
    box.place(x = 40, y = 80)
    condicional_title.place(x = 570, y = 30)
    condicional_label.place(x = 50, y = 40)
    if_label.place(x = 50, y = 145)
    if_example.place(x = 50, y = 180)
    elif_label.place(x = 50, y = 265)
    elif_example.place(x = 50, y = 315)
    prox_btn.place(x = 100, y = 30)
    titulo_pysina.place_forget()
    sub_pysina.place_forget()
    intro_btn.place_forget()
    variaveis_btn.place_forget()
    condicional_btn.place_forget()
    array_btn.place_forget()

#Função que envia para a outra aba do modulo condicionais
def proxToClick():
    returnToMenu.place(x = 40, y = 30)
    box.place(x = 40, y = 80)
    else_label.place(x = 50, y = 40)
    else_example.place(x = 50, y = 75)
    condicional_label2.place(x = 50, y = 230)
    condicional_example2.place(x = 50, y = 265)
    condicional_label3.place(x = 50, y = 445)
    confirme_btn4.place(x = 50, y = 525)
    condicional_label.place_forget()
    if_label.place_forget()
    if_example.place_forget()
    elif_label.place_forget()
    elif_example.place_forget()
    prox_btn.place_forget()
    if condicionalComplete == True:
        confirme_btn4.place_forget()

#Função que envia para a outra aba do modulo arrays
def proxToClick2():
    array_label4.place(x = 50, y = 40)
    array_example4.place(x = 50, y = 130)
    array_label5.place(x = 50, y = 200)
    array_example5.place(x = 50, y = 230)
    confirme_btn5.place(x = 50, y = 370)
    array_label.place_forget()
    array_example.place_forget()
    array_label2.place_forget()
    array_example2.place_forget()
    array_label3.place_forget()
    array_example3.place_forget()
    prox_btn2.place_forget()
    if arrayComplete == True:
        confirme_btn5.place_forget()

#Função que envia para as arrays
def array_clique():
    returnToMenu.place(x = 40, y = 30)
    array_title.place(x = 570, y = 30)
    boxArrays.place(x = 40, y = 80)
    array_label.place(x = 50, y = 40)
    array_example.place(x = 50, y = 150)
    array_label2.place(x = 50, y = 250)
    array_example2.place(x = 50, y = 300)
    array_label3.place(x = 50, y = 380)
    array_example3.place(x = 50, y = 430)
    prox_btn2.place(x = 100, y = 30)
    titulo_pysina.place_forget()
    sub_pysina.place_forget()
    intro_btn.place_forget()
    variaveis_btn.place_forget()
    condicional_btn.place_forget()
    array_btn.place_forget()

#Envia você de volta ao menu
def returnToClick():
    titulo_pysina.place(x = 70, y = 80)
    sub_pysina.place(x = 72, y = 165)
    intro_btn.place(x = 74, y = 230)

    if introComplete == True:
        variaveis_btn.place(x = 74, y = 280)

    if varComplete == True:
        condicional_btn.place(x = 74, y = 330)

    if condicionalComplete == True:
        array_btn.place(x = 74, y = 380)

    if arrayComplete == True:
        pass

    returnToMenu.place_forget()
    introducao.place_forget()
    printHello.place_forget()
    confirme_btn.place_forget()
    coment.place_forget()
    comentex.place_forget()
    coment2.place_forget()
    comentex2.place_forget()
    coment3.place_forget()
    printComent.place_forget()
    confirme_btn2.place_forget()
    variableLbl.place_forget()
    variableex.place_forget()
    variableLbl2.place_forget()
    variableex2.place_forget()
    variableLbl3.place_forget()
    acertouLabel.place_forget()
    errouLabel.place_forget()
    box.place_forget()
    variable_title.place_forget()
    coment_title.place_forget()
    intro_title.place_forget()
    janela.place_forget()
    condicional_label.place_forget()
    if_label.place_forget()
    if_example.place_forget()
    elif_label.place_forget()
    elif_example.place_forget()
    prox_btn.place_forget()
    condicional_title.place_forget()
    else_label.place_forget()
    else_example.place_forget()
    condicional_label2.place_forget()
    condicional_example2.place_forget()
    condicional_label3.place_forget()
    confirme_btn4.place_forget()
    array_title.place_forget()
    boxArrays.place_forget()
    array_label4.place_forget()
    array_example4.place_forget()
    array_label5.place_forget()
    array_example5.place_forget()
    confirme_btn5.place_forget()
    prox_btn2.place_forget()

#----------------------------------------------------- SUPORTE OBJECTS -----------------------------------------------------#

#Suporte Introdução
introducao = CTkLabel(master = box, wraplength = box_width - 90, text = "Seja bem-vindo à Introdução ao Python! Aqui, você vai adquirir os conhecimentos essenciais para iniciar sua jornada na programação utilizando essa linguagem poderosa.\n\nComeçaremos com o básico, aprendendo a imprimir uma palavra no terminal. Para isso, utilizaremos a função print(), que está disponível nativamente na biblioteca Python. Vamos Começar Escrevendo um código simples que fara o computador responder Olá Mundo no terminal, para isso digite o seguinte código:\n\nprint('Olá Mundo')", justify = LEFT, font = ("Arial", 18))
printHello = CTkEntry(master = box, placeholder_text = "Digite aqui o código", font = ("Arial", 18), height = 40, width = 300, text_color = FOREGROUND_COLOR)
confirme_btn = CTkButton(master = box, text = "Confirmar Texto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, command = confirmeClick)
intro_title = CTkLabel(master = background, text = "Introdução", justify = LEFT, font = ("Arial", 30, "bold", "italic"), text_color = FOREGROUND_COLOR)

#Suporte Comentários
coment = CTkLabel(master = box, wraplength = box_width - 90, text = "Agora vamos abordar os comentários em Python.\nVamos começar pelos comentários de linha unica que podem ser feitos ao digitar # na linha assim fazendo com que todo o texto seguinte seja transformado em comentário assim como no exemplo a seguir:", justify = LEFT, font = ("Arial", 18))
coment2 = CTkLabel(master = box, wraplength = box_width - 90, text = "Também Podemos fazer blocos de comentários utilizando do '''  ''' assim fazendo com que todo o texto presente entre as aspas seja comentado como no exemplo a seguir:", justify = LEFT, font = ("Arial", 18))
coment3 = CTkLabel(master = box, wraplength = box_width - 90, text = "Agora escreva o comentário -> Eu programo com o Pysina. E utilize o tipo ideal de comentário para uma linha.", justify = LEFT, font = ("Arial", 18))
comentex = CTkLabel(master = box, wraplength = box_width - 90, text = "#Estou estudando Python com Pysina", justify = LEFT, font = ("Arial", 18), text_color = COMENT_COLOR)
comentex2 = CTkLabel(master = box, wraplength = box_width - 90, text = "''' Configurações do Projeto\n\n 1920x1080\n\n Volume 100% '''", justify = LEFT, font = ("Arial", 18), text_color = COMENT_COLOR)
printComent = CTkEntry(master = box, placeholder_text = "Digite aqui o código", font = ("Arial", 18), height = 40, width = 300, text_color = FOREGROUND_COLOR)
confirme_btn2 = CTkButton(master = box, text = "Confirmar Texto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, command = confirmeClick2)
coment_title = CTkLabel(master = background, text = "Comentários", justify = LEFT, font = ("Arial", 30, "bold", "italic"), text_color = FOREGROUND_COLOR)

#Suporte Variáveis
#Inteiro
variableLbl = CTkLabel(master = janela.tab("Inteiro"), wraplength = box_width - 90, text = "Agora vamos abordar as Variáveis:\n\nVariável de tipo Inteiro:\nUma variável de tipo inteiro em Python é usada para armazenar valores numéricos inteiros, ou seja, números sem parte fracionária. Em Python, você pode atribuir um valor inteiro a uma variável usando a sintaxe simples de atribuição, por exemplo:", justify = LEFT, font = ("Arial", 18))
variableex = CTkLabel(master = janela.tab("Inteiro"), wraplength = box_width - 90, text = "idade = 21", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
variableLbl2 = CTkLabel(master = janela.tab("Inteiro"), wraplength = box_width - 90, text = "Neste exemplo, 'idade' é o nome da variável e 25 é o valor atribuído a ela. Em Python, não é necessário especificar o tipo de dados ao declarar uma variável, pois a linguagem é dinamicamente tipada, o que significa que o tipo de dados é inferido automaticamente pelo interpretador. Variáveis inteiras podem ser usadas em operações matemáticas, como adição, subtração, multiplicação e divisão. Por exemplo:", justify = LEFT, font = ("Arial", 18))
variableex2 = CTkLabel(master = janela.tab("Inteiro"), wraplength = box_width - 90, text = "a = 10\nb = 5\nsoma = a + b\nprint(soma)", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
variableLbl3 = CTkLabel(master = janela.tab("Inteiro"), wraplength = box_width - 90, text = "Neste caso, a variável 'soma' terá o valor 15. Além disso, as variáveis inteiras podem ser usadas em expressões lógicas e em várias outras operações em Python.", justify = LEFT, font = ("Arial", 18))
variable_title = CTkLabel(master = background, text = "Variáveis", justify = LEFT, font = ("Arial", 30, "bold", "italic"), text_color = FOREGROUND_COLOR)
#Float
variableLbl4 = CTkLabel(master = janela.tab("Float"), wraplength = box_width - 90, text = "Uma variável de tipo float em Python é usada para armazenar valores numéricos com ponto flutuante, ou seja, números que podem ter uma parte inteira e uma parte fracionária. Por exemplo, 3.14 é um número float.\n\nAssim como as variáveis inteiras, você pode atribuir um valor float a uma variável usando a sintaxe de atribuição simples:", justify = LEFT, font = ("Arial", 18))
variableex3 = CTkLabel(master = janela.tab("Float"), wraplength = box_width - 90, text = "altura = 1.75\n\n\n\n\n\n\npi = 3.14\nraio = 2.5\narea = pi * (raio ** 2)", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
variableLbl5 = CTkLabel(master = janela.tab("Float"), wraplength = box_width - 90, text = "Neste exemplo, 'altura' é o nome da variável e 1.75 é o valor atribuído a ela. Da mesma forma que as variáveis inteiras, não é necessário especificar o tipo de dados ao declarar uma variável float em Python.\n\nVariáveis float podem ser usadas em operações matemáticas, como adição, subtração, multiplicação e divisão, tanto com outras variáveis float quanto com variáveis inteiras. Por exemplo:", justify = LEFT, font = ("Arial", 18))
variableLbl6 = CTkLabel(master = janela.tab("Float"), wraplength = box_width - 90, text = "Neste caso, a variável 'area' armazenará o valor da área de um círculo com raio 2.5, calculado usando a fórmula da área do círculo\n(pi * raio^2).", justify = LEFT, font = ("Arial", 18))
#String
variableLbl7 = CTkLabel(master = janela.tab("String"), wraplength = box_width - 90, text = "Uma variável de tipo string em Python é usada para armazenar texto, ou seja, sequências de caracteres. Por exemplo, 'Olá, mundo!' é uma string.\n\nPara atribuir uma string a uma variável, você pode usar aspas simples (' '), aspas duplas, ou até mesmo aspas triplas (''' ''') para strings multilinhas:", justify = LEFT, font = ("Arial", 18))
variableex4 = CTkLabel(master = janela.tab("String"), wraplength = box_width - 90, text = "nome = 'Alice'\nmensagem = 'Bem-vindo ao mundo Python!'\nparagrafo = '''Este é um exemplo\n                     de uma string multilinha.'''", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
variableLbl8 = CTkLabel(master = janela.tab("String"), wraplength = box_width - 90, text = "Nestes exemplos, 'nome', 'mensagem' e 'paragrafo' são os nomes das variáveis, e as strings 'Alice', 'Bem-vindo ao mundo Python!' e o parágrafo de texto multilinha são os valores atribuídos a elas.\n\nVariáveis do tipo string podem ser manipuladas de diversas formas em Python. Você pode concatenar strings, acessar caracteres individuais, dividir uma string em substrings, substituir partes da string e muito mais, utilizando diversos métodos e operadores disponíveis na linguagem.\n\nPor exemplo, para concatenar duas strings:\n\n\n\n\nNeste caso, a variável 'nome_completo' conterá a string 'João Silva'.", justify = LEFT, font = ("Arial", 18))
variableex5 = CTkLabel(master = janela.tab("String"), wraplength = box_width - 90, text = "nome = 'João'\nsobrenome = 'Silva'\nnome_completo = nome + " " + sobrenome", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
#Booleano
variableLbl9 = CTkLabel(master = janela.tab("Booleano"), wraplength = box_width - 90, text = "Uma variável de tipo booleano em Python é usada para armazenar valores lógicos, ou seja, valores que representam verdadeiro ou falso. Em Python, os valores booleanos são representados pelos literais True e False.\n\nPor exemplo, você pode atribuir um valor booleano a uma variável da seguinte forma:", justify = LEFT, font = ("Arial", 18))
variableex6 = CTkLabel(master = janela.tab("Booleano"), wraplength = box_width - 90, text = "temperatura_alta = True", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
variableLbl10 = CTkLabel(master = janela.tab("Booleano"), wraplength = box_width - 90, text = "Neste exemplo, 'temperatura_alta' é o nome da variável e True é o valor atribuído a ela, indicando que a temperatura está alta.\n\nVariáveis booleanas são frequentemente utilizadas em expressões condicionais e em operações lógicas, como em estruturas de controle de fluxo (if-else), loops e expressões booleanas mais complexas.\n\nPor exemplo, em uma estrutura condicional:", justify = LEFT, font = ("Arial", 18))
variableex7 = CTkLabel(master = janela.tab("Booleano"), wraplength = box_width - 90, text = "temperatura_alta = True\nif temperatura_alta:\n    print('Está quente lá fora!')\nelse:\n    print('Está frio lá fora!')", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
variableLbl11 = CTkLabel(master = janela.tab("Booleano"), wraplength = box_width - 90, text = "Neste caso, se a variável 'temperatura_alta' for True, será impressa a mensagem 'Está quente lá fora!', caso contrário, será impressa a mensagem 'Está frio lá fora!'.\nVariáveis booleanas também são frequentemente usadas para controlar o fluxo do programa, determinando se certas ações devem ou não ser realizadas com base em condições lógicas.", justify = LEFT, font = ("Arial", 18))
#Constante
variableLbl12 = CTkLabel(master = janela.tab("Constante"), wraplength = box_width - 90, text = "Em Python, não há um tipo de dado 'constante' nativo como em algumas outras linguagens de programação, onde você pode declarar uma variável como constante e garantir que seu valor não seja alterado durante a execução do programa. No entanto, é uma prática comum usar convenções de nomenclatura para indicar que uma variável é tratada como constante, ou seja, seu valor não deve ser alterado após a sua atribuição inicial.\n\nPor convenção, em Python, os programadores costumam nomear variáveis que devem ser tratadas como constantes em letras maiúsculas, separando palavras com sublinhados, seguindo o padrão conhecido como 'snake_case'.\n\nPor exemplo:", justify = LEFT, font = ("Arial", 18))
variableex8 = CTkLabel(master = janela.tab("Constante"), wraplength = box_width - 90, text = "TAXA_JUROS = 0.05\nDIAS_SEMANA = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
variableLbl13 = CTkLabel(master = janela.tab("Constante"), wraplength = box_width - 90, text = "Embora essas variáveis não sejam verdadeiramente constantes (pois Python não tem um mecanismo embutido para definir constantes), a convenção de nomenclatura em letras maiúsculas indica aos outros programadores (e a você mesmo) que essas variáveis não devem ser modificadas durante a execução do programa.\n\nAlém disso, se você realmente deseja garantir que uma variável não seja alterada, você pode usar técnicas de programação defensiva, como encapsular seu código em funções ou classes e evitar modificar diretamente essas variáveis fora do escopo apropriado.", justify = LEFT, font = ("Arial", 18))
confirme_btn3 = CTkButton(master = janela.tab("Constante"), text = "Próximo Assunto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, command = confirmeClick3)

#Suporte Condicionais
condicional_title = CTkLabel(master = background, text = "Condicionais", justify = LEFT, font = ("Arial", 30, "bold", "italic"), text_color = FOREGROUND_COLOR)
condicional_label = CTkLabel(master = box, wraplength = box_width - 90, text = "As condicionais em Python são usadas para controlar o fluxo de um programa com base em determinadas condições. Elas permitem que você execute diferentes blocos de código dependendo se uma condição é verdadeira ou falsa. As condicionais mais comuns em Python são expressas por meio das instruções if, elif (abreviação de 'else if') e else.", justify = LEFT, font = ("Arial", 18))
if_label = CTkLabel(master = box, wraplength = box_width - 90, text = "1. if: A instrução if verifica se uma condição é verdadeira. Se a condição for verdadeira, o bloco de código dentro do if é executado.", justify = LEFT, font = ("Arial", 18))
if_example = CTkLabel(master = box, wraplength = box_width - 90, text = "idade = 18\nif idade >= 18:\n    print('Você é maior de idade.')", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
elif_label = CTkLabel(master = box, wraplength = box_width - 90, text = "2. elif: A instrução elif é usada para verificar múltiplas condições após a primeira if. Se a condição associada a um elif for verdadeira, o bloco de código correspondente a esse elif é executado.", justify = LEFT, font = ("Arial", 18))
elif_example = CTkLabel(master = box, wraplength = box_width - 90, text = "nota = 75\n\nif nota >= 90:\n    print('Aprovado com nota A.')\nelif nota >= 80:\n    print('Aprovado com nota B.')\nelif nota >= 70:\n    print('Aprovado com nota C.')\nelse:\n    print('Reprovado.')", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
else_label = CTkLabel(master = box, wraplength = box_width - 90, text = "3. else: A instrução else é usada para executar um bloco de código quando nenhuma das condições associadas a if ou elif é verdadeira.", justify = LEFT, font = ("Arial", 18))
else_example = CTkLabel(master = box, wraplength = box_width - 90, text = "numero = 7\n\nif numero % 2 == 0:\n    print('O número é par.')\nelse:\n    print('O número é ímpar.')", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
condicional_label2 = CTkLabel(master = box, wraplength = box_width - 90, text = "As condicionais em Python também podem ser aninhadas, permitindo a criação de estruturas condicionais mais complexas. Por exemplo:", justify = LEFT, font = ("Arial", 18))
condicional_example2 = CTkLabel(master = box, wraplength = box_width - 90, text = "idade = 21\n\nif idade >= 18:\n    print('Você é maior de idade.')\n    if idade >= 21:\n        print('E pode beber nos EUA.')\nelse:\n    print('Você é menor de idade.')", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
condicional_label3 = CTkLabel(master = box, wraplength = box_width - 90, text = "É importante entender que a indentação é fundamental em Python para indicar os blocos de código associados a cada condicional. Cada bloco de código deve ser indentado com um número consistente de espaços ou tabulações para garantir que o interpretador Python interprete corretamente a estrutura do código.", justify = LEFT, font = ("Arial", 18))
prox_btn = CTkButton(master = background, text = ">", font = ("Arial", 25, "bold"), height = 30, width = 40, corner_radius = 36, command = proxToClick)
confirme_btn4 = CTkButton(master = box, text = "Próximo Assunto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, command = confirmeClick4)

#Suporte Arrays
array_title = CTkLabel(master = background, text = "Arrays", justify = LEFT, font = ("Arial", 30, "bold", "italic"), text_color = FOREGROUND_COLOR)
array_label = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "Em Python, o conceito de 'arrays' é geralmente abordado por meio de listas. As listas são estruturas de dados que podem armazenar uma coleção ordenada de itens, onde cada item pode ser de um tipo de dado diferente, como números, strings, booleanos, outras listas e assim por diante. As listas são muito versáteis e flexíveis, permitindo adicionar, remover e modificar elementos facilmente.\n\nPara criar uma lista em Python, você pode utilizar colchetes [ ] e separar os elementos por vírgulas. Por exemplo:", justify = LEFT, font = ("Arial", 18))
array_example = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "lista_numeros = [1, 2, 3, 4, 5]\nlista_strings = ['maçã', 'banana', 'laranja']\nlista_mista = [10, 'python', True, 3.14]", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
array_label2 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "Você pode acessar elementos individuais de uma lista através de seu índice, que começa em 0 para o primeiro elemento, 1 para o segundo elemento, e assim por diante. Por exemplo:", justify = LEFT, font = ("Arial", 18))
array_example2 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "fruta = lista_strings[0]  # Acessando o primeiro elemento da lista de strings\nprint(fruta)  # Saída: maçã", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
array_label3 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "Além disso, as listas em Python suportam indexação negativa, o que significa que você pode acessar os elementos a partir do final da lista. Por exemplo, -1 representa o último elemento, -2 representa o penúltimo elemento, e assim por diante.", justify = LEFT, font = ("Arial", 18))
array_example3 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "ultima_fruta = lista_strings[-1]  # Acessando o último elemento da lista de strings\nprint(ultima_fruta)  # Saída: laranja", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
array_label4 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "As listas em Python são mutáveis, o que significa que você pode modificar seus elementos, adicionar novos elementos, remover elementos existentes e muito mais.\n\nPor exemplo, para adicionar um novo elemento à lista, você pode usar o método append( ):", justify = LEFT, font = ("Arial", 18))
array_example4 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "lista_numeros.append(6)  # Adicionando o número 6 à lista de números\nprint(lista_numeros)  # Saída: [1, 2, 3, 4, 5, 6]", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
array_label5 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "Para remover um elemento da lista, você pode usar os métodos remove( ) ou pop( ):", justify = LEFT, font = ("Arial", 18))
array_example5 = CTkLabel(master = boxArrays, wraplength = box_width - 90, text = "lista_strings.remove('banana')  # Removendo a string 'banana' da lista de strings\nprint(lista_strings)  # Saída: ['maçã', 'laranja']\n\nelemento_removido = lista_numeros.pop(0)  # Removendo o primeiro elemento da lista de números\nprint(elemento_removido)  # Saída: 1\nprint(lista_numeros)  # Saída: [2, 3, 4, 5, 6]", justify = LEFT, font = ("Arial", 18), text_color = PRESSIONED_COLOR)
prox_btn2 = CTkButton(master = background, text = ">", font = ("Arial", 25, "bold"), height = 30, width = 40, corner_radius = 36, command = proxToClick2)
confirme_btn5 = CTkButton(master = boxArrays, text = "Próximo Assunto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, command = confirmeClick5)

#Suporte Menu Return
returnToMenu = CTkButton(master = background, text = "<", font = ("Arial", 25, "bold"), height = 30, width = 40, corner_radius = 36, command = returnToClick)

#----------------------------------------------------- CRIANDO ELEMENTOS -----------------------------------------------------#

#Tela de Login
CrieSuaConta = CTkLabel(master = boxLogin, text = "Entre ou Registre-se", font = ("Arial", 40, "bold"), text_color = "#2CC985")
email = CTkEntry(master = boxLogin, placeholder_text = "Digite seu Email", font = ("Arial", 18), height = 40, width = 400, text_color = FOREGROUND_COLOR)
senha = CTkEntry(master = boxLogin, placeholder_text = "Digite sua Senha", font = ("Arial", 18), show = ("*"), height = 40, width = 400, text_color = FOREGROUND_COLOR)
exibirSenha = CTkSwitch(master = boxLogin, text = "Exibir Senha", font = ("Arial", 15), command = switch_event, variable = switch_var, onvalue = "on", offvalue = "off")
login_btn = CTkButton(master = boxLogin, text = "Entrar", font = ("Arial", 25, "bold"), height = 40, width = 400, corner_radius = 15, command = entrar_clique)
registre_btn = CTkButton(master = boxLogin, text = "Registre-se", font = ("Arial", 20, "bold"), height = 20, width = 210, corner_radius = 32, fg_color = COMENT_COLOR, hover_color = "#566081", command = registre_clique)
naoTemConta = CTkLabel(master = boxLogin, text = "Se não tem uma conta", font = ("Arial", 18), text_color = FOREGROUND_COLOR)
#Tela de Registro
CrieSuaContaR = CTkLabel(master = boxLogin, text = "Registre-se", font = ("Arial", 40, "bold"), text_color = "#2CC985")
nomeUsuario = CTkEntry(master = boxLogin, placeholder_text = "Digite seu Nome de Usuário", font = ("Arial", 18), height = 40, width = 400, text_color = FOREGROUND_COLOR)
emailcad = CTkEntry(master = boxLogin, placeholder_text = "Digite seu Email", font = ("Arial", 18), height = 40, width = 400, text_color = FOREGROUND_COLOR)
senhacad = CTkEntry(master = boxLogin, placeholder_text = "Digite sua Senha", font = ("Arial", 18), show = ("*"), height = 40, width = 400, text_color = FOREGROUND_COLOR)
repitaSenha = CTkEntry(master = boxLogin, placeholder_text = "Repita sua Senha", font = ("Arial", 18), show = ("*"), height = 40, width = 400, text_color = FOREGROUND_COLOR)
criarConta_btn = CTkButton(master = boxLogin, text = "Entrar", font = ("Arial", 25, "bold"), height = 40, width = 400, corner_radius = 15, command = criarConta_clique)
returnToLogin_btn = CTkButton(master = boxLogin, text = "Login", font = ("Arial", 25, "bold"), height = 40, width = 400, corner_radius = 15, fg_color = COMENT_COLOR, hover_color = "#566081", command = returnToLogin_clique)

#------------------------------------------------------------------------------------------------------------------------------#

#Criando o Titulo do APP
titulo_pysina = CTkLabel(master = background, text = "Pysina", font = ("Arial", 70, "bold"))

#Criando o SubTitulo do APP
sub_pysina = CTkLabel(master = background, text = "O Aplicativo que ensina Python para você", font = ("Arial", 20), text_color = "#716F6C")

#Criando o Botão de Entrada Para a Introdução ao Python
intro_btn = CTkButton(master = background, text = "Introdução ao Python", font = ("Arial", 25), height = 40, width = 300, corner_radius = 32, command = intro_clique)

#Criando o Botão de Entrada Para Variáveis
variaveis_btn = CTkButton(master = background, text = "Variáveis", font = ("Arial", 25), height = 40, width = 300, corner_radius = 32, command = variable_clique)

#Criando o Botão de Entrada Para Condicionais
condicional_btn = CTkButton(master = background, text = "Condicionais", font = ("Arial", 25), height = 40, width = 300, corner_radius = 32, command = condicional_clique)

#Criando o Botão de Entrada Para Arrays
array_btn = CTkButton(master = background, text = "Arrays", font = ("Arial", 25), height = 40, width = 300, corner_radius = 32, command = array_clique)

#----------------------------------------------------- POSICIONANDO ELEMENTOS -----------------------------------------------------#

#Posicionando o Box de Login e Cadastro
boxLogin.place(x = 770, y = 11)
CrieSuaConta.place(x = 50, y = 150)
email.place(x = 50, y = 260)
senha.place(x = 50, y = 310)
exibirSenha.place(x = 50, y = 360)
login_btn.place(x = 50, y = 410)
naoTemConta.place(x = 55, y = 465)
registre_btn.place(x = 240, y = 460)

#----------------------------------------------------- MANTENDO A JANELA ABERTA -----------------------------------------------------#

#Mantendo a Janela Aberta
pysina.mainloop()
