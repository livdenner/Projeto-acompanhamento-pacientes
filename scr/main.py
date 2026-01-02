import customtkinter #importa a biblioteca customtkinter para criar as janelas 
import json # importa a biblioteca json (é uma biblioteca de dicionário)


def informacao_paciente(nome_paciente): # função c as informações do paciente para chamar no botão
    janela3 = customtkinter.CTkToplevel(janela) #cria uma aba de janela nova, ligada a janela principal(janela)
    janela3.geometry("700x400") #pra formatar o tamanho bonitinho
    texto3 = customtkinter.CTkLabel(janela3, text='Informações do Paciente') #aqui é um widgte bonitinho, um textinho pra colocar na janela
    texto3.pack(padx=10, pady=10) #aqui é a posição do widget
    
    with open('pacientes.json', 'r') as arquivo:   #abrir o arquivo json (o r é de read, leitura ) >> se o arquivo não existir vai dar erro
        pacientes = json.load(arquivo) # vai abrir o arquivo (no modo leitura) e armazenar na variável pacientes
    
    if nome_paciente in pacientes:  #se o nome do paciente tiver no arquivo que agora ta armazenado na variável ´pacientes (que é um dicionário)
        info = pacientes[nome_paciente] #SE tiver dentro, a variável info recebe as informações do nome que tá sendo procurado, no caso, o paciente procurado
        for chave, valor in info.items(): #para cada chave e valor dentro de info (que recebeu as informações do paciente e virou dicionario):
            texto = customtkinter.CTkLabel(janela3, text=f'{chave}: {valor}') #criou um widget pra mostrar todas as chaves e informações do dicionário, tipo nome : kézia
            texto.pack(padx=10, pady=5) #configurações do widget, onde vai mostrar na tela 
    else:
        texto = customtkinter.CTkLabel(janela3, text='Paciente não encontrado.') # no caso, se n tiver dentro mostra isso, q n foi encontrado
        texto.pack(padx=10, pady=5) #configuração do widget


def informacao_profissional(email_prof, senha_prof): #função para informação do profissional
    
    #usuário e senha padrão para login
    username_padrao = "Clínicaaba@gmail.com"
    senha_padrao = "abaImersão#"

    #se o usuário e senha digitados forem iguais aos pré estabelecidos ai libera a entrada
    if email_prof == username_padrao and senha_prof == senha_padrao:
      
      janela5 = customtkinter.CTkToplevel(janela) #criação de nova janela p informação do profissa caso o login seja realizado
      janela5.geometry("700x400") #formatando a nova janela
      texto3 = customtkinter.CTkLabel(janela5, text='Informações do Profissional') #widget de texto na janela
      texto3.pack(padx=10, pady=10) #formatação do widget

      nomeparabuscar = customtkinter.CTkEntry(janela5, placeholder_text="Nome do paciente:") # colocar o nome do paciente que vai ser buscado, esse placeholder é tipo um input
      nomeparabuscar.pack(padx=10, pady=10) #a configuração do placeholder
      botao5 = customtkinter.CTkButton(janela5, text='Buscar', command=lambda: buscar_paciente(nomeparabuscar.get(), janela5)) #botãozinho c comando p buscar o paciente quando apertado, acionando a função lambda
      botao5.pack(padx=10, pady=10) #configuração do botão
    
      adicionarpaciente = customtkinter.CTkButton(janela5, text='Adicionar Paciente', command=adicionar_paciente) #botãozinho quando clicado aciona a função adicionar paciente
      adicionarpaciente.pack(padx=10, pady=10) #configuração do botaozinho
    
    
    else: #se o usuario e senha digitados n forem iguais aos pre estabelecidos mostra isso : 
        customtkinter.CTkLabel(janela, text='Usuário ou senha incorretos.').pack(padx=10, pady=10) #pack = configuração da janela
    


 #função de buscar paciente que vai ser colocada no botaozinho da informação do profissional
