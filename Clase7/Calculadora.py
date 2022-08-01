def Suma(*numeros):
    _total=0
    for num in numeros:
        _total+=num
    return _total

def Resta(*numeros):
    _total=numeros[0]
    for i in range(1,len(numeros)):
        _total-=numeros[i]
    return _total

def Multiplicar(*numeros):
    _total=1
    for num in numeros:
        _total*=num
    return _total

def Dividir(a,b):
    try:
        return a/b
    except:
        print('a o b es 0, no puedes dividir')
        return 0