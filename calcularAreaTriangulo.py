import math

aSide = int((input('Digite o lado A do triangulo: ')))
bSide = int((input('Digite o lado B do triangulo: ')))
cSide = int((input('Digite o lado C do triangulo: ')))

if aSide > (bSide+cSide) or bSide > (aSide+cSide) or cSide > (aSide+bSide):
    print(f'{aSide}, {bSide}, {cSide}, Não formam um triangulo')
else: 
    semiPerimetro = (aSide + bSide + cSide) // 2
    area = math.sqrt(semiPerimetro * ((semiPerimetro - aSide) * (semiPerimetro - bSide) * (semiPerimetro - cSide)))

print(f'A area do triangulo é: {area}')