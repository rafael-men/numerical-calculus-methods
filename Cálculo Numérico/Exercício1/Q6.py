import numpy as np

v0 = 30  # velocidade inicial em m/s
x = 90   # distância em metros
g = 9.81 # aceleração devido à gravidade em m/s^2


def f(theta):
    theta_rad = np.radians(theta)  # converter para radianos
    return (g * x) / (2 * v0**2) - np.tan(theta_rad) / (np.cos(theta_rad)**2)


def df(theta):
    theta_rad = np.radians(theta)  # converter para radianos
    tan_theta = np.tan(theta_rad)
    cos_theta = np.cos(theta_rad)
    sec_theta = 1 / cos_theta
    return - (g * x) / (2 * v0**2) - (np.sin(theta_rad) * (sec_theta**2) * cos_theta) / (cos_theta**4)


def newton_raphson(f, df, x0, precisao, max_iter=1000):
    iteracoes = 0  
    while iteracoes < max_iter:
        iteracoes += 1
        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
        x0 = x1
    return x0, iteracoes


chute_inicial = 45  # Um valor razoável para o ângulo inicial
precisao = 1e-5     # Precisão desejada


angulo, num_iteracoes = newton_raphson(f, df, chute_inicial, precisao)

print("----------RESULTADOS-------------------------")
print("---------------------------------------------")
print(f"O ângulo inicial necessário é: {angulo:.5f} graus")
print(f"A raiz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
