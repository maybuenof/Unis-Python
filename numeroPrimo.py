numero = int(input('Digite um numero de 1 a 100: '))

if numero < 1 or numero > 100:
    print('Numero não é válido')

primo = True

if numero > 1:
    for index in range(2, numero):
        if (numero % index) == 0:
            primo = False
            break

if primo == False:
    print(f'O número {numero} não é primo')
else: print(f'O número {numero} é primo')