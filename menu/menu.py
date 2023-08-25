import os
lista_de_emails = []

while(True):
    os.system("cls")
    print("Menu funcionarios")
    print("1 - cadastrar")
    print("2 - listar funcionario")
    print("3 - excluir")
    print("4 - sair")
    opcao = input("Opcao: ")
    
    if (opcao == "1"):
        print("\nCadastro de funcionario\n")
        #Validar um nome completo, 2 palavras ao menos               
        while(True):
            nome_completo = input("Digite um nome completo: ")
            vetor_nome = nome_completo.split(" ")
            if (len(vetor_nome)<=1):
                print("Voce precisa digitar um nome completo!")
            else:
                break    
  
        #Montar um email baseado no nome e sobrenome
        email = vetor_nome[0]+"."+vetor_nome[-1]+"@ufn.edu.br"
        email = email.lower()

        #Verificar se o email ja esta na lista    
        if (lista_de_emails.__contains__(email)):
            print("Email ja cadastrado\n")
        else:
            lista_de_emails.append(email)
         
        #Manter ordenado a lista
        lista_de_emails.sort()

        
    elif (opcao == "2"):
        print("\nListagem de funcionarios\n")
        
        if (len(lista_de_emails)==0):
            print("Lista vazia")
        else:
            for i in lista_de_emails:
                print(i)
        
    elif (opcao == "3"):
        print("\nExclusao de funcionarios\n")
        email = input("Digite o email para ser removido")
        if (len(lista_de_emails)==0):
            print("Lista vazia")
        else:
            if (lista_de_emails.__contains__(email)):
                lista_de_emails.remove(email) 
            else:
                print("O email nao existe na lista")      
 
        
    elif (opcao == "4"):
        print("\nSaiu do menu\n")
        break
    
    else:
        print("\nOpcao invalida\n")    
        
    os.system("pause")