alunos, media = [], []

def Exibir_Alunos_Notas():
    iterador_Notas = 0
    for aluno in alunos:
        print("-----------------------", "\nALUNO: \n", aluno, "\n\nMÉDIA: \n", media[iterador_Notas], "\n-----------------------")

def Inserir_Aluno():
    entrada = input("Insira o nome do aluno:\n")
    if (entrada != None and not entrada.isdigit()):
        alunos.append(entrada)
    else:
        print("Insira o nome corretamente")
        # Callback
        Inserir_Aluno()
    

def Inserir_Nota():
    entrada = float(input("Insira a nota do aluno:\n"))
    if (entrada != None and entrada >= 0.0 and entrada <= 10.0):
        media.append(entrada)
    else:
        print("Insira a nota corretamente")
        # Callback
        Inserir_Nota()

def Pesquisar_Aluno():
    print ("Deseja consultar algum aluno específico?\nS\\N")
    # Entrada do usuário
    entrada = input().lower()
    # Tratamento
    if (entrada != None and entrada == "s"):
        print("Insira o nome do aluno:")
        nome_search = input()
        i = alunos.index(nome_search)
        print("-----------------------", "\nALUNO: \n", alunos[i], "\n\nMÉDIA: \n", media[i], "\n-----------------------")
    else:
        Exibir_Alunos_Notas()
        

# Começar a inserção de dados
Inserir_Aluno()
Inserir_Nota()
# Loop
while True:
    # Questionando o usuário
    print("Deseja continuar?\nS\\N")
    entrada = input().lower()
    if (entrada != None):
        if (entrada == "s"):
            Inserir_Aluno()
            Inserir_Nota()
        else:
            Pesquisar_Aluno()
            break
    else:
        Exibir_Alunos_Notas()
        break