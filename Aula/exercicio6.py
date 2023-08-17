#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados

estado = input('Digite a sigla de um estado')

if estado == "RS":
    print("Sulista")
elif estado == "SP":
    print("Paulista")
elif estado == "MG":
    print("Mineiro")
elif estado == "AM":
    print("Amazonense")
elif estado == "PE":
    print("Pernambucano")
