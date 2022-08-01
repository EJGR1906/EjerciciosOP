import time 
def main():
    #Definimos el tiempo local al momento de la ejecucion
    lt=time.localtime()
    #Definimos la hora de salida
    #Finish time 
    ft=(lt.tm_year,lt.tm_mon,lt.tm_mday,19,0,0,lt.tm_wday,lt.tm_yday,lt.tm_isdst)
    print('La hora actual es:', time.strftime('%X',lt))
    print('La hora de salida es:', time.strftime('%X',ft))

    #Si, la hora actual ya ha pasado la hora de salida, entonces:
    if(time.mktime(lt)>=time.mktime(ft)):
        print('Es hora de salir! la hora actual es',time.strftime('%X',lt))

    #Si la hora actual es menor a la hora de salida, entonces:
    else:
        #Restamos la hora de salida con la hora actual 
        time_left=(lt.tm_year,lt.tm_mon,lt.tm_mday,18-lt.tm_hour,60-lt.tm_min,60-lt.tm_sec,lt.tm_wday,lt.tm_yday,lt.tm_isdst)
        print('Aun no es la hora de salir, todavia faltan:',time.strftime('%X',time_left))

if __name__ == '__main__':
    main()




