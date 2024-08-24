def main():
    num = obtener_numero()
    miau(num)


def miau(n):
    for i in range(n):
        print("miau")
        
def obtener_numero():
    while True:
        n = int(input("Ingresa un valor n mayor que 0: "))
        if n < 0:
            continue
        else:
            break
        miau(n)



main()