def run():
    nombre_1 = input('Cual es tu nombre?: ')
    edad_1 = int(input('Cuantos años tienes? '))
    nombre_2 = input('Cual es el otro nombre?: ')
    edad_2 = int(input('Cuantos años tienes?  '))


    if edad_1 > edad_2:
        print(f'{nombre_1} es mayor que {nombre_2}')
    elif edad_1 < edad_2:
        print(f'{nombre_2} es mayor que {nombre_1}')
    else: 
        print('Los dos tienen la misma edad')


if __name__=='__main__':
    run()
