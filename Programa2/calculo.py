"""
Módulo 2: Cálculo de subtotal, descuento y total.

Contiene las funciones que realizan los cálculos numéricos de cada venta.
Si el subtotal supera los 150 soles se aplica un descuento del 10%.
"""

LIMITE_DESCUENTO = 150.0
PORCENTAJE_DESCUENTO = 0.10


def calcular_subtotal(precio_unitario, cantidad):
    """
    Calcula el subtotal a partir del precio unitario y la cantidad.
    Input:  La función recibe precio_unitario y cantidad
    Output: Retorna subtotal con 2 decimales
    """
    if precio_unitario <= 0:
        raise ValueError("El precio unitario debe ser mayor que cero.")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")
    subtotal = precio_unitario * cantidad
    return round(subtotal, 2)


def calcular_descuento(subtotal):
    """
    Calcula el descuento del 10% si el subtotal supera los 150 soles.
    Input:  La función recibe subtotal
    Output: Retorna descuento con 2 decimales si lo hubiera, sino descuento = 0.0
    """
    if subtotal < 0:
        raise ValueError("El subtotal no puede ser negativo.")
    if subtotal > LIMITE_DESCUENTO:
        descuento = subtotal * PORCENTAJE_DESCUENTO
    else:
        descuento = 0.0
    return round(descuento, 2)


def calcular_total(subtotal, descuento):
    """
    Calcula el total final restando el descuento al subtotal.
    Input:  La función recibe subtotal y descuento
    Output: Retorna total con 2 decimales
    """
    if subtotal < 0:
        raise ValueError("El subtotal no puede ser negativo.")
    if descuento < 0:
        raise ValueError("El descuento no puede ser negativo.")
    if descuento > subtotal:
        raise ValueError("El descuento no puede ser mayor que el subtotal.")
    total = subtotal - descuento
    return round(total, 2)
