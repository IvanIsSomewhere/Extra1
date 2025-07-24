from fontTools.misc.bezierTools import epsilon

from Test_Funcions import aplicar_funcion, func_limit


def fase_acotamiento(f, x0, delta, max_iter=100):

    # PASO 1: Inicialización
    k = 0
    print(f"Iteración {k}:")
    print(f"  x0 = {x0:.4f}, f(x0) = {f(x0):.4f}, Δ = {delta:.4f}")

    # PASO 2: Determinar dirección de Δ
    delta_abs = abs(delta)
    f_left = f(x0 - delta_abs)
    f_center = f(x0)
    f_right = f(x0 + delta_abs)

    ab_history =[[],[]]


    print(
        f"  f({x0 - delta_abs:.4f}) = {f_left:.4f}, f({x0:.4f}) = {f_center:.4f}, f({x0 + delta_abs:.4f}) = {f_right:.4f}")

    if f_left >= f_center >= f_right:
        Delta = delta_abs  # Dirección positiva
        print("  Condición 1: f(x0-|Δ|) ≥ f(x0) ≥ f(x0+|Δ|) → Δ positivo")
    elif f_left <= f_center <= f_right:
        Delta = -delta_abs  # Dirección negativa
        print("  Condición 2: f(x0-|Δ|) ≤ f(x0) ≤ f(x0+|Δ|) → Δ negativo")
    else:
        # Si no se cumple ninguna condición, devolver intervalo inicial
        print("  No se cumplen condiciones → Usar intervalo inicial")
        a = min(x0 - delta_abs, x0 + delta_abs)
        b = max(x0 - delta_abs, x0 + delta_abs)
        return a, b

    # Valores iniciales
    x_k = x0
    f_k = f_center
    x_history = [x0]  # Guardar historial de puntos
    l_history = []
    # Bucle principal (k = 0, 1, 2, ..., max_iter-1)
    for k in range(1, max_iter + 1):
        # PASO 3: Calcular nuevo punto
        step_size = 2 ** (k - 1) * Delta
        x_k1 = x_k + step_size

        # PASO 4: Evaluar función en nuevo punto
        f_k1 = f(x_k1)
        x_history.append(x_k1)

        print(f"\nIteración {k}:")
        print(f"  x_{k - 1} = {x_k:.4f}, f(x_{k - 1}) = {f_k:.4f}")
        print(f"  Paso: 2^{k - 1}*Δ = {2 ** (k - 1)}*{Delta:.4f} = {step_size:.4f}")
        print(f"  x_{k} = {x_k:.4f} + {step_size:.4f} = {x_k1:.4f}")
        print(f"  f(x_{k}) = {f_k1:.4f}")

        # Comprobar condición de parada
        if f_k1 >= f_k:
            print(f"\nCondición de parada: f(x_{k}) = {f_k1:.4f} ≥ f(x_{k - 1}) = {f_k:.4f}")
            a = min(x_history[-3], x_k1) if len(x_history) >= 3 else min(x0, x_k1)
            b = max(x_history[-3], x_k1) if len(x_history) >= 3 else max(x0, x_k1)
            print(f"  Intervalo final: [{a:.4f}, {b:.4f}]")
            return (b-a), x_history

        # Actualizar para siguiente iteración
        x_k = x_k1
        f_k = f_k1

    # Si se alcanza el máximo de iteraciones sin encontrar mínimo
    print(f"\nMáximo de iteraciones alcanzado ({max_iter})")
    a = min(x_history[0], x_history[-1])
    b = max(x_history[0], x_history[-1])
    l_history.append(b-a)
    print(f"  Intervalo final: [{a:.4f}, {b:.4f}]")
    return (b-a), l_history




def execute_FA(id):
    f = aplicar_funcion(id)
    a,b = func_limit(id)
    x0 = (a+b)/ 2

    return fase_acotamiento(f,x0,0.2)