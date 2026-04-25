"""
Módulo 1: Lectura de datos de entrada.

Contiene funciones para solicitar y validar los datos de cada venta:
nombre del libro, precio unitario y cantidad adquirida.
"""


def leer_nombre_libro():
    """
    Solicita el nombre del libro, valida que no esté vacío ni tenga números en su nombre.
    Input:  Solicita nombre del libro y lo almacena en la variable nombre
    Output: Retorna nombre
    """
    while True:
        try:
            nombre = input("Ingrese el nombre del libro: ").strip()
            if nombre == "":
                raise ValueError("El nombre del libro no puede estar vacío.")
            if any(caracter.isdigit() for caracter in nombre):
                raise ValueError("El nombre del libro no debe contener números.")
            return nombre
        except ValueError as error:
            print(f"Error: {error} Intente nuevamente.\n")


def leer_precio_unitario():
    """
    Solicita el precio unitario, valida que el precio no sea nulo y que sea un número positivo.
    Input:  Solicita precio unitario y lo almacena en la variable entrada (alcance local)
    Output: Retorna entrada
    """
    while True:
        try:
            entrada = input("Ingrese el precio unitario (S/.): ").strip()
            if entrada == "":
                raise ValueError("Debe ingresar un precio.")
            precio = float(entrada)
            if precio <= 0:
                raise ValueError("El precio debe ser mayor que cero.")
            return precio
        except ValueError as error:
            mensaje = str(error)
            if "could not convert" in mensaje:
                print("Error: Debe ingresar un valor numérico válido. Intente nuevamente.\n")
            else:
                print(f"Error: {mensaje} Intente nuevamente.\n")


def leer_cantidad():
    """
    Solicita la cantidad de libros, valida que no sea nula, sea un entero positivo y sea mayor que 0.
    Input:  Solicita cantidad y lo almacena en la variable entrada (alcance local)
    Output: Retorna entrada
    """
    while True:
        try:
            entrada = input("Ingrese la cantidad adquirida: ").strip()
            if entrada == "":
                raise ValueError("Debe ingresar una cantidad.")
            if not entrada.isdigit():
                raise ValueError("La cantidad debe ser un número entero positivo.")
            cantidad = int(entrada)
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero.")
            return cantidad
        except ValueError as error:
            print(f"Error: {error} Intente nuevamente.\n")


def leer_continuar():
    """
    Pregunta al usuario si desea registrar otra venta. Retorna True/False.
    Input:  Solicita 's' o 'n' para ingresar o no otro libro
    Output: Retorna True o False
    """
    while True:
        try:
            respuesta = input("¿Desea registrar una nueva venta? (s/n): ").strip().lower()
            if respuesta == "":
                raise ValueError("Debe ingresar 's' para sí o 'n' para no.")
            if respuesta not in ("s", "n", "si", "no"):
                raise ValueError("Respuesta no válida. Use 's' o 'n'.")
            return respuesta in ("s", "si")
        except ValueError as error:
            print(f"Error: {error} Intente nuevamente.\n")
