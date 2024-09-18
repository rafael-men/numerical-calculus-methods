import numpy as np

# Constantes fornecidas
r = 2  # raio em metros
L = 5  # comprimento em metros
V = 8  # volume em metros cúbicos


def f(h):
    return (r**2 * np.arccos((r - h) / r) - (r - h) * np.sqrt(2 * r * h - h**2)) * L - V

# Derivada da função f em relação a h
def df(h):
  
    term1 = -r / np.sqrt(r**2 - (r - h)**2)  # Derivada do termo arccos
    term2 = (r - h) / np.sqrt(2 * r * h - h**2) - (r - h) * (r - (2 * h)) / (2 * np.sqrt(2 * r * h - h**2))  # Derivada do termo sqrt
    return (r**2 * (-term1) - (np.sqrt(2 * r * h - h**2)) - (r - h) * (-term2)) * L


def newton_raphson(f, df, x0, precisao):
    iteracoes = 0  
    while True:
        iteracoes += 1
        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
        x0 = x1


chute_inicial = 1.0  # Um valor razoável para a profundidade inicial
precisao = 1e-5       # Precisão desejada


profundidade, num_iteracoes = newton_raphson(f, df, chute_inicial, precisao)

print("----------NEWTON-RAPHSON-------------------------")
print("---------------------------------------------")
print(f"A profundidade correspondente ao volume de 8 m³ é: {profundidade:.5f} m")
print(f"A raiz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
