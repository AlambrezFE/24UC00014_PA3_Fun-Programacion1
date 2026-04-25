"""
Módulo 4: Acumulación del total general.

Lleva el control del monto total acumulado de todas las ventas
realizadas durante la jornada y muestra el reporte final.
"""


def acumular_total(total_general, total_venta):
    """
    Suma el total de la venta actual al total general acumulado.
    Input:  La función recibe total_general, total_venta
    Output: Retorna nuevo_total con 2 decimales
    """
    if total_general < 0:
        raise ValueError("El total general no puede ser negativo.")
    if total_venta < 0:
        raise ValueError("El total de la venta no puede ser negativo.")
    nuevo_total = total_general + total_venta
    return round(nuevo_total, 2)


def mostrar_total_general(total_general, cantidad_ventas):
    """
    Imprime el resumen final con el monto total acumulado de la jornada.
    Input:  La función recibe total_general, cantidad_ventas
    Output: Imprime los datos del resumen de la jornada
    """
    if total_general < 0:
        raise ValueError("El total general no puede ser negativo.")
    if cantidad_ventas < 0:
        raise ValueError("La cantidad de ventas no puede ser negativa.")

    print("\n" + "*" * 45)
    print("       RESUMEN FINAL DE LA JORNADA")
    print("*" * 45)
    print(f"Cantidad de ventas registradas : {cantidad_ventas}")
    print(f"TOTAL GENERAL ACUMULADO        : S/. {total_general:.2f}")
    print("*" * 45)
    print("Gracias por usar el sistema Libros Académicos.\n¡Hasta pronto!\n")
