#4 - O volume de um cubo é determinado através do produto da área da base pela altura, 
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.

altura = float(input('Digite a altura em metros'))
largura = float(input('Digite a largura em metros'))
comprimento = float(input('Digite o comprimento em metros'))

area_base = comprimento*largura
volume = area_base*altura
print('O volume de agua necessario para encher eh: ',volume,' litros')