from customtkinter import *

#Criando a Janela
pysina = CTk()

#Definindo as Proporções
win_width, win_height = 1280, 720
pysina.geometry("{}x{}".format(win_width, win_height))

#Definindo o Nome da Aplicação
pysina.title("Pysina")

#Definindo o Tema da Janela
set_appearance_mode("#282A36")

introComplete = False
varComplete = False

#----------------------------------------------------- PALETA DE CORES DO APP -----------------------------------------------------#

BACKGROUND_COLOR = "#282A36"
BOX_COLOR = "#44475A"
COMENT_COLOR = "#6272A4"
FOREGROUND_COLOR = "#F8F8F2"
BUTTON_COLOR = "#309A7B"
PRESSIONED_COLOR = "#64895C"
ORANGE_COLOR = "#FFB86C"

#----------------------------------------------------- CRIANDO JANELAS -----------------------------------------------------#

background = CTkFrame(master = pysina, fg_color = BACKGROUND_COLOR, width = 1920, height = 1080)
background.place(x = 0, y = 0)
box = CTkFrame(master = background, fg_color = BOX_COLOR, width = 1200, height = 600, border_color = BACKGROUND_COLOR, border_width = 2)
box_width, box_height = 1200, 600
janela = CTkTabview(master = background, fg_color = BOX_COLOR, width = 1200, height = 600, border_color = BACKGROUND_COLOR, border_width = 2,)
janela.add("Inteiro")
janela.add("Float")
janela.add("String")
janela.add("Booleano")
janela.add("Constante")

#----------------------------------------------------- FUNÇÕES -----------------------------------------------------#

#Texto de suporte para Certo e Errado
acertouLabel = CTkLabel(master = box, wraplength = box_width - 90, text = "Acertou vamos para o próximo tópico a ser abordado", justify = LEFT, font = ("Arial", 18), text_color = BUTTON_COLOR)
errouLabel = CTkLabel(master = box, wraplength = box_width - 90, text = "Isso não está correto. Tente novamente", justify = LEFT, font = ("Arial", 18), text_color = ORANGE_COLOR)

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

def confirmeClick3():
    global varComplete
    varComplete = True
    variaveis_btn.configure(fg_color = COMENT_COLOR, hover_color = "#566081")
    returnToClick()

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
    if varComplete == True:
        confirme_btn3.place_forget()

def condicional_clique():
    returnToMenu.place(x = 40, y = 30)
    titulo_pysina.place_forget()
    sub_pysina.place_forget()
    intro_btn.place_forget()
    variaveis_btn.place_forget()
    condicional_btn.place_forget()

#Envia você de volta ao menu
def returnToClick():
    titulo_pysina.place(x = 70, y = 80)
    sub_pysina.place(x = 72, y = 165)
    intro_btn.place(x = 74, y = 230)

    if introComplete == True:
        variaveis_btn.place(x = 74, y = 280)

    if varComplete == True:
        condicional_btn.place(x = 74, y = 330)

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

#----------------------------------------------------- SUPORTE OBJECTS -----------------------------------------------------#

#Suporte Introdução
introducao = CTkLabel(master = box, wraplength = box_width - 90, text = "Seja bem-vindo à Introdução ao Python! Aqui, você vai adquirir os conhecimentos essenciais para iniciar sua jornada na programação utilizando essa linguagem poderosa.\n\nComeçaremos com o básico, aprendendo a imprimir uma palavra no terminal. Para isso, utilizaremos a função print(), que está disponível nativamente na biblioteca Python. Vamos Começar Escrevendo um código simples que fara o computador responder Olá Mundo no terminal, para isso digite o seguinte código:\n\nprint('Olá Mundo')", justify = LEFT, font = ("Arial", 18))
printHello = CTkEntry(master = box, placeholder_text = "Digite aqui o código", font = ("Arial", 18), height = 40, width = 300, text_color = FOREGROUND_COLOR)
confirme_btn = CTkButton(master = box, text = "Confirmar Texto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, fg_color = BUTTON_COLOR, hover_color = PRESSIONED_COLOR, command = confirmeClick)
intro_title = CTkLabel(master = background, text = "Introdução", justify = LEFT, font = ("Arial", 30, "bold", "italic"), text_color = FOREGROUND_COLOR)

#Suporte Comentários
coment = CTkLabel(master = box, wraplength = box_width - 90, text = "Agora vamos abordar os comentários em Python.\nVamos começar pelos comentários de linha unica que podem ser feitos ao digitar # na linha assim fazendo com que todo o texto seguinte seja transformado em comentário assim como no exemplo a seguir:", justify = LEFT, font = ("Arial", 18))
coment2 = CTkLabel(master = box, wraplength = box_width - 90, text = "Também Podemos fazer blocos de comentários utilizando do '''  ''' assim fazendo com que todo o texto presente entre as aspas seja comentado como no exemplo a seguir:", justify = LEFT, font = ("Arial", 18))
coment3 = CTkLabel(master = box, wraplength = box_width - 90, text = "Agora escreva o comentário -> Eu programo com o Pysina. E utilize o tipo ideal de comentário para uma linha.", justify = LEFT, font = ("Arial", 18))
comentex = CTkLabel(master = box, wraplength = box_width - 90, text = "#Estou estudando Python com Pysina", justify = LEFT, font = ("Arial", 18), text_color = COMENT_COLOR)
comentex2 = CTkLabel(master = box, wraplength = box_width - 90, text = "''' Configurações do Projeto\n\n 1920x1080\n\n Volume 100% '''", justify = LEFT, font = ("Arial", 18), text_color = COMENT_COLOR)
printComent = CTkEntry(master = box, placeholder_text = "Digite aqui o código", font = ("Arial", 18), height = 40, width = 300, text_color = FOREGROUND_COLOR)
confirme_btn2 = CTkButton(master = box, text = "Confirmar Texto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, fg_color = BUTTON_COLOR, hover_color = PRESSIONED_COLOR, command = confirmeClick2)
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
confirme_btn3 = CTkButton(master = janela.tab("Constante"), text = "Próximo Assunto", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, fg_color = BUTTON_COLOR, hover_color = PRESSIONED_COLOR, command = confirmeClick3)

#Suporte Menu Return
returnToMenu = CTkButton(master = background, text = "<", font = ("Arial", 25, "bold"), height = 30, width = 40, corner_radius = 36, fg_color = BUTTON_COLOR, hover_color = PRESSIONED_COLOR, command = returnToClick)

#----------------------------------------------------- CRIANDO ELEMENTOS -----------------------------------------------------#

#Criando o Titulo do APP
titulo_pysina = CTkLabel(master = background, text = "Pysina", font = ("Arial", 70, "bold"))

#Criando o SubTitulo do APP
sub_pysina = CTkLabel(master = background, text = "O Aplicativo que ensina Python para você", font = ("Arial", 20), text_color = "#716F6C")

#Criando o Botão de Entrada Para a Introdução ao Python
intro_btn = CTkButton(master = background, text = "Introdução ao Python", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, fg_color = BUTTON_COLOR, hover_color = PRESSIONED_COLOR, command = intro_clique)

#Criando o Botão de Entrada Para Variáveis
variaveis_btn = CTkButton(master = background, text = "Variáveis", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, fg_color = BUTTON_COLOR, hover_color = PRESSIONED_COLOR, command = variable_clique)

#Criando o Botão de Entrada Para Variáveis
condicional_btn = CTkButton(master = background, text = "Condicionais", font = ("Arial", 25), height = 40, width = 40, corner_radius = 32, fg_color = BUTTON_COLOR, hover_color = PRESSIONED_COLOR, command = condicional_clique)

#----------------------------------------------------- POSICIONANDO ELEMENTOS -----------------------------------------------------#

#Posicionando o Titulo do APP
titulo_pysina.place(x = 70, y = 80)

#Posicionando o SubTitulo do APP
sub_pysina.place(x = 72, y = 165)

#Posicionando o Botão de Introdução
intro_btn.place(x = 74, y = 230)

#----------------------------------------------------- MANTENDO A JANELA ABERTA -----------------------------------------------------#

#Mantendo a Janela Aberta
pysina.mainloop()