from Test_Funcions import aplicar_funcion, function_return_limit


def bracket_minimum(f, a, b, n):

    if n <= 0:
        n = 1
    delta_x = (b - a) / n
    x1 = a
    x2 = x1 + delta_x
    if x2 >= b:
        return None
    x3 = x2 + delta_x
    while x3 <= b:
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
        if f1 >= f2 and f2 <= f3:
            return (x1, x3)
        x1 = x2
        x2 = x3
        x3 += delta_x
    return None


def optimize(f, a, b, n=10, m=None):

    bracket = bracket_minimum(f, a, b, n)
    if bracket is None:
        fa, fb = f(a), f(b)
        return a if fa <= fb else b
    x1, x3 = bracket
    if m is None:
        m = n
    if m <= 0:
        m = 1
    delta_x_refine = (x3 - x1) / m
    best_x = x1
    best_val = f(x1)

    best_X_array = []
    for i in range(1, m + 1):
        x = x1 + i * delta_x_refine
        val = f(x)
        if val < best_val:
            best_val = val
            best_x = x
        best_X_array.append(val)

    return {
        "minimum" : best_x,
        "array_steps": best_X_array,
    }


def ES_ejecutar(id_function):

    _var = function_return_limit(id_function)
    a = _var["lo"]
    b = _var["hi"]

    return optimize(aplicar_funcion(1),a,b)



