# Calculadora básica

while True:
    symbol = input("Indique la operación (+, -, *, /, %, **, //) o 'x' para salir: ")
    
   
    if symbol == "x":
        print("Saliendo de la calculadora...")
        break

    if symbol == "+":
        print("Inserte el primer número")
        a = int(input())
        print("Inserte el segundo número")
        b = int(input())
        c = a + b
        print(c)
    elif symbol == "-":
        print("Inserte el primer número")
        a = int(input())
        print("Inserte el segundo número")
        b = int(input())
        c = a - b
        print(c)
    elif symbol == "*":
        print("Inserte el primer número")
        a = int(input())
        print("Inserte el segundo número")
        b = int(input())
        c = a * b
        print(c)
    elif symbol == "/":
        print("Inserte el primer número")
        a = int(input())
        print("Inserte el segundo número")
        b = int(input())
        c = a / b
        print(c)
    elif symbol == "%":
        print("Inserte el primer número")
        a = int(input())
        print("Inserte el segundo número")
        b = int(input())
        c = a % b
        print(c)
    elif symbol == "**":
        print("Inserte la base")
        a = int(input())
        print("Inserte el exponente")
        b = int(input())
        c = a ** b
        print(c)
    elif symbol == "//":
        print("Inserte el primer número")
        a = int(input())
        print("Inserte el segundo número")
        b = int(input())
        c = a // b
        print(c)
    
    else:
        print("Error: operación no válida")

    # Pausa para que el usuario vea el resultado antes de la siguiente iteración
    input("Presiona Enter para continuar...")

