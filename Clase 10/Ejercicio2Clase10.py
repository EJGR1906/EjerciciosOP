import tkinter
from tkinter import ttk

class Aplicacion(tkinter.Tk):
    def __init__(self):
        #Creamos la ventana
        self.window=tkinter.Tk()
        self.window.title('Ejercicio 2 OpenBootcamp Python')
        self.window.config(bg='gray')

        #Creamos los labels 
        self.label1= tkinter.Label(self.window,text='Por favor selecciona una opcion:')
        self.label1.pack(side='top')

        #Creamos la lista seleccionable
        #Creamos los valores seleccionables
        self.list_values=['HTML','CSS','JavaScript','Python','C#']
        self.lista_desplegable=ttk.Combobox(self.window,state='readonly',values=self.list_values)
        self.lista_desplegable.pack()

        #Creamos un boton 
        self.button=tkinter.Button(self.window,text='A estudiar!',command=self.Seleccion)
        self.button.pack()

        self.window.mainloop()
        #Definimos la funcion 
    def Seleccion(self):
        self.label1.config(text=f'Es hora de estudiar {self.lista_desplegable.get()}')
    

if __name__=='__main__':
    app=Aplicacion()
