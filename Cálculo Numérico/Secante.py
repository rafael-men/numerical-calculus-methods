def secant_method(f, x0, x1, precision):
  
    iteration_count = 0
    
    while abs(x1 - x0) > precision:
        try:
            
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        except ZeroDivisionError:
            raise ValueError("Denominador na fórmula da secante é zero. Tente valores diferentes.")
     
        x0 = x1
        x1 = x2
        
       
        iteration_count += 1

    return x1, iteration_count


if __name__ == "__main__":

    def func(x):
        return x**2 - 4  

   
    x0 = 1.0
    x1 = 3.0
    precision = 1e-5

    
    raiz, num_iteracoes = secant_method(func, x0, x1, precision)
print("----------SECANTE-------------------")
print("---------------------------------------------")
print(f"A raiz aproximada é: {raiz}")
print(f"A raíz foi achada com: {num_iteracoes} iterações")
print("---------------------------------------------")
