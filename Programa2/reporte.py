"""
Módulo 3: Reporte individual de cada venta.

Muestra en pantalla los datos de la venta procesada:
nombre del libro, subtotal, descuento aplicado y total a pagar.
"""


def mostrar_reporte_venta(nombre_libro, precio_unitario, cantidad, subtotal, descuento, total):
    """
    Imprime un reporte formateado con el detalle de la venta.
    Input:  La función recibe nombre_libro, precio_unitario, cantidad, subtotal, descuento, total
    Output: Imprime los datos de reporte individual
    """
    if not isinstance(nombre_libro, str) or nombre_libro.strip() == "":
        raise ValueError("El nombre del libro es inválido.")
    if subtotal < 0 or descuento < 0 or total < 0:
        raise ValueError("Los montos no pueden ser negativos.")

    print("\n" + "=" * 45)
    print("       REPORTE DE VENTA INDIVIDUAL")
    print("=" * 45)
    print(f"Libro registrado : {nombre_libro}")
    print(f"Precio unitario  : S/. {precio_unitario:>8.2f}")
    print(f"Cantidad         : {cantidad:>9}")
    print("-" * 45)
    print(f"Subtotal         : S/. {subtotal:>8.2f}")
    if descuento > 0:
        print(f"Descuento (10%)  : S/. {descuento:>8.2f}")
    else:
        print(f"Descuento        : S/. {descuento:>8.2f}  (no aplica)")
    print(f"TOTAL A PAGAR    : S/. {total:>8.2f}")
    print("=" * 45 + "\n")
