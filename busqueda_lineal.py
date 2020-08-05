import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match 


if __name__ == '__main__':
    whit_of_list = int(input('De qué tamaño será a lista?'))
    objetivo = int(input('Qué número quieres enontrar?'))

    lista = [random.randint(0, 100) for i in range(whit_of_list)]


    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
