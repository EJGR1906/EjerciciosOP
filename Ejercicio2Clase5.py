#Segundo ejercicio clase 5
def comprobarPrimo(num):
    lista=[]
    for i in range(1, num+1):
        if (num%i==0):
            lista.append(i)
    if(len(lista)>2):
        return f'{num} No es un numero primo'
    else:
        return f'{num} Si es un numero primo'
num=int(input('Por favor, introduce un numero entero para ser comprobado: '))

print(comprobarPrimo(num))

