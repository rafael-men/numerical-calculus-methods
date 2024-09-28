import sympy as sp

def secant_method_str(f_str, var_str, x0, x1, precision):
    # Definir a variável simbólica com base na string fornecida pelo usuário
    var = sp.symbols(var_str)
    
    # Converter a string da função em uma expressão simbólica
    try:
        f = sp.sympify(f_str, locals={'sin': sp.sin, 'cos': sp.cos})
    except (sp.SympifyError, ValueError) as e:
        raise ValueError(f"Erro ao processar a função: {e}")
    
    # Converter a função simbólica em uma função numérica
    f_lambdified = sp.lambdify(var, f, 'numpy')
    
    iteration_count = 0
    
    while abs(x1 - x0) > precision:
        try:
            x2 = x1 - f_lambdified(x1) * (x1 - x0) / (f_lambdified(x1) - f_lambdified(x0))
        except ZeroDivisionError:
            raise ValueError("Denominador na fórmula da secante é zero. Tente valores diferentes.")
        
        x0 = x1
        x1 = x2
        
        iteration_count += 1

    return x1, iteration_count


if __name__ == "__main__":
    f_str = "x**2 - 4"  # Função definida pelo usuário
    var_str = "x"       # Variável que o usuário quer usar
    x0 = 1.0            # Chute inicial 1
    x1 = 3.0            # Chute inicial 2
    precision = 1e-5    # Precisão fornecida pelo usuário

    try:
        raiz, num_iteracoes = secant_method_str(f_str, var_str, x0, x1, precision)
        print("----------SECANTE-------------------")
        print("---------------------------------------------")
        print(f"A raiz aproximada é: {raiz}")
        print(f"A raíz foi achada com: {num_iteracoes} iterações")
        print("---------------------------------------------")
    except ValueError as e:
        print(f"Erro: {e}")
