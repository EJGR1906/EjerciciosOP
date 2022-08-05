from Programa_AplicacionInit import App
from tkinter import ttk,messagebox
import tkinter as tk
import sqlite3

class AppRegistro(App):
    def __init__(self,window,nombre):
        super().__init__(window,nombre)

    #-----------Funcion que define los widgets-----------#
    def widgets(self):
        #-----------Creamos los labels-----------#
        #Label Nombre completo
        label0=tk.Label(self.root, text='Nombre completo:')
        label0.grid(column=0,row=0,padx=5,pady=5,sticky=tk.W)

        #Label Usuario
        label1=tk.Label(self.root, text='Usuario:')
        label1.grid(column=0,row=2,padx=5,pady=5,sticky=tk.W)

        #Label Email
        label2=tk.Label(self.root, text='Email:')
        label2.grid(column=0,row=4,padx=5,pady=5,sticky=tk.W)

        #Label Contraseña
        label3=tk.Label(self.root,text='Contraseña:')
        label3.grid(column=0,row=6,padx=5,pady=5,sticky=tk.W)

        #Label Confirmar Contraseña
        label4=tk.Label(self.root,text='Confirmar contraseña:')
        label4.grid(column=0,row=8,padx=5,pady=5,sticky=tk.W)

        #Label Usuario Existente
        self.label5=tk.Label(self.root,text='Este usuario ya existe')

        #Label Email Existente
        self.label6=tk.Label(self.root,text='Este email ya existe')

        #------Labels de entrys vacios------#

        self.label7=tk.Label(self.root,fg='red')

        self.label8=tk.Label(self.root,fg='red')

        self.label9=tk.Label(self.root,fg='red')

        self.label10=tk.Label(self.root,fg='red')

        self.label11=tk.Label(self.root,fg='red')

        #-----------Creamos las entradas de texto-----------#

        #Entrada de Nombre completo
        self.text1=ttk.Entry(self.root)
        self.text1.grid(column=1,row=0,padx=5)

        #Entrada de Usuario
        self.text2=ttk.Entry(self.root)
        self.text2.grid(column=1,row=2,padx=5)

        #Entrada de Email
        self.text3=ttk.Entry(self.root)
        self.text3.grid(column=1,row=4,padx=5,pady=5)

        #Entrada de Contraseña
        self.text4=ttk.Entry(self.root,show='*')
        self.text4.grid(column=1,row=6,padx=5)

        #Entrada de Confirmar contraseña
        self.text5=ttk.Entry(self.root,show='*')
        self.text5.grid(column=1,row=8,padx=5,pady=5)

        #-----------Creamos el boton-----------#

        #Boton de Registro
        boton_register=ttk.Button(self.root,text='Registrar',command=self.CrearUsuario)
        boton_register.grid(column=1,row=10,padx=5,pady=5)

        #-----------Creamos el check-----------#

        #Check para mostrar Contraseña
        self.check_mostrar=ttk.Checkbutton(self.root,text='Mostrar',command=self.MostrarPass,variable=self.mostrarpass)
        self.check_mostrar.grid(column=2,row=6,padx=5,pady=5) 
    #-----------Funcion Crear Usuario-----------#
    def CrearUsuario(self):
        self.OcultarLabels()
        if self.VerificarEntrys():
            nombre=self.text1.get().split(' ')[0]
            try:
                apellido=self.text1.get().split(' ')[1]

            except IndexError:
                apellido=''

            usuario=self.text2.get()
            email=self.text3.get()
            passw=self.text4.get()
            if (self.VerificarUsuario(usuario) and self.VerificarEmail(email) and self.ComprobarPass()):
                
                print('Puedes registrarlo')
                conn=sqlite3.connect('Usuarios.db')
                cursor=conn.cursor()
                query=f"INSERT INTO users(nombre,apellido,usuario,email,password) VALUES('{nombre}','{apellido}','{usuario}','{email}','{passw}')"
                cursor.execute(query)
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo('Register','Se ha registrado correctamente!')
                self.volver()
            elif self.ComprobarPass()==False:
                self.label11.config(text='Las contraseñas no coinciden')
                self.label11.grid(column=1,row=9)
            else:
                self.EmailExistente()
                self.UsuarioExistente()           
    #-----------Funcion Verificar Entradas de datos-----------#
    def VerificarEntrys(self):
        texto1=self.text1.get()
        texto2=self.text2.get()
        texto3=self.text3.get()
        texto4=self.text4.get()
        texto5=self.text5.get()
        
        if texto1=='':
            self.label7.config(text='No puede estar vacio')
            self.label7.grid(column=1,row=1)
        if texto2=='':
            self.label8.config(text='No puede estar vacio')
            self.label8.grid(column=1,row=3)
        if texto3=='':
            self.label9.config(text='No puede estar vacio')
            self.label9.grid(column=1,row=5)
        if texto4=='':
            self.label10.config(text='No puede estar vacio')
            self.label10.grid(column=1,row=7)
        if texto5=='':
            self.label11.config(text='No puede estar vacio')
            self.label11.grid(column=1,row=9)
        if(texto1=='' or texto2=='' or texto3=='' or texto4==''or texto5==''):
            return False
        return True
    #-----------Funcion que muestra las contraseñas-----------#
    def MostrarPass(self):
        if self.mostrarpass.get() == 1:
                self.text4.config(show='')
                self.text5.config(show='')
        else:
                self.text4.config(show='*')
                self.text5.config(show='*')
    #-----------Funcion que comprueba si las claves son identicas-----------#
    def ComprobarPass(self):
        password1=self.text4.get()
        password2=self.text5.get()

        if(password1==password2):
            return True
        return False
    #-----------Funcion que oculta los labels de aviso-----------#
    def OcultarLabels(self):
        self.label7.grid_forget()
        self.label8.grid_forget()
        self.label9.grid_forget()
        self.label10.grid_forget()
        self.label11.grid_forget()
    #-----------Funcion Verificar existencia del usuario-----------#
    def VerificarUsuario(self,usuario):
        conn=sqlite3.connect('Usuarios.db')
        cursor=conn.cursor()

        query=f"SELECT id FROM users WHERE usuario= '{usuario}'"
        rows=cursor.execute(query)
        data=rows.fetchone()

        cursor.close()
        conn.close
        
        if(data == None):
            return True

        #Si el usuario existe, entonces:
        self.label5.grid(column=1,row=3)
        return False
    #-----------Funcion Verificar existencia del email-----------#
    def VerificarEmail(self,email):
        conn=sqlite3.connect('Usuarios.db')
        cursor=conn.cursor()

        query=f"SELECT id FROM users WHERE email= '{email}'"
        rows=cursor.execute(query)
        data=rows.fetchone()

        cursor.close()
        conn.close
        if(data == None):
            return True

        #Si el email existe, entonces:
        self.label6.grid(column=1,row=5)
        return False

