import random

def generar_password():
    mayus = ['A', 'B', 'C', 'D', 'F', 'G']
    minus = ['a','b','c','d','e','f', 'g']
    simbol = ['!','#','$','%','&']
    num = ['1','2','3','4','5','6','7','8','9']

    caracteres = mayus + minus + simbol + num

    password = []
    
    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)
    return password


def run():
    password = generar_password()
    print('Tu nueva contraseña es: ' + password)


if __name__=='__main__':
    run()
