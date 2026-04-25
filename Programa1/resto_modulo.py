def calcular_resto(x, y):
    # fórmula: x % y = x - (int(x/y) * y)
    cociente = int(x / y)
    resto = x - (cociente * y)
    return resto