# Bibliotecas
import time, os
# Variaveis
Alunos = {
    0: {"nome":"Ana","nota":8.5},
    1: {"nome":"Claudia","nota":6.0},
    2: {"nome":"Diego","nota":4.5},
    3: {"nome":"Diogo","nota":6.5},
    4: {"nome":"Elizia","nota":9.5},
    5: {"nome":"Fabricio","nota":5.5},
    6: {"nome":"Gabriella","nota":8.0},
    7: {"nome":"Marcelo","nota":4.0},
    8: {"nome":"Marcelly","nota":9.0},
    9: {"nome":"Tássia","nota":2.5},
}

# Funções
def LoaderVisual(resposta:str) -> None:
    for i in range(1, 4):
        os.system("cls" if os.name =="nt" else "clear")
        print(resposta+(i*"."))
        time.sleep(0.5)
    time.sleep(0.7)

def Menu() -> chr : 
    entrada = input("Escolhas as opções abaixo\n[A] Alterar\n[E] Excluir\n[M] Mostrar Nomes\n[S] Sair\n").upper()
    return entrada

def Check_Index() -> int:
    try:
        indice = int(input("Insira o ID do aluno:\n"))
        if (indice in range(0, Alunos.__len__())):
            return indice
        else:
            return Check_Index()
    except(ValueError):
        Check_Index()
    finally:
        os.system("cls" if os.name =="nt" else "clear")

def Delete_Data_User(indice:int=-1) -> None:
    if indice < 0: return

    try:
        confirm = input(f"O ID {indice} que corresponde à {Alunos.get(indice)["nome"]}, é o alvo a ser deletado?\n[S\\N]\n")

        if (confirm.upper() not in ["S"]):
            print("Voltando ao menu")
            time.sleep(1)
            return
        else:
            Alunos.pop(indice)
            LoaderVisual("Aluno Removido")
    except (ValueError):
        print("Você inseriu algo que não esperavamos, tente novamente")
        time.sleep(1)
        return
    finally:
        os.system("cls" if os.name =="nt" else "clear")

def Change_Data_User(indice:int=-1) -> None:
    if indice < 0: return

    try:
        notaNew = int(input(f"Insira a nota que gostaria de substituir à {Alunos.get(indice)["nome"]}\n"))
        confirm = input(f"Você tem certeza que irá mudar a nota de {Alunos.get(indice)["nome"]}\n[S\\N]\n")
        if (0 <= notaNew <= 10 and confirm.upper() in ["S"]):
            Alunos.get(indice)["nota"] = notaNew
            LoaderVisual("Alterando Nota")
        else:
            print("Nota inválida")
            time.sleep(1)
    except (ValueError):
        print("Você inseriu algo que não é um valor numérico, tente novamente\n")
        return time.sleep(1)
    finally:
        os.system("cls" if os.name =="nt" else "clear")

# Loops
while True:
    os.system("cls" if os.name =="nt" else "clear")
    match Menu():
        case "A":
            Change_Data_User(Check_Index())
        case "E":
            Delete_Data_User(Check_Index())
        case "M":
            os.system("cls" if os.name =="nt" else "clear")
            for i, v in Alunos.items():
                time.sleep(0.8)
                print(f"\nID: {i}\nAluno: {v["nome"]}\nMédia: {v["nota"]}\n")
        case "S":
            print("Saindo")
            break
        case _:
            print("Escolha algo válido")
            time.sleep(1)
