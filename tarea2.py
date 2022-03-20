def factorial(n):
    resultado = 1
    if n == 1:
        return resultado
    else:
        for i in range(2, n+1):
            resultado *= i
    return resultado