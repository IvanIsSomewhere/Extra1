from Test_Funcions import aplicar_funcion, function_return_limit


def interval_halving(f, a, b, epsilon=1e-6, max_iter=1000):

    # Step 1: Initial setup
    L = b - a
    x_m = (a + b) / 2.0
    f_m = f(x_m)
    iter_count = 0

    x_history = [[a],[b]]

    # Iterate until interval length < epsilon or max iterations reached
    while abs(L) >= epsilon and iter_count < max_iter:
        iter_count += 1

        # Step 2: Calculate quarter points
        x1 = a + L / 4.0
        x2 = b - L / 4.0
        f1 = f(x1)
        f2 = f(x2)


        # Step 3: Check left quarter point
        if f1 < f_m:
            b = x_m  # Update upper bound
            x_m = x1  # New midpoint
            f_m = f1  # Update function value
        # Step 4: Check right quarter point
        elif f2 < f_m:
            a = x_m  # Update lower bound
            x_m = x2  # New midpoint
            f_m = f2  # Update function value
        # Neither quarter point is better
        else:
            a = x1  # Shrink interval left
            b = x2  # Shrink interval right
            # x_m remains unchanged (still valid midpoint)

        x_history[0].append(a)
        x_history[1].append(b)

        # Step 5: Update interval length
        L = b - a

    return x_m, x_history

def IHM_execute(id,epsi = 0.001):

    _f = aplicar_funcion(id)
    _limits = function_return_limit(id)

    _a = _limits['lo']
    _b = _limits['hi']

    x_history = []
    mid_x, x_history = interval_halving(_f,_a,_b,epsi)

    return mid_x, x_history
    #what the hell man

print(IHM_execute(1))