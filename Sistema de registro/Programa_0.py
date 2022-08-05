
from Programa_Registro import AppRegistro
from Programa_Login import AppLogin
from tkinter import ttk
import tkinter as tk 

class Aplicacion():
    def __init__(self):
        self.window=tk.Tk()
        self.window.title('Programa')
        self.widgets()


    def widgets(self):
        #-----------Creamos los labels
        #Label de inicio
        label1=tk.Label(self.window,text='Bienvenido! Por favor inicia sesion.')
        label1.grid(columnspan=4, row=1,padx=5,pady=5)
 
        #-----------Creamos los botones-----------

        #Boton de Registro
        button1=ttk.Button(self.window,text='Registrate Aqui',command=self.Registrar)
        button1.grid(column=0,row=2,padx=5,pady=5,sticky="E")

        #Boton de login
        button2=ttk.Button(self.window,text='Inicia Sesion Aqui',command=self.IniciarSesion)
        button2.grid(column=3,row=2,padx=5,pady=5,sticky="W")
        self.window.mainloop()
    #-----------Funcion para iniciar sesion-----------
    def IniciarSesion(self):
        nombre='Login'
        AppLogin(self.window,nombre)
    #-----------Funcion para registrar-----------
    def Registrar(self):
        nombre='Registro'
        AppRegistro(self.window,nombre)

if __name__=='__main__':
    Aplicacion()