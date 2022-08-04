from getpass import getpass
import sqlite3
import tkinter
def main():
    seleccion = int(input('Quieres Registrarte un nuevo Alumno o Verificar sus datos (1: Registro, 2: Verificar): '))
    nombre = input('Nombre de Alumno: ')
    if(seleccion==1):
        apellido = input('Apellido del Alumno: ')
        Crear_Alumno(nombre,apellido)
    elif(seleccion==2):
        Verificar_Alumno(nombre)
    else:
        print('Haz escogido una opcion invalida')

def Verificar_Alumno(nombre):

    if Verifica_Existencia(nombre):
        conn=sqlite3.connect('Alumnos.db')
        cursor=conn.cursor()
        query= f"SELECT * FROM Alumnos WHERE nombre='{nombre}'"
        rows=cursor.execute(query)
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
    else:
        print('El alumno no esta registrado')

def Verifica_Existencia(nombre):
    conn = sqlite3.connect('Alumnos.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM Alumnos WHERE nombre = '{nombre}'"
    rows = cursor.execute(query)
    data=rows.fetchone()

    cursor.close() 
    conn.close()

    if data==None:
        return False
    
    return True

def Crear_Alumno(nombre, apellido):
    if (Verifica_Existencia(nombre)):
        print('Lo siento este alumno ya se encuentra registrado')
    else:    
        conn = sqlite3.connect('Alumnos.db')
        cursor = conn.cursor()

        query = f"INSERT INTO Alumnos(nombre, apellido) VALUES( '{nombre}', '{apellido}')"

        rows = cursor.execute(query)
        conn.commit()
        cursor.close() 
        conn.close()

if __name__=='__main__':
    main()


