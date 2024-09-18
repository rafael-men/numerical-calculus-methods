import numpy as np


def f(i):
    P = 35000  # Valor do veículo
    A = 8500   # Pagamento anual
    n = 7      # Número de anos
    return (P * i * (1 + i)**n) / ((1 + i)**n - 1) - A


def df(i):
    P = 35000  # Valor do veículo
    n = 7      # Número de anos
    numerator = P * (1 + i)**n * (1 + i) - P * i * (1 + i)**n * np.log(1 + i) * n
    denominator = ((1 + i)**n - 1)**2
    return numerator / denominator

def newton_raphson(f, df, x0, precisao):
    iteracoes = 0  
    while True:
        iteracoes += 1

        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
        x0 = x1

chute_inicial = 0.05  
precisao = 1e-5        

raiz, num_iteracoes = newton_raphson(f, df, chute_inicial, precisao)

raiz_percentual = raiz * 100

print("----------NEWTON - RAPHSON-------------------")
print("---------------------------------------------")
print(f"A taxa de juros anual aproximada é: {raiz_percentual:.5f}%")
print(f"A raiz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
