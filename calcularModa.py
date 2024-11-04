def calcularModa (lri, d1, d2, c):
    resultado = lri + ((d1)/(d1+d2))*c
    return resultado

a = calcularModa(6,(19-12),(19-4),  2)

print(f"El resultado de la moda es: {a}")
