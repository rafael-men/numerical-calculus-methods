import numpy as np


T0 = 300          # Temperatura de referência em Kelvin
T = 1000          # Temperatura em Kelvin
mu0 = 1360        # Mobilidade de referência em cm^2/(V.s)
q = 1.7e-19       # Carga do elétron em Coulombs
ni = 6.21e9       # Densidade de transporte intrínseca em cm^-3
rho_desejada = 6.5e-6 


def f(N):
    mu = mu0 * (T / T0)**(-2.42) 
    n = 0.5 * (N + np.sqrt(N**2 + 4 * ni**2)) 
    rho = 1 / (q * n * mu)  
    return rho - rho_desejada


def df(N):
    mu = mu0 * (T / T0)**(-2.42)
    d_n_dN = 0.5 * (1 + (N / np.sqrt(N**2 + 4 * ni**2)))
    d_rho_dN = -1 / (q * mu) * d_n_dN
    return d_rho_dN


def newton_raphson(f, df, x0, precisao):
    iteracoes = 0  
    while True:
        iteracoes += 1

        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
        x0 = x1


chute_inicial = 1e10 
precisao = 1e-5      

# Encontrar a densidade de dopagem
N, num_iteracoes = newton_raphson(f, df, chute_inicial, precisao)

print("----------NEWTON - RAPHSON-------------------")
print("---------------------------------------------")
print(f"A densidade de dopagem aproximada é: {N:.5e} cm^-3")
print(f"A raiz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
