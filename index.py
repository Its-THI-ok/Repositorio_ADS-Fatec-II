# Dados
alunos =  [
    ["Ana", 8.5],
    ["Claudia", 6.0],
    ["Diego", 4.5],
    ["Diogo", 6.5],
    ["Elizia", 9.5],
    ["Fabricio", 5.5],
    ["Gabriella", 8.0],
    ["Marcelo", 4.0],
    ["Marcelly", 9.0],
    ["Tássia", 2.5]
]

def Menu()->str:
    entrada = input("Escolhas as opções abaixo\n[A] Alterar\n[E] Excluir\n[M] Mostrar Nomes\n[S] Sair\n").upper()
    if (entrada not in ["A", "E", "M", "S"]):
        print("Insira um valor válido")
    else:
        return entrada

def Checador_Indice(indice:int)->int:
    if (indice in range(0, len(alunos))):
        return indice
    else:
        return -1

def Opcao_Execute()->bool:
    input_msg = input().upper()
    if ((input_msg in ["S", "SI", "SIM"])): 
        return True
    else: 
        return False

def Inserindo_Nota(target:int =-1)->None:
    if (not Checador_Indice(target) >= 0): return print("Valor fora de índice")
    # Carregando Dado
    print(f"{alunos[target][0]}, {alunos[target][1]}\nDeseja alterar registro de {alunos[target][0]}?\nS\\N:")
    if Opcao_Execute(): 
        valor = float(input("Insira a nova nota:\n"))
        while (0 < valor > 10):
            print("Insira uma nota corretamente")
            valor = float(input("Insira a nova nota:\n"))

        print("Confirme?\nS\\N")
        if Opcao_Execute():
            alunos[target].__setitem__(1, valor)
        else:
            print("Cancelando")

def Remove_Data(target:int =-1)->None:
    if (not Checador_Indice(target) >= 0): return print("Valor fora de índice")

    print(f"{alunos[target][0]}, {alunos[target][1]}\nDeseja remover {alunos[target][0]} do registro?\nS\\N")

    # Carregando Dado
    if Opcao_Execute():
        alunos.pop(target)

while True:
    match Menu():
        case "A":
            Inserindo_Nota(Checador_Indice(int(input("Insira o ID:\n"))))
        case "E":
            Remove_Data(Checador_Indice(int(input("Insira o ID:\n"))))
        case "M":
            for i, (nome, media) in enumerate(alunos):
                print(f"\nID:{i}\nAluno: {nome}\nMédia: {media}")
        case "S":
            print("Saindo")
            break
        case _:
            print("Escolha algo válido")
