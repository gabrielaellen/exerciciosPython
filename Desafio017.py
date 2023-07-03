import math
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')

'''Outro exemplo:
from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')'''