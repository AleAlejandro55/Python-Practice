edad = int(input("escribe tu edad: "))

if edad > 17 and edad < 120:
    print("eres mayor de edad")
elif edad < 17 and edad > 0:
    print("eres menor de edad")
else:
    print("eres un robot o un elefante mistico ancestral")
