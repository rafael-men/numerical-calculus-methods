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

# Exemplo de uso
f_str = "750 - 1800 * log((160000 / (160000 - 2600 * x)) * 9.81 * x)"  # Função definida pelo usuário
var_str = "x"  # Variável que o usuário quer usar (pode ser qualquer letra)
chute_inicial = "0.1"  # Chute inicial fornecido pelo usuário
precisao = "1e-10"  # Precisão fornecida pelo usuário

try:
    raiz, num_iteracoes = newton_raphson_str(f_str, var_str, chute_inicial, precisao)
    print("----------NEWTON - RAPHSON-------------------")
    print("---------------------------------------------")
    print(f"A raiz aproximada é: {raiz}")
    print(f"A raíz foi achada com: {num_iteracoes} iterações")
    print("---------------------------------------------")
except ValueError as e:
    print(f"Erro: {e}")
