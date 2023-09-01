# fhffhgj
import random
# def popular(lista,quantidade):
#     for i in range(0,quantidade):
#         lista.append(random.randint(0,100))

#     lista.sort()

# def exibir(lista):
#     for i in lista:
#         print(i)


def popular_nomes(lista_nomes,quantidade):
    for i in range(0,quantidade):
        nome = input(" Digite um nome ")
        nome.upper()
        if(lista_nomes.__contains__(nome)):
            print("Nome ja esta presente na lista")
            break
        lista_nomes.append(nome)
        
    lista_nomes.sort()

def exibir_nomes(lista_nomes):
    for i in lista_nomes:
        print(i)

