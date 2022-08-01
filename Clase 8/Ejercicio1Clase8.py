def main():
    lista=['Hola','Estoy escribiendo en ','Mi archivo ejemplo de python', 'Para la clase 8 de ','OpenBootcamp','~Eduardo']
    def EscribirArchivo(fichero: str, datos: list):
        f=open(fichero,'a')
        for linea in datos:
            if not linea.endswith('\n'):
                linea+='\n'
            f.write(linea)
        f.close()
    EscribirArchivo('Ejercicio1.txt',lista)
if __name__=='__main__':
    main()


