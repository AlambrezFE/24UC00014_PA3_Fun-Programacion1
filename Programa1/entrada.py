"""
    Se inserta un bucle while para permitir al usuario ingresar datos hasta que sean válidos.
    Se utiliza un bloque try-except para manejar posibles errores de conversión al intentar convertir la entrada a enteros.
"""
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
        
