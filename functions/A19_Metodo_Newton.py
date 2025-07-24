import numpy as np
from scipy.linalg import solve


def newton_method(f, grad_f, hessian_f, x0, tol=1e-6, max_iter=100):
    x = np.array(x0, dtype=float)
    history = [(x.copy(), f(x))]

    for _ in range(max_iter):
        gradient = grad_f(x)
        hessian = hessian_f(x)

        # Solve the linear system HΔx = -∇f
        delta_x = solve(hessian, -gradient)

        x += delta_x
        current_val = f(x)
        history.append((x.copy(), current_val))

        # Check convergence
        if np.linalg.norm(delta_x) < tol:
            break

    return x, history