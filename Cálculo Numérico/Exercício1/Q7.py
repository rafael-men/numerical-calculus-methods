import numpy as np


R = 3  # raio do tanque em metros
V = 30  # volume em metros cúbicos
pi = np.pi


def f(h):
    return pi * h**2 * (3 * R - h) / 3 - V

def df(h):
    return 2 * pi * h * (3 * R - h) / 3 - pi * h**2 / 3


def newton_raphson(f, df, x0, precisao, max_iter=1000):
    iteracoes = 0
    while iteracoes < max_iter:
        iteracoes += 1
        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
        x0 = x1
    return x0, iteracoes

chute_inicial = 2  # valor razoável para a profundidade inicial
precisao = 1e-5     # Precisão desejada

# Encontrar a profundidade
profundidade, num_iteracoes = newton_raphson(f, df, chute_inicial, precisao)

print("----------NEWTON-RAPHSON-------------------------")
print("---------------------------------------------")
print(f"A profundidade necessária para armazenar 30 m³ é: {profundidade:.5f} metros")
print(f"A raiz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
