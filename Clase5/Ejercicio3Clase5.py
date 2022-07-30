bisiesto=lambda year: f'{year} es un año bisiesto' if year % 4 == 0 else f'{year} No un año bisiesto'

num=int(input('Introduce un año para ser comprobado: '))

print(bisiesto(num))

