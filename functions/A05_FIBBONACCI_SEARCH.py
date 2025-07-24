import math

from Test_Funcions import aplicar_funcion, function_return_limit


def fibonacci_search(f, a, b, n, epsilon):
    # Precompute Fibonacci numbers up to F_{n+1}
    F = [0, 1]
    for i in range(2, n + 2):
        F.append(F[-1] + F[-2])

    L = b - a
    k = 2
    x1 = a + (F[n - k + 1] / F[n + 1]) * L
    x2 = b - (F[n - k + 1] / F[n + 1]) * L
    f_x1 = f(x1)
    f_x2 = f(x2)

    ab_history = [[],[]]


    while (b - a) > epsilon and k <= n:
        if f_x1 < f_x2:
            b = x2
            x2 = x1
            f_x2 = f_x1
            k += 1
            if k <= n:
                x1 = a + (F[n - k + 1] / F[n + 1]) * (b - a)
                f_x1 = f(x1)
        else:
            a = x1
            x1 = x2
            f_x1 = f_x2
            k += 1
            if k <= n:
                x2 = b - (F[n - k + 1] / F[n + 1]) * (b - a)
                f_x2 = f(x2)
        ab_history[0].append(a)
        ab_history[1].append(b)

    # Return the midpoint of the final interval as the approximate minimizer
    return a,b,ab_history


def execute_Fib(id_function,epsi = 0.01):
    _f = aplicar_funcion(id_function)

    _var = function_return_limit(id_function)
    _a = _var["lo"]
    _b = _var["hi"]

    a,b,ab_history = fibonacci_search(_f,_a,_b,1000,epsi)

    return a,b,ab_history