def buscar_paciente(nome_paciente, janela_atual): 
    with open('pacientes.json', 'r') as arquivo: #abrir o arquivo json (o r é de read, leitura ) >> se o arquivo não existir vai dar erro
        pacientes = json.load(arquivo) # vai abrir o arquivo (no modo leitura) e armazenar na variável pacientes
    
    for widget in janela_atual.winfo_children(): #vai atualizar a interface, "apagando" qualquer resultado anterior, por exemplo, se outro paciente foi buscado, p poder buscar o novo
        #esse winfo_children é uma função do próprio tkinter que chama todos os widgets dentro do widget pai (janela)
        if isinstance(widget, customtkinter.CTkLabel) and widget.cget("text").startswith("Resultado"):
            widget.destroy()
    
    if nome_paciente in pacientes: #chehcar se o paciente ta salvo no arquivo
        info = pacientes[nome_paciente]
        resultado = f'Resultado para {nome_paciente}: ' + ", ".join([f'\n {chave}: {valor}' for chave, valor in info.items()]) #se tiver manda as infos, igual previamente
    else:
        resultado = 'Paciente não encontrado.' # se n tiver mostra q n foi encontrado
    
    # p mostrar a variável resultado, transformando ela em widget
    resultado_label = customtkinter.CTkLabel(janela_atual, text=resultado)
    resultado_label.pack(padx=10, pady=10)


# função p adicionar paciente q vai ser acionadsa no botaozinho
def adicionar_paciente():

    # cria nova janela para adicionar as informações do novo paciente
    janela_adicionar = customtkinter.CTkToplevel(janela)
    janela_adicionar.geometry("700x400") #configuracao
    janela_adicionar.title("Adicionar Paciente") #titulo
    
    # campos de entrada de dados do paciente
    campos = ['Email do Responsável','CPF','Nome', 'Data','Idade', 
              'Habilidades de Atenção', 'Habilidades de Imitação',
              'Linguagem Receptiva', 'Linguagem Expressiva', 
              'Habilidades Pré-acadêmicas', 'Comportamento',
              'Observações', 'Jogo recomendado'
              ]
    
    # dicionário  vazio  para armazenar as entradas de texto associadas a cada campo
    entradas = {}
 
    # loop para criar os campos de entrada e rótulos correspondentes na janela
    for campo in campos:
        frame = customtkinter.CTkFrame(janela_adicionar)  # cria um frame q é tipo um contêiner que pode armazenar outros widgets
        frame.pack(padx=10, pady=5, fill=customtkinter.BOTH) #essa ultima informacao é p expandir verticalmente e horizontalmente 

        label = customtkinter.CTkLabel(frame, text=campo)
        label.pack(side=customtkinter.LEFT, padx=5, pady=5)
        
        entrada = customtkinter.CTkEntry(frame)
        entrada.pack(side=customtkinter.RIGHT, padx=5, pady=5, fill=customtkinter.X, expand=True)
        
        entradas[campo.lower()] = entrada
    entradas['senha'] = entradas['cpf'] #senha do paciente p login == cpf
    botao_salvar = customtkinter.CTkButton(janela_adicionar, text='Salvar', command=lambda: salvar_paciente(entradas))
    botao_salvar.pack(padx=10, pady=10)


def salvar_paciente(entradas):  # salvar as informações do paciente no arquivo
    paciente = {campo: entradas[campo].get() for campo in entradas} #para cada chave de campo acessa o objeto em entrada e preenche

    with open('pacientes.json', 'r') as arquivo:
        pacientes = json.load(arquivo)
    
    pacientes[paciente['email do responsável']] = paciente #  essa linha adiciona ou atualiza a entrada no dicionário pacientes usando o e-mail do responsável como chave, e as informações completas do paciente como valor.

    with open('pacientes.json', 'w') as arquivo:# vai abrir o arquivo no modo de escrita (write em ingles)
        #o with é pra fechar esse arquivo arquivo depois de executar o código
        json.dump(pacientes, arquivo)  # vai transformar o arquivo pacientes em string e jogar no arquivo inicial (arquivo)
    
    customtkinter.CTkLabel(janela, text='Paciente adicionado com sucesso!').pack(padx=10, pady=10)


