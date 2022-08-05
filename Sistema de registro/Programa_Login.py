from Programa_AplicacionInit import App
from Programa_Registro import AppRegistro
from tkinter import messagebox, ttk
import tkinter as tk 
import sqlite3

class AppLogin(App):
    def __init__(self,window,nombre):
        super().__init__(window,nombre)
        
    def widgets(self):
        #-----------Creamos los labels-----------
        #Label Usuario
        label1=tk.Label(self.root, text='Usuario:')
        label1.grid(column=0,row=0,padx=5,pady=5)

        #Label Contraseña
        label2=tk.Label(self.root,text='Contraseña:')
        label2.grid(column=0,row=2,padx=5,pady=5)

        #Label Usuario Existente
        self.label3=tk.Label(self.root,text='Usuario o contraseña incorrecta',fg='red')

        #-----------Creamos las entradas de texto-----------
        #Entrada de Usuario
        text1=ttk.Entry(self.root)
        text1.grid(column=1,row=0,padx=5)

        #Entrada de Contraseña
        self.text2=ttk.Entry(self.root,show='*')
        self.text2.grid(column=1,row=2,padx=5,pady=5)

        #-----------Creamos los botones-----------

        #Boton de Registro
        boton_register=ttk.Button(self.root,text='Registro',command=self.Ventana_Registro)
        boton_register.grid(column=0,row=3,padx=5,pady=5)

        #Boton de login
        boton_login=ttk.Button(self.root,text='Login',command=lambda: self.Login(text1.get(),self.text2.get()))
        boton_login.grid(column=1,row=4,padx=5,pady=5)

        #-----------Creamos el check-----------

        #Check para mostrar Contraseña
        check_mostrar=ttk.Checkbutton(self.root,text='Mostrar',command=self.MostrarPass,variable=self.mostrarpass)
        check_mostrar.grid(column=2,row=2,padx=5,pady=5)

    def Ventana_Registro(self):
        nombre='Registro'
        self.root.destroy()
        AppRegistro(self.parent,nombre)

    def MostrarPass(self):
        if self.mostrarpass.get()==1:
            self.text2.config(show='')
        else:
            self.text2.config(show='*')

    def Login(self,usuario,passw):
        conn=sqlite3.connect('Usuarios.db')
        cursor=conn.cursor()

        query=f"SELECT id FROM users WHERE usuario='{usuario}' AND password='{passw}'"
        row=cursor.execute(query)
        data=row.fetchone()
        if data==None:
            self.label3.grid(column=1,row=3)
        else:
            self.label3.grid_forget()
            messagebox.showinfo('Login', 'Se ha logeado correctamente!')
            self.volver()
        cursor.close()
        conn.close()