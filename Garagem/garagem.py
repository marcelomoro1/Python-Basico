import os

lista = []

def entrarGaragem():
    while(True): 
        placa = input("Digite a placa: ").upper()
        if len(placa) != 7:
            print("Placa inválida")
        else:
            break

    if (lista.__contains__(placa)):
        print("Carro já esta na garagem!")
    else:
        lista.append(placa)
            
    lista.sort()

def exibirLista():
    if (len(lista) == 0 ):
        print("Lista Vazia!")
    else:
        for i in lista:
            print(i)    

def excluirPlaca():
    if len(lista) == 0:
        print("Lista vazia!")
    else:
        placa = input("Digite a placa que deseja apagar: ").upper()

        if placa in lista:
            lista.remove(placa)
            print(f"Placa {placa} removida com sucesso!")
        else:
            print("Placa não localizada!")

while(True):
    os.system("cls")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Sair")

    opcao = input("opcao: ")

    if(opcao == "1"):   
       entrarGaragem()
    elif(opcao == "2"):
       exibirLista()
    elif(opcao == "3"):
       excluirPlaca()
    elif(opcao == "4"):
        print("Saiu do sistema\n")
        break
    else:
        print ("opcao invalida! Tente novamente\n")

    os.system("pause")