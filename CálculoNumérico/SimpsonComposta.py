def simpson_composite(f, a, b, n):
    """
    Calcula a integral de uma função f(x) no intervalo [a, b] usando a regra de Simpson composta.
    
    """
    # Verificar se o número de subintervalos é par
    if n % 2 != 0:
        raise ValueError("O número de subintervalos n deve ser par.")

    
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        coeficiente = 4 if i % 2 != 0 else 2
        integral += coeficiente * f(x_i)

  
    return (h / 3) * integral

# Exemplo de uso
# Definindo a função f(x) = x**2 para integrar no intervalo [0, 1]
f = lambda x: x**2
a = 0  # Limite inferior da integração
b = 1  # Limite superior da integração
n = 10  # Número de subintervalos (deve ser par)


integral = simpson_composite(f, a, b, n)

print("--------------------Regra de Simpson Composta -------------------------------------")
print(f"A integral aproximada de f(x) = x^2 no intervalo [{a}, {b}] com {n} subintervalos é: {integral}")
print("-----------------------------------------------------------------------------------")
