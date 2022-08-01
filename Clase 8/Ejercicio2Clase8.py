import pickle
class Vehiculo():
    def __init__(self,marca: str,modelo: str,cilindraje:float):
        self._marca=marca
        self._modelo=modelo
        self._cilindraje=cilindraje

    def __str__(self):
        return f'Es un carro marca: {self._marca}, modelo: {self._modelo}, con un cilindraje: {self._cilindraje}'

carro=Vehiculo('Ford','Explorer','4.0')
print(carro)

with open('Ejercicio2.bin','wb') as WriteFile:
    pickle.dump(carro, WriteFile)
    WriteFile.close()
with open('Ejercicio2.bin','rb') as ReadFile:
    carro2=pickle.load(ReadFile)
    ReadFile.close()

print(carro2)


