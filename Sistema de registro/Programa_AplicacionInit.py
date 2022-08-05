from tkinter import IntVar, Toplevel
import sqlite3

class App():
    def __init__(self,window,nombre):
        self.CrearBaseDeDatos()

        self.parent=window
        self.parent.withdraw()
        self.root=Toplevel(self.parent)
        self.root.protocol("WM_DELETE_WINDOW", self.volver)
        self.mostrarpass= IntVar()
        self.root.title(nombre)
        self.widgets()

    def CrearBaseDeDatos(self):
        conn=sqlite3.connect('Usuarios.db')
        cursor=conn.cursor()
        query='CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL, usuario TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL)'
        cursor.execute(query)
        cursor.close()
        conn.close()
#-----------Funcion que retorna a la ventana anterior-----------#
    def volver(self):
        self.parent.deiconify()
        self.root.destroy()

    

