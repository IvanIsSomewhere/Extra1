def secant_minimize(f_prime, x0, x1, epsilon=1e-6, max_iter=1000):

    iterations = 0
    f_prime_x0 = f_prime(x0)
    f_prime_x1 = f_prime(x1)

    for _ in range(max_iter):
        if abs(f_prime_x1) < epsilon:
            break

        # Evitar división por cero
        if abs(f_prime_x1 - f_prime_x0) < 1e-10:
            break

        # Fórmula de la secante
        x_next = x1 - (f_prime_x1 * (x1 - x0)) / (f_prime_x1 - f_prime_x0)

        # Actualizar valores
        x0, x1 = x1, x_next
        f_prime_x0, f_prime_x1 = f_prime_x1, f_prime(x_next)
        iterations += 1

    return x1, iterations


# Ejemplo de uso
def ejecutar_sec(id,name):
    hola = 1