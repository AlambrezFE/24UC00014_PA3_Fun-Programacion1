from resto_modulo import calcular_resto
"""
se importa la función calcular_resto desde el módulo resto_modulo para ser utilizada en el cálculo del MCD.
un buble caso si el valor de y es mayor a 0, caso contrario si Y es igual a 0, retornara el valor de X.
"""
def obtener_mcd(x, y):
    while y > 0:
        resto = calcular_resto(x, y)
        x = y
        y = resto
    return x


