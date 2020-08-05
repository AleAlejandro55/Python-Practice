import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    whit_of_list = int(input('De qué tamaño será a lista?'))
    objetivo = int(input('Qué número quieres enontrar?'))

    lista = [random.randint(0, 100) for i in range(whit_of_list)]


    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
