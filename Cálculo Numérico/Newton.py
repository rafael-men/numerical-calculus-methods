def newton_raphson(f, df, x0, precisao):
    iteracoes = 0  
    while True:
        iteracoes += 1

        x1 = x0 - f(x0) / df(x0)
        
        
        if abs(x1 - x0) < precisao:
            return x1, iteracoes
        
    
        x0 = x1

def f(x):
    return x**2 - 4

def df(x):
    return 2 * x


raiz, num_iteracoes = newton_raphson(f, df, 3, 0.0001)
print("----------NEWTON - RAPHSON-------------------")
print("---------------------------------------------")
print(f"A raiz aproximada é: {raiz}")
print(f"A raíz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
