def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    
    if palabra == palabra_invertida:
        return print("Es palindromo")
    else:
        return print("No es palindromo")


def run():
    print("Cuidado con la aibofobia")
    palabra = input('Escribe una palabra: ')
    palindromo(palabra)
#    es_palindromo = palindromo(palabra)

#    if es_palindromo == True:
#        print("Es palindromo")
#    else:
#        print("No es palindromo")


if __name__ == '__main__':
    run()
