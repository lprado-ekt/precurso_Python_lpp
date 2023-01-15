import math

opciones = 0


def suma():
    n1 = float(input("Proporciona un número: "))
    n2 = float(input("Proporciona otro número: "))
    return n1 + n2


def rest():
    n1 = float(input("Proporciona un número: "))
    n2 = float(input("Proporciona otro número: "))
    return n1 - n2


def divi():
    n1 = float(input("Proporciona un número: "))
    n2 = float(input("Proporciona otro número: "))
    return n1 / n2


def mult():
    n1 = float(input("Proporciona un número: "))
    n2 = float(input("Proporciona otro número: "))
    return n1 * n2


def expo():
    n1 = float(input("Proporciona el número base: "))
    n2 = float(input("Exponente: "))
    n3 = math.pow(n1, n2)
    return n3


def sen():
    n1 = float(input("Proporciona un número: "))
    n3 = math.sin(n1)
    n4 = math.degrees(n1)
    return n3, n4


def usalista():
    milista = []
    contador = int(input("¿Cuántos números a evaluar?"))
    i = 1
    while contador > 0:
        numero = float(input("# " + str(i) + ":"))
        milista.append(numero)
        i = i + 1
        contador = contador - 1
    nummayor = max(milista)
    nummenor = min(milista)
    print("Lista de números: ", milista)
    print("Número mayor: ", nummayor)
    print("Número menor: ", nummenor)
    print("\n")


def pintamenu():
    print("""
        *** Selecciona la operación que deseas realizar y proporciona 2 números ***
        1) Suma 
        2) Resta
        3) Multiplicación
        4) División
        5) Raíz n
        6) Exponente 
        7) Seno 
        8) Números Max y Min de una lista 
        9) Tangente 
        10) Apagar calculadora
        """)


while True:
    pintamenu()
    try:
        opciones = int(input("Selecciona una opción: "))
    except ValueError:
        print("¡Selecciona una opción válida!""\n")
        continue
    if opciones > 11:
        print("Selecciona una opción del 1 al 9 o selecciona opción 10 para salir""\n")
        continue

    print("\n")
    if opciones == 1:
        print("SUMA")
        print("El resultado es:", suma(), "\n")
    elif opciones == 2:
        print("RESTA")
        print("El resultado es:", rest(), "\n")
    elif opciones == 3:
        print("MULTIPLICACIÓN")
        print("El resultado es:", mult(), "\n")
    elif opciones == 4:
        print("DIVISIÓN")
        print("El resultado es:", divi(), "\n")
    elif opciones == 5:
        print("RAÍZ n")
        n3 = int(input("Proporcione un número mayor a cero"))
        if n3 > 0:
            print("Resultado (número entero no negativo):", math.isqrt(n3), "\n")
        else:
            print("Operación no realizada, el número debe ser mayor a 0")
    elif opciones == 6:
        print("Exponente")
        print("El resultado es:", expo(), "\n")
    elif opciones == 7:
        print("SENO")
        print("El seno en radianes y grados es: ", sen(), "\n")
    elif opciones == 8:
        print("Máximo - Mínimo", "\n")
        usalista()
    elif opciones == 9:
        print("***OPERACIÓN NO DISPONIBLE POR EL MOMENTO**")
    elif opciones == 10:
        print("Hasta luego")
        exit()
    else:
        print("Opción incorrecta")
        break
