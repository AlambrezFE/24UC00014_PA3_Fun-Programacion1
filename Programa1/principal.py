import entrada
import mcd_modulo
import salida

def ejecutar_sistema():
    print("BIENVENIDO AL CALCULADOR DE MCD (MÉTODO EUCLIDES)")
    
    while True:
        # Lectura
        num1, num2 = entrada.leer_datos()
        
        # Cálculo
        resultado_mcd = mcd_modulo.obtener_mcd(num1, num2)
        
        # Salida
        salida.mostrar_resultado(num1, num2, resultado_mcd)
        
        # repetición
        continuar = input("¿Desea realizar otro cálculo? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por usar el software educativo. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    ejecutar_sistema()