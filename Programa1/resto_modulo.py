def calcular_resto(x, y):
    # fórmula del algoritmo de euclides: x % y = x - (int(x/y) * y)
    cociente = int(x / y)
    resto = x - (cociente * y)
    return resto

