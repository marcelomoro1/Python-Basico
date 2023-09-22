import os
from util import inscricao, conexao_base, listagem
lista_inscritos = [] #guardar matricula

conexao_base(lista_inscritos) #adiciona as matriculas do inscricoes.dat pra caso eu for registrar uma matricula, ele já verificar se existe no bloco de notas


while(True):
    os.system("cls")
    print("1 - Inscrever")
    print("2 - Listar")
    print("3 - Registrar entrada")
    print("4 - Registrar saida")
    print("5 - Sair")

    opcao = input("opcao: ")

    if(opcao == "1"):   
       inscricao(lista_inscritos)
    elif(opcao == "2"):
       listagem()
    elif(opcao == "3"):
       print('b')
    elif(opcao == "4"):
       print('c')     
    elif(opcao == "5"):
        print("Saiu do sistema\n")
        break
    else:
        print ("opcao invalida! Tente novamente\n")

    os.system("pause")