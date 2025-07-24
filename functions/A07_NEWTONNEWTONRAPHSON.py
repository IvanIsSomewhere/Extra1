from Test_Funcions import func_limit, aplicar_funcion,aplicar_funcion_d,aplicar_funcion_dd
from functions.A03_ELIMINACION_REGIONES import eliminar_regiones

def newton_raphson_minimize(f_prime, f_double_prime, x0, epsilon=1e-6, max_iter=1000):
    """
    Encuentra un mínimo local de una función usando el método de Newton-Raphson.

    Parámetros:
    f_prime (function): Función que calcula la primera derivada (f').
    f_double_prime (function): Función que calcula la segunda derivada (f'').
    x0 (float): Valor inicial (x^(1)).
    epsilon (float): Tolerancia para la convergencia (criterio de parada).
    max_iter (int): Número máximo de iteraciones permitidas.

    Retorna:
    tuple: (x_min, f_prime_min, iterations)
        x_min: Valor de x donde se alcanza el mínimo.
        f_prime_min: Valor de la derivada en x_min.
        iterations: Número de iteraciones realizadas.
    """
    x_k = x0
    iterations = 0
    f_prime_history = []

    for _ in range(max_iter):
        f_prime_k = f_prime(x_k)
        f_double_prime_k = f_double_prime(x_k)

        # Verificar que la segunda derivada no sea cero para evitar división por cero
        if abs(f_double_prime_k) < 1e-12:
            raise ValueError("Segunda derivada cercana a cero. El método no puede continuar.")

        # Actualizar x_k usando el metodo
        x_k_new = x_k - (f_prime_k / f_double_prime_k)
        f_prime_new = f_prime(x_k_new)

        f_prime_history.append(f_prime_new)
        iterations += 1

        # Criterio de parada
        if abs(f_prime_new) < epsilon:
            return f_prime_new, f_prime_history

        x_k = x_k_new
    return f_prime_new,iterations, f_prime_history


def ejecutar_nw(id,epsilon = 0.01):

    _f = aplicar_funcion(id)
    _fd = aplicar_funcion_d(id)
    _fdd = aplicar_funcion_dd(id)

    _a,_b = func_limit(id)
    _a = _a + (((_a+_b)/2) * 0.002)
    _b = _b - (((_a+_b)/2) * 0.002)
    _in_x = (_a + _b) / 2

    return newton_raphson_minimize(_fd, _fdd, _in_x, epsilon)


print(ejecutar_nw(1))

