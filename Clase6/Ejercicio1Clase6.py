class Vehiculo:
    color=''
    ruedas=0
    puertas=0

class Coche:
    coche=Vehiculo()
    velocidad=0
    cilindrada=0

carro=Coche()
carro.coche.color='Rojo'
carro.coche.ruedas=4
carro.coche.puertas=5
carro.velocidad=330
carro.cilindrada=8
carro2=Coche()
print(carro2.coche.color,
carro2.coche.ruedas,
carro2.coche.puertas,
carro2.velocidad,
carro2.cilindrada)



