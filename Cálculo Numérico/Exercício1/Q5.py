import numpy as np


def f(t):
    return 9 * np.exp(-t) * np.sin(2 * np.pi * t) - 3.5


def df(t):
    return -9 * np.exp(-t) * np.sin(2 * np.pi * t) + 18 * np.pi * np.exp(-t) * np.cos(2 * np.pi * t)


def newton_raphson(f, df, x0, precisao, max_iter=1000):
    iteracoes = 0  
    while iteracoes < max_iter:
        iteracoes += 1
        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
        x0 = x1
    return x0, iteracoes


intervalo = 1  # O período de sin(2 * pi * t) é 1 segundo
precisao = 1e-5
max_iter = 1000
raizes = []
t_inicio = 0
t_fim = 5  # Intervalo para procurar raízes


t_atual = t_inicio
while t_atual < t_fim:
    try:
        raiz, num_iteracoes = newton_raphson(f, df, t_atual, precisao, max_iter)
        if raiz not in raizes and t_inicio <= raiz <= t_fim:
            raizes.append(raiz)
    except ZeroDivisionError:
        pass
    
    t_atual += intervalo


raizes = sorted(set(round(t, 5) for t in raizes))

print("----------NEWTON-RAPHSON-------------------------")
print("---------------------------------------------")
print(f"Valores de t para I = 3.5 são:")
for raiz in raizes:
    print(f"t = {raiz:.5f} segundos")
print("---------------------------------------------")
