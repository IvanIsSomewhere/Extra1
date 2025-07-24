from Test_Funcions import func_limit, aplicar_funcion, aplicar_funcion_d, aplicar_funcion_dd


def metodo_biseccion(f_derivada, a, b, epsilon=1e-6, max_iter=1000):

    # Verificación inicial de las condiciones del intervalo
    if f_derivada(a) >= 0 or f_derivada(b) <= 0:
        raise ValueError("El intervalo [a, b] no cumple con f'(a) < 0 y f'(b) > 0.")

    x1, x2 = a, b
    historial = []

    for iteracion in range(max_iter):
        z = (x1 + x2) / 2
        derivada_z = f_derivada(z)
        historial.append(z)

        # Criterio de parada
        if abs(derivada_z) <= epsilon:
            print(f"Convergencia alcanzada en {iteracion + 1} iteraciones.")
            return z, historial

        # Actualización del intervalo
        if derivada_z < 0:
            x1 = z
        elif derivada_z > 0:
            x2 = z

    print("Advertencia: Máximo de iteraciones alcanzado.")
    return z, historial

# Ejemplo de uso

def ejecutar_biseccion(id,epsilon = 0.01):
    _f = aplicar_funcion(id)
    _fd = aplicar_funcion_d(id)
    _fdd = aplicar_funcion_dd(id)

    _a, _b = func_limit(id)

    _l = (_b - _a)

    step = _l / 10000
    x1 = _a+ step
    x2 = _b



    print(_fd(x1))


    print(_fd(x2))

    return metodo_biseccion(_fd,_a,_b, epsilon)


ejecutar_biseccion(3)