import tkinter
def main():
    #Creo la ventana
    window=tkinter.Tk()
    window.title('Ejercicio1')
    #Definimos las funciones
    def MostrarValor():
        label1.config(text=f'{valorRadiobutton.get()}')

    def Reiniciar():
        valorRadiobutton.set(0)
        MostrarValor()
    #Creamos el frame
    frame=tkinter.Frame(window,padx=20,pady=20)
    frame.pack()

    #Creamos los radiobuttons
    valorRadiobutton=tkinter.IntVar()
    radiobutton1=tkinter.Radiobutton(frame,text='Radiobutton 1',variable=valorRadiobutton,value=1,command=MostrarValor)
    radiobutton1.pack()

    radiobutton2=tkinter.Radiobutton(frame,text='Radiobutton 2',variable=valorRadiobutton,value=2,command=MostrarValor)
    radiobutton2.pack()

    radiobutton3=tkinter.Radiobutton(frame,text='Radiobutton 3',variable=valorRadiobutton,value=3,command=MostrarValor)
    radiobutton3.pack()

    radiobutton4=tkinter.Radiobutton(frame,text='Radiobutton 4',variable=valorRadiobutton,value=4,command=MostrarValor)
    radiobutton4.pack()

    #Creamos el button de reinicio
    button=tkinter.Button(frame,text='Reinicio',command=Reiniciar)
    button.pack()

    #Creamos el label
    label1=tkinter.Label(frame)
    label1.pack()


    window.mainloop()

if __name__=='__main__':
    main()
