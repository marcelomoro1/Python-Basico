'''#1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar
#    uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),
#    meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60). 
#    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina
#    que ele deverá administrar baseada na equação: 
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade
'''
glicemia = int(input('Digite sua glicemia'))
pre = int(input('Qual sua meta pre-refeicao?'))
sensibilidade = int(input('Qual o fator de sensibilidade?'))

if sensibilidade <20 or sensibilidade>60:
    print("Valor invalido")

else:    
    qnt_insulina = (glicemia - pre)/sensibilidade
    print(qnt_insulina)