def checarjson():
    try:
        with open('pacientes.json', 'r') as arquivo:
            json.load(arquivo)
    except FileNotFoundError: #vai ocorrer quando o arquivo n for encontrado
        with open('pacientes.json', 'w') as arquivo: #abre no modo de escrita, se o arquivo n exisir vai ser criaod
            json.dump({}, arquivo) #cria um arquivo json vazio p armazenar dado de paciente


def login_profissional(): #funcao p login do profissa
    
    janela4 = customtkinter.CTkToplevel(janela) #cria nova janela
    janela4.geometry("700x400") #configuração
    janela4.title("Login Profissional") #titulo
    email_prof = customtkinter.CTkEntry(janela4, placeholder_text="Seu e-mail:") #caixa de entrada, tipo input, pro profissa digitar
    email_prof.pack(padx=10, pady=10) #configuração pra onde a caixa vai ficar

    senha_prof = customtkinter.CTkEntry(janela4, placeholder_text="Sua senha:", show="*") #caixa de entrada, tipo input pra senha, o show * é p n mostrar a senha
    senha_prof.pack(padx=10, pady=10) #configuracao
    botao4 = customtkinter.CTkButton(janela4, text='Continuar', command=lambda: informacao_profissional(email_prof.get(), senha_prof.get())) # botão p executar funcao, chama a função com os valores inseridos de argumento, p ver se deixa entrar ou n
    botao4.pack(padx=10, pady=10) #configuracao



def recomendacao_jogos(): #botão de recomendação de jogo q fica na aba de login, a funcao vai ser acionada quando clicarem no botao
    janelajogos = customtkinter.CTkToplevel(janela) # criando nova janela
    janelajogos.geometry("700x400") #configuração  
    janelajogos.title("Recomendação de jogos") #título

    informacao_jogos = customtkinter.CTkLabel(janelajogos, text= "Recomendações de jogos") #widget de texto p aparecer na tela
    informacao_jogos.pack(padx=10,pady=10) #configuracao widget
    
    botaojogo1 = customtkinter.CTkButton(janelajogos, text='Reduzir estresse mental', command=estresse_mental) #esses botao ai e pra ir pra aba de jogo q vai ser acionada a função de cada jogo
    botaojogo1.pack(padx=10,pady=10) #configuracao
    
    botaojogo2 = customtkinter.CTkButton(janelajogos, text='Exercício de estimulação', command = exercicio_estimulacao) #mesma coisa do botao 1 
    botaojogo2.pack(padx=10,pady=10) # configuração
    
    botaojogo3 = customtkinter.CTkButton(janelajogos, text='Prova de memorização visual', command=memorizacao_visual) #msm coisa do outro botao
    botaojogo3.pack(padx=10,pady=10) # configuraçao
    
    botaojogo4 = customtkinter.CTkButton(janelajogos, text='Complementação de desenhos', command=complentacao_jogos) # msm coisa
    botaojogo4.pack(padx=10,pady=10) # configuracao
    
    botaojogo5 = customtkinter.CTkButton(janelajogos, text='Prova de análise e síntese', command=analise_sintese)
    botaojogo5.pack(padx=10,pady=10)

def estresse_mental(): #função jogo p colocar no botao
    janelamental = customtkinter.CTkToplevel(janela)
    janelamental.geometry('700x400')
    janelamental.title("Jogo para estresse mental")
    
    labelmental = customtkinter.CTkLabel(janelamental, text = 'Indicado: Indicados para pacientes diagnosticados com Transtorno do Déficit de Atenção com Hiperatividade (TDAH), Transtorno de Ansiedade e outros. ')
    labelmental.pack(padx=10,pady=10)
    
    labelmental2 = customtkinter.CTkLabel(janelamental, text = 'Benefícios: Regula os níveis de ansiedade, aprimora as habilidades sociais e emocionais, melhora a qualidade do sono e criatividade')
    labelmental2.pack(padx=10,pady=10)
    
    labelmental3 = customtkinter.CTkLabel(janelamental, text = ' EXEMPLO:')
    labelmental3.pack(padx=10,pady=10)
    
    labelmental4 = customtkinter.CTkLabel(janelamental, text = 'Encha uma garrafa ou pote transparente com água e glitter.\n Feche bem e mexa o pote para o glitter se agitar\n. Diga à criança que nossos pensamentos funcionam como o glitter: \n se nos agitamos e perdemos a calma, os pensamentos se agitam e ficam desorganizados. \n Mas, à medida que paramos, respiramos e nos acalmamos, mantendo o foco e a atenção, os pensamentos vão se organizando novamente.')
    labelmental4.pack(padx=10,pady=10)

def exercicio_estimulacao(): #função jogo p colocar no botao
    janelaestimulo = customtkinter.CTkToplevel(janela)
    janelaestimulo.geometry('700x400')
    janelaestimulo.title("Jogo de exercício de estimulação")
    
    labelestimulo = customtkinter.CTkLabel(janelaestimulo, text = 'Indicados para: Aqueles com dificuldades de escrita, coordenação visomotora e coordenação motora fina e outros.')
    labelestimulo.pack(padx=10,pady=10)
    
    labelestimulo1 = customtkinter.CTkLabel (janelaestimulo, text = 'Benefícios: Ajudam na coordenação dos movimentos, coordenação olho-mão e destreza; \n Também adquirem-se noção espacial, motricidade fina, orientação temporal e outros.')
    labelestimulo1.pack(padx=10,pady=10)
    
    labelestimulo2 = customtkinter.CTkLabel(janelaestimulo, text = '1. PROVA DE RECORTE PARA CRIANÇAS PEQUENAS\nMaterial: 3 folhas da prova, tesoura e cronômetro.\nIdade ideal: De 5 à 6 anos\nO que se observa: mão usada para recortar, qualidade do recorte, tempo de cada recorte, desvios da linha.\nInstrua (ou fale): "Você vai recortar esse caminho sem tocar as bordas, nem sair do caminho, assim... veja"\n"Agora continue e pare aqui".\nQuando Usar: Dificuldades de escrita, coordenação visomotora e coordenação motora fina.')
    labelestimulo2.pack(padx=10,pady=10)
    


def memorizacao_visual(): #função jogo p colocar no botao 
    janelamemoria = customtkinter.CTkToplevel(janela)
    janelamemoria.geometry('700x400')
    janelamemoria.title("Jogo de memorização visual")
    
    labelmemoria = customtkinter.CTkLabel (janelamemoria, text = ' EXPLORAÇÃO DA AGNOSIA VISUAL')
    labelmemoria.pack(padx=10,pady=10)
    
    labelmemoria2 = customtkinter.CTkLabel(janelamemoria, text = 'Material: 1 prancha com os desenhos (não obrigatório), 1 folha de papel ofício, lápis preto, borracha.\n Idade ideal: A partir de 6 anos.\n O que se observa: preensão do instrumento, qualidade do desenho, distribuição dos elementos na página. \n Instrua (ou fale): “Copie estes desenhos seguindo a ordem do modelo." \n Quando usar: Dificuldades de escrita, organização espacial a nível gráfico, dificuldade de memória visual, coordenação visomotora e coordenação motora fina.')
    labelmemoria2.pack(padx=10,pady=10)

def complentacao_jogos(): #função jogo p colocar no botao
    janelacomplentacao = customtkinter.CTkToplevel(janela)
    janelacomplentacao.geometry('700x400')
    janelacomplentacao.title("Complementação de desenhos")
   
    labelcomp = customtkinter.CTkLabel(janelacomplentacao, text = 'COMPLEMENTAÇÃO DE DESENHOS')
    labelcomp.pack(padx=10,pady=10)
   
    labelcomp2 = customtkinter.CTkLabel(janelacomplentacao, text = ' Material: 1 folha de prova, lápis preto, borracha. \n Idade ideal: A partir dos 12 anos.\n Quando usar: Para avaliar a capacidade de abstração do aprendiz.\n O que se observa: Qualidade da complementação do desenho, ângulos, semelhança com o modelo, pressão e preensão.\n Instrua (ou fale): "Você está vendo esses desenhos? Os da direita são iguais aos da esquerda, mas estão em outra posição e faltando algo. \n Você vai completá-los de modo que fiquem iguais.”')
    labelcomp2.pack(padx=10,pady=10)


def analise_sintese(): #função jogo p colocar no botao
    janela_analise = customtkinter.CTkToplevel(janela)
    janela_analise.geometry('700x400')
    janela_analise.title("Prova de análise e síntese")
    
    labelanalise = customtkinter.CTkLabel(janela_analise, text = ' PROVA DE ANÁLISE E SÍNTESE (Figuras Incompletas)')
    labelanalise.pack(padx=10,pady=10)
    
    labelanalise2 = customtkinter.CTkLabel(janela_analise, text = ' Material: os cartões de aplicação da prova. \n Idade ideal: A partir dos 6 anos. \n Quando usar: Para avaliar a capacidade de abstração do aprendiz. \n O que se observa: Capacidade de identificação da criança. \n  Identidade de objetos. \n Instrua (ou fale): “Se este desenho tivesse completo o que seria ?')
    labelanalise2.pack(padx=10,pady=10)

def login(paciente):


    with open('pacientes.json', 'r') as arquivo:
        pacientes = json.load(arquivo)

    # verifica se o email e a senha digitada são iguais as que forma cadatradas e mostra o resultado
    if email.get() in pacientes and senha.get() == pacientes[email.get()]["senha"]:

        informacao_paciente(paciente)

    else: # se não tiver sido cadatrado, exibe o texto "Usuário ou senha incorretos"
        customtkinter.CTkLabel(janela, text='Usuário ou senha incorretos.').pack(padx=10, pady=10)

# define o modo de aparência como escuro
customtkinter.set_appearance_mode("dark")
# define o tema de cor padrão como azul escuro
customtkinter.set_default_color_theme("dark-blue")

# cria uma janela com título "Avaliação Pacientes" 
janela = customtkinter.CTk()
janela.title("Avaliação Pacientes") 
janela.geometry("700x400") #configuracao
janela.maxsize(width=900, height=550) #tamanho maximo
janela.minsize(width=500, height=300) #minimo
texto = customtkinter.CTkLabel(janela, text='Bem-vindo!') # add o texto "Bem-vindo" a janela
texto.pack(padx=10, pady=10) #configuracao

# chama a função checarJson()
checarjson()

# cria uma caixa de entrada de texto para o e-mail do paciente com um texto de placeholder, input
email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail:")
email.pack(padx=10, pady=10) #configuracao

# cria uma caixa de entrada de texto para a senha do paciente com um texto de placeholder e oculta os caracteres digitados
senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha:", show="*")
senha.pack(padx=10, pady=10) #configuracao

# cria uma Checkbox para lembrar o login
checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar login')
checkbox.pack(padx=10, pady=10) #configuracao

# cria um botão "Login" que chama a função login(email.get()) ao ser clicado 
botao = customtkinter.CTkButton(janela, text='Login', command=lambda: login(email.get()))
botao.pack(padx=10, pady=10)

# cria um botão "É profissional?" que chama a função login_profissional ao ser clicado
botao3 = customtkinter.CTkButton(janela, text='É profissional?', command=login_profissional)
botao3.pack(padx=10, pady=10)

# cria um botão "Recomendações jogos" que chama a função recomendacao_jogos ao ser clicado
botao4 = customtkinter.CTkButton(janela, text="Recomendações jogos", command=recomendacao_jogos)
botao4.pack(padx=10, pady=10)

# mantém a janela aberta enquanto o programa estiver em execução
janela.mainloop()


# E-mail e se senha do login profissional
#  Clínicaaba@gmail.com
#  abaImersão#
