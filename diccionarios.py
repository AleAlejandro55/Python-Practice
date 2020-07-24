def run():
    mi_dic = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    
#    print(mi_dic['llave1'])
#    print(mi_dic['llave2'])
#    print(mi_dic['llave3'])

    poblacion_paises = {
        'Argentina': 44_938712,
        'Brasil': 210147_125,
        'Colombia': 50_372424,
    }

#    print(poblacion_paises['Argentina'])

    for pais, poblacion in poblacion_paises.items():

        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__=='__main__':
    run()
