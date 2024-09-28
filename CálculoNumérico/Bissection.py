import sympy as sp
import numpy as np

def bisseccao_str(f_str, var_str, xa, xb, precisao):
    # Definir a variável simbólica com base na string fornecida pelo usuário
    var = sp.symbols(var_str)
    
    # Converter a string da função em uma expressão simbólica
    try:
        f = sp.sympify(f_str, locals={'log': sp.log, 'sin': sp.sin, 'cos': sp.cos})
    except (sp.SympifyError, ValueError) as e:
        raise ValueError(f"Erro ao processar a função: {e}")
    
    # Converter a função simbólica em uma função numérica
    f_lambdified = sp.lambdify(var, f, 'numpy')
    
    # Verificar se a função tem sinais opostos nos limites xa e xb
    fa = f_lambdified(xa)
    fb = f_lambdified(xb)
    
    print(f"f({xa}) = {fa}, f({xb}) = {fb}")  # Imprimir os valores da função
    
    if fa * fb > 0:
        print("A função deve ter sinais opostos em xa e xb.")
        return None  # Retornar None se não houver raiz

    iteracoes = 0  
    print("\n----------BISSECÇÃO--------------------------")
    print("Iteração |     xa      |     xb      |     xm      |   f(xa)   |   f(xb)   |   f(xm)   |  Precisão")
    print("---------------------------------------------------------------------------------------------------")
    
    while (xb - xa) / 2.0 > precisao:
        iteracoes += 1
        xm = (xa + xb) / 2.0
        fxm = f_lambdified(xm)

        # Imprimir valores da iteração atual
        print(f"{iteracoes:<9} | {xa:<12.6f} | {xb:<12.6f} | {xm:<12.6f} | {fa:<10.6f} | {fb:<10.6f} | {fxm:<10.6f} | {abs(xb - xa):<12.6f}")

        if fxm == 0 or (xb - xa) / 2.0 < precisao:
            return xm, iteracoes
        
        if fxm * fa < 0:
            xb = xm
            fb = fxm  # Atualiza fb
        else:
            xa = xm
            fa = fxm  # Atualiza fa

    raiz = (xa + xb) / 2.0
    print(f"{iteracoes + 1:<9} | {xa:<12.6f} | {xb:<12.6f} | {(xa + xb) / 2.0:<12.6f} | {fa:<10.6f} | {fb:<10.6f} | {f_lambdified(raiz):<10.6f} | {abs(xb - xa):<12.6f}")
    return raiz, iteracoes

# Função para encontrar um intervalo válido
def encontrar_intervalo(f_lambdified, test_xa, test_xb, num_points=100):
    x_values = np.linspace(test_xa, test_xb, num_points)
    f_values = [f_lambdified(x) for x in x_values]

    # Verificando onde há mudança de sinal
    for i in range(len(f_values) - 1):
        if f_values[i] * f_values[i + 1] < 0:
            return x_values[i], x_values[i + 1]
    return None  # Retornar None se não encontrar

# Exemplo de uso
f_str = "750 - 1800 * log((160000 / (160000 - 2600 * x))) * 9.81 * x"  # Função definida pelo usuário
var_str = "x"  # Variável que o usuário quer usar

# Definindo um intervalo de teste
test_xa = 4   # Limite inferior (ajustado)
test_xb = 200   # Limite superior (ajustado)

# Avaliando a função para encontrar um intervalo onde a função muda de sinal
try:
    # Criar a função simbólica e lambdificada para encontrar o intervalo
    var = sp.symbols(var_str)
    f = sp.sympify(f_str, locals={'log': sp.log, 'sin': sp.sin, 'cos': sp.cos})
    f_lambdified = sp.lambdify(var, f, 'numpy')

    # Encontrar o intervalo
    intervalo = encontrar_intervalo(f_lambdified, test_xa, test_xb)
    if intervalo is not None:
        xa, xb = intervalo
        precisao = 1e-5  # Precisão fornecida pelo usuário

        resultado = bisseccao_str(f_str, var_str, xa, xb, precisao)
        if resultado is not None:
            raiz, num_iteracoes = resultado
            print("---------------------------------------------")
            print(f"A raiz aproximada é: {raiz}")
            print(f"A raíz foi achada com {num_iteracoes} iterações.")
            print("---------------------------------------------")
    else:
        print("Não foi encontrado um intervalo onde a função muda de sinal.")
except ValueError as e:
    print(f"Erro: {e}")
