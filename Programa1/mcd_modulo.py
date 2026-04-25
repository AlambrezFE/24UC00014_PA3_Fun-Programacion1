from resto_modulo import calcular_resto

def obtener_mcd(x, y):
    # MCD. Mientras que el valor y no sea 0, seguimos calculando el resto
    while y > 0:
        resto = calcular_resto(x, y)
        x = y
        y = resto
    return x