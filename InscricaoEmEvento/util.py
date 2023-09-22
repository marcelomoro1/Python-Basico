def inscricao(lista):
    matricula = input("Digite a sua matricula: ")
    if matricula in lista:
        print("Ja escrita no evento!")
    else:
        lista.append(matricula)
        nome = input("Digite o seu nome: ").upper()
        email = input("Digite o seu email: ").lower()

        escritor = open('inscricoes.dat','a')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')
        escritor.close()

def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat', 'r')
        for i in leitor:
            vetor_i = i.split(';')
            lista.append(vetor_i[0])

        leitor.close()
    except:
        pass    

def listagem():
    try:
        leitor = open('inscricoes.dat', 'r')
        for i in leitor:
            vetor_i = i.split(';')
            print('Nome:', vetor_i[1], ' Matricula:',vetor_i[2])
        leitor.close()
    except:
        print("Nao ha inscritos no evento")        