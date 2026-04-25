def leer_datos():
    print("|-|-|- Ingreso de Datos -|-|-|")
    while True:
        try:
            a = int(input("Ingrese el primer número entero positivo: "))
            b = int(input("Ingrese el segundo número entero positivo: "))
            if a > 0 and b > 0:
                return a, b
            else:
                print("Vamos..... , ingrese solo números mayores a cero!!!.")
        except ValueError:
            print("Entrada invalida...... Asegúrese de ingresar números enteros.")
        
# se ingreso manejo de excepciones (Exception Handling) y validacion de datos de entrada.