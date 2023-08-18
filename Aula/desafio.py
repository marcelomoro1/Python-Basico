
#DESAFIO
#CNTRL V = CNTRL + SHIFT + V
texto = input("Digite o texto para encontrar a quantidade de palavras/artigos/prep \n")
palavras = texto.split()
qnt_palavras = len(palavras)

artigo = ["a", "o", "as", "os", "um", "uma", "uns"]
qnt_artigo = 0

preposicoes = ["ante", "apos", "adiante"]
quais_prepo = []

for i in palavras:
    if i.lower() in artigo:
        qnt_artigo=qnt_artigo+1
    if i.lower() in preposicoes:
        quais_prepo.append(i) #Joga pra dentro da lista
    
print("A quantidade de palavras eh:",qnt_palavras,", e a quantidade de artigos eh:",qnt_artigo, ", As prepo: ",quais_prepo) 