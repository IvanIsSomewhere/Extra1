import numpy as np
from funciones_multivariables import get_mv_function, get_mv_limit, get_mv_x0

import numpy as np


def nelder_mead(f, x0, tol=1e-6, max_iter=1000, alpha=2, gamma=2, rho=0.5, sigma=0.5):
    """
    Nelder-Mead optimization algorithm to find the minimum of a function.

    Parameters:
    f (function): The objective function to minimize.
    x0 (list/np.array): Initial guess.
    tol (float): Tolerance for convergence.
    max_iter (int): Maximum number of iterations.
    alpha, gamma, rho, sigma (float): Reflection, expansion, contraction, shrink coefficients.

    Returns:
    float: The minimum value of the function found.
    """
    n = len(x0)
    simplex = [np.array(x0, dtype=float)]
    val_his = []


    # Initialize simplex
    for i in range(n):
        x = np.array(x0, dtype=float)
        x[i] = x[i] + 1.0 if x[i] != 0 else 0.25
        simplex.append(x)

    for _ in range(max_iter):
        # Evaluate function at each vertex
        values = [f(x) for x in simplex]

        # Order the simplex from best to worst
        order = np.argsort(values)
        values = [values[i] for i in order]
        simplex = [simplex[i] for i in order]

        # Check for convergence


        # Calculate centroid (excluding worst point)
        x0 = np.mean(simplex[:-1], axis=0)

        # Reflection
        xr = x0 + alpha * (x0 - simplex[-1])
        fr = f(xr)

        if values[0] <= fr < values[-2]:
            simplex[-1] = xr
            continue

        # Expansion
        if fr < values[0]:
            xe = x0 + gamma * (xr - x0)
            fe = f(xe)
            if fe < fr:
                simplex[-1] = xe
            else:
                simplex[-1] = xr
            continue

        # Contraction
        if fr >= values[-2]:
            xc = x0 + rho * (simplex[-1] - x0)
            fc = f(xc)
            if fc < values[-1]:
                simplex[-1] = xc
                continue

        # Shrink
        x1 = simplex[0]
        new_simplex = [x1]
        for i in range(1, n + 1):
            xs = x1 + sigma * (simplex[i] - x1)
            new_simplex.append(xs)
        simplex = new_simplex

        val_his.append(min([f(x) for x in simplex]))



    # Return best value found
    return min([f(x) for x in simplex]), val_his




def execute_nm(id):
    func = get_mv_function(id)
    a, b = get_mv_limit(id)
    x0 = get_mv_x0(id)

    return nelder_mead(func,x0)

print(execute_nm("himmelblau"))