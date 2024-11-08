def trapezoidal_rule_composite(f, a, b, n):
    """
    Calcula a integral de uma função f(x) no intervalo [a, b] usando a regra do trapézio composto.
    """
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        integral += 2 * f(x_i)

    return (h / 2) * integral

# Definindo a função f(x) = x**2 para integrar no intervalo [0, 1]
f = lambda x: x**2
a = 0  # Limite inferior da integração
b = 1  # Limite superior da integração
n = 10  # Número de subintervalos

integral = trapezoidal_rule_composite(f, a, b, n)

print("--------------------Trapézio Composto -------------------------------------")
print(f"A integral aproximada de f(x) = x^2 no intervalo [{a}, {b}] com {n} subintervalos é: {integral}")
print("--------------------------------------------------------------------------")
