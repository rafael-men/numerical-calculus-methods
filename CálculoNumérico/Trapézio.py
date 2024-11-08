def trapezoidal_rule(f, a, b):
    """
    Calcula a integral de uma função f(x) no intervalo [a, b] usando a regra do trapézio simples.
    """
    return (b - a) * (f(a) + f(b)) / 2


# Definindo a função f(x) = x**2 para integrar no intervalo [0, 1]
f = lambda x: x**2
a = 0 # Limite inferior da integração.
b = 1 # Limite superior da integração.


integral = trapezoidal_rule(f, a, b)
print("--------------------Trapézio Simples -------------------------------------")
print(f"A integral aproximada de f(x) = x^2 no intervalo [{a}, {b}] é: {integral}")
print("--------------------------------------------------------------------------")
