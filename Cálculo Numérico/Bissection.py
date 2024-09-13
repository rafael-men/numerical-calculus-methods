import math

def bisseccao(f, xa, xb, precisao):
    if f(xa) * f(xb) > 0:
        print("A função deve ter sinais opostos em xa e xb.")
        return None

  
    iteracoes = 0  
    while (xb - xa) / 2.0 > precisao:
        iteracoes += 1
        xm = (xa + xb) / 2.0
        
      
        if f(xm) == 0 or (xb - xa) / 2.0 < precisao:
            return xm, iteracoes
        
   
        if f(xm) * f(xa) < 0:
            xb = xm
        else:
            xa = xm

    return (xa + xb) / 2.0, iteracoes

def f(x):
    return math.sin(10*x) + math.cos(3*x)


raiz, num_iteracoes = bisseccao(f, 3, 6, 1e-5)
print("----------BISSECÇÃO--------------------------")
print("---------------------------------------------")
print(f"A raiz aproximada é: {raiz}")
print(f"A raíz foi achada com {num_iteracoes} iterações.")
print("---------------------------------------------")
