
#7 - Faça um programa Python que receba duas notas, calcule a média aritmética e mostre o resultado.
#    Além disso, deve mostrar ao lado da média Aprovado (se média >= 7.0) Reprovado (se média <= 3.0),
#    Exame (se média entre 3.0 e 7.0)

nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
media = (nota1+nota2)/2
if media >=7:
    print("Aprovado")
elif media >=3 and media<7:
    print("Exame")
else:
    print("Reprovado")
    