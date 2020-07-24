def conversor(tipo_moneda, valor_dolar):
    pesos = input("¿Cuántos " + tipo_moneda + "tienes? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 
elige una opción:
    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos
"""

opcion = int(input(menu))

if opcion == 1:
    conversor("pesos colombianos", 3875)
elif opcion == 2:
    conversor("pesos argentinos", 65)
elif opcion == 3:
    conversor("pesos argentinos", 24)

else:
    print("Ingresa un número válido")
