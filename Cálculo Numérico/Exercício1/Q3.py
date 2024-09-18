import numpy as np
import matplotlib.pyplot as plt


a0 = 0.99403
a1 = 1.671e-4
a2 = 9.7215e-8
a3 = -9.5838e-11
a4 = 1.9520e-14

# Função que calcula Cp
def Cp(T):
    return a0 + a1 * T + a2 * T**2 + a3 * T**3 + a4 * T**4

# Função que define a diferença entre Cp(T) e o valor desejado
def f(T):
    return Cp(T) - 1.1

# Derivada da função em relação a T
def df(T):
    return a1 + 2 * a2 * T + 3 * a3 * T**2 + 4 * a4 * T**3

# Método de Newton-Raphson
def newton_raphson(f, df, x0, precisao):
    iteracoes = 0  
    while True:
        iteracoes += 1
        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
        x0 = x1

# Gerar o gráfico
T_values = np.linspace(0, 1200, 500)
Cp_values = Cp(T_values)

plt.plot(T_values, Cp_values, label='$C_p$ versus $T$')
plt.axhline(y=1.1, color='r', linestyle='--', label='Cp = 1.1 kJ/(Kg·K)')
plt.xlabel('Temperatura (K)')
plt.ylabel('$C_p$ (kJ/(Kg·K))')
plt.title('Gráfico de $C_p$ versus Temperatura')
plt.legend()
plt.grid(True)
plt.show()

chute_inicial = 500  # Chute inicial para a temperatura
precisao = 1e-5       # Precisão desejada

temperatura, num_iteracoes = newton_raphson(f, df, chute_inicial, precisao)

print("----------NEWTON-RAPHSON-------------------------")
print("---------------------------------------------")
print(f"A temperatura correspondente a Cp = 1.1 kJ/(Kg·K) é: {temperatura:.5f} K")
print(f"A raiz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
