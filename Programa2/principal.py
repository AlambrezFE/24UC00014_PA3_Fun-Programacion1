"""
Módulo 5: Programa principal (integrador).

Integra los módulos de entrada, cálculo, reporte y acumulación
para gestionar las ventas diarias de la librería universitaria.
"""

import entrada
import calculo
import reporte
import acumulacion_total


def mostrar_bienvenida():
    """
    Muestra el encabezado del sistema al iniciar.
    Output: Imprime encabezado
    """
    print("=" * 45)
    print("   SISTEMA DE GESTIÓN DE VENTAS - LIBRERÍA")
    print("        Universidad - Jornada diaria")
    print("=" * 45 + "\n")


def main():
    """
    Función principal que coordina la ejecución del sistema. Llama a las funciones en orden para el workflow
    """
    mostrar_bienvenida()

    total_general = 0.0
    cantidad_ventas = 0
    continuar = True

    while continuar:
        try:
            print(f"--- Registro de venta N° {cantidad_ventas + 1} ---")

            nombre_libro = entrada.leer_nombre_libro()
            precio_unitario = entrada.leer_precio_unitario()
            cantidad = entrada.leer_cantidad()

            subtotal = calculo.calcular_subtotal(precio_unitario, cantidad)
            descuento = calculo.calcular_descuento(subtotal)
            total = calculo.calcular_total(subtotal, descuento)

            reporte.mostrar_reporte_venta(
                nombre_libro, precio_unitario, cantidad,
                subtotal, descuento, total
            )

            total_general = acumulacion_total.acumular_total(total_general, total)
            cantidad_ventas += 1

            continuar = entrada.leer_continuar()

        except ValueError as error:
            print(f"\n[ERROR DE VALIDACIÓN]: {error}")
            print("La venta no se registró. Intente nuevamente.\n")
        except Exception as error:
            print(f"\n[ERROR INESPERADO]: {error}")
            print("Se cancelará la venta actual.\n")
            continuar = entrada.leer_continuar()

    if cantidad_ventas == 0:
        print("\nNo se registraron ventas durante esta jornada.\n")
    else:
        acumulacion_total.mostrar_total_general(total_general, cantidad_ventas)


if __name__ == "__main__":
    main()
