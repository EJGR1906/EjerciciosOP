def main():
    def Paises():
        set_paises={input('Por favor introduce un pais: ').capitalize()}
        print('')
        i=0
        while True:
            print('**Si quieres salir del programa escribe "Fin"**')
            set_paises.add(input('Por favor introduce un pais: ').capitalize().strip())
            print('')
            lista_paises=list(set_paises)
            try:
                lista_paises.pop(lista_paises.index('Fin'))
                return sorted(lista_paises)
            except:
                i+=1
        
    print(Paises())
            
            
if __name__=='__main__':
    main()