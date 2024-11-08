import sympy as sp

def newton_raphson_str(f_str, var_str, chute_inicial, precisao):
    # Definir a variável simbólica com base na string fornecida pelo usuário
    var = sp.symbols(var_str)
    
    # Converter a string da função em uma expressão simbólica
    try:
        f = sp.sympify(f_str, locals={'log': sp.log})
    except (sp.SympifyError, ValueError) as e:
        raise ValueError(f"Erro ao processar a função: {e}")
    
    # Calcular a derivada de f simbolicamente em relação à variável
    df = sp.diff(f, var)
    
    # Converter as funções simbólicas em funções numéricas
    f_lambdified = sp.lambdify(var, f, 'numpy')
    df_lambdified = sp.lambdify(var, df, 'numpy')
    
    iteracoes = 0  
    x0 = float(chute_inicial)  # Garantir que o chute inicial seja um número

    while True:
        iteracoes += 1
        
        try:
            # Avaliar a função e a derivada para o valor atual de x0
            f_valor = f_lambdified(x0)
            df_valor = df_lambdified(x0)
            
            # Imprimir valores de depuração
            print(f"Iteração {iteracoes}: x0 = {x0}, f(x0) = {f_valor}, df(x0) = {df_valor}")
            
            # Aplicar o método de Newton-Raphson
            if df_valor == 0:
                raise ValueError("Derivada é zero, método não pode continuar.")
            
            x1 = x0 - f_valor / df_valor
        
            if abs(x1 - x0) < float(precisao):
                return x1, iteracoes
            
            x0 = x1
        
        except ZeroDivisionError:
            raise ValueError("Divisão por zero ocorreu no cálculo da derivada.")
        except ValueError as ve:
            raise ValueError(f"Erro no cálculo: {ve}")

# Função fornecida
f_str = "4 + x * cos(x)"  
var_str = "x"  
chute_inicial_1 = "1"  # Primeiro chute inicial
chute_inicial_2 = "-2"  # Chute inicial negativo
precisao = "1e-5"  # Precisão

try:
    raiz_1, num_iteracoes_1 = newton_raphson_str(f_str, var_str, chute_inicial_1, precisao)
    raiz_2, num_iteracoes_2 = newton_raphson_str(f_str, var_str, chute_inicial_2, precisao)
    
    print("----------NEWTON - RAPHSON-------------------")
    print("---------------------------------------------")
    print(f"A primeira raiz aproximada é: {raiz_1}, encontrada em {num_iteracoes_1} iterações")
    print(f"A segunda raiz aproximada é: {raiz_2}, encontrada em {num_iteracoes_2} iterações")
    print("---------------------------------------------")
except ValueError as e:
    print(f"Erro: {e}")
