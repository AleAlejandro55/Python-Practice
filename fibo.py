def run():
    contador = int(input("cuantos números fibonacci quieres?: "))
    i = 0
    a , b = 0, 1
    while i < contador:
        a = a + b
        b = a - b
        i += 1
        print(f'({i})', a)

if __name__=='__main__':
    run()
