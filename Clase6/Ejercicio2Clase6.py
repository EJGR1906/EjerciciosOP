class Alumno:
    def __init__(self,nombre,nota):
        self._nombre=Alumno.Nombre(nombre)
        self._nota=Alumno.Nota(nota)
    def Nombre(nombre):
        print(f'Hola, {nombre}')
        return nombre
             
    def Nota(nota):
        print(f'Tu nota es {nota}')
        return nota
    def MostrarNota(self):
        if self._nota<10:
            print(f'{self._nombre}, reprobaste con {self._nota}')
        else:
            print(f'{self._nombre}, aprobaste con {self._nota}')

eduardo=Alumno('Eduardo',10)
eduardo.MostrarNota()
