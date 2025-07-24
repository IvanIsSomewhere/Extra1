import numpy as np
from Custom_Plots import cplot_1,cplot_2
from funciones_multivariables import get_mv_function, get_mv_limit, get_mv_x0

import numpy as np
import math
import random


def hooke_jeeves(f, x0, step_size=0.5, step_reduction=0.5, tolerance=1e-6, max_iter=1000):

    n = len(x0)
    best_x = x0.copy()
    best_f = f(best_x)
    history = [(best_x.copy(), best_f)]

    for _ in range(max_iter):
        improved = False

        # 1. Exploratory Moves (local search)
        for i in range(n):
            for direction in [1, -1]:
                x_new = best_x.copy()
                x_new[i] += direction * step_size
                f_new = f(x_new)
                history.append((x_new.copy(), f_new))

                if f_new < best_f:
                    best_x = x_new
                    best_f = f_new
                    improved = True
                    break  # Accept first improvement

            if improved:
                break

        # 2. Pattern Move (accelerated search)
        if improved:
            while True:
                x_pattern = 2 * best_x - history[-2][0]  # Extrapolate
                f_pattern = f(x_pattern)
                history.append((x_pattern.copy(), f_pattern))

                if f_pattern < best_f:
                    best_x = x_pattern
                    best_f = f_pattern
                else:
                    break
        else:
            # 3. Reduce step size if no improvement
            step_size *= step_reduction
            if step_size < tolerance:
                break

    return best_x, history


def ejecutar(id):
    f = get_mv_function(id)
    bounds = [0,0]
    bounds[0] , bounds[1] = get_mv_limit(id)
    x0 = get_mv_x0(id)

    return hooke_jeeves(f, x0)

a,b = ejecutar("rastrigin")