'''#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.'''

distancia = float(input('Digite a distancia em km'))
tempo = float(input('Digite o tempo em horas'))
vm = distancia/tempo

print('Velocidade media eh de: ',vm,' km/h')