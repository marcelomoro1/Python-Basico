#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.

distancia = float(input('Digite a distancia em km'))
vm = float(input('Digite a velocidade media'))
t = distancia/vm

print('O tempo foi de : ',t,' horas')