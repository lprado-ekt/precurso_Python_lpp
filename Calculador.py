
    print("""
    *** Selecciona la operación que deseas realizar y proporciona 2 números ***
    1) Suma 
    2) Resta
    3) Multiplición
    4) Divición
    5) Raiz n
    6) Exponente 
    7) Seno 
    8) Coseno 
    9) Tangente 
    10) Apagar calculadora
    """)
    while True:
        try:
            opciones = int(input("Seleciona una opción: "))
        except ValueError:
            print("¡Selecciona una opción válida!""\n")
            continue
        if opciones > 11:
            print("Selecciona una opción del 1 al 9 o selecciona opción 10 para salir""\n")
            continue
        else:
            break
    if opciones == 1:
        print("SUMA")
    elif opciones == 2:
        print("RESTA")
    elif opciones == 3:
        print("MULTIPLIACIÓN")
    elif opciones == 4:
        print("MULTIPLIACIÓN")
    elif opciones == 5:
        print("MULTIPLIACIÓN")
    elif opciones == 6:
        print("MULTIPLIACIÓN")
    elif opciones == 7:
        print("MULTIPLIACIÓN")
    elif opciones == 8:
        print("***OPERACIÓN NO DISPONIBLE POR EL MOMENTO**")
    elif opciones == 9:
        print("***OPERACIÓN NO DISPONIBLE POR EL MOMENTO**")
    elif opciones == 10:
        print("Hasta luego")
        break
    else:
        print("Opción incorrecta")
