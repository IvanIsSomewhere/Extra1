import numpy as np
from typing import Callable, Tuple, Optional


class NewtonOptimizer:

    def __init__(self,
                 function: Callable[[np.ndarray], float],
                 grad_tol: float = 1e-3,
                 step_tol: float = 1e-3,
                 max_iter: int = 100):
        self.function = function
        self.grad_tol = grad_tol
        self.step_tol = step_tol
        self.max_iter = max_iter

    def _compute_gradient(self, x: np.ndarray, h: float = 1e-6) -> np.ndarray:
        grad = np.zeros_like(x)
        for i in range(len(x)):
            x_plus = x.copy()
            x_minus = x.copy()
            x_plus[i] += h
            x_minus[i] -= h
            grad[i] = (self.function(x_plus) - self.function(x_minus)) / (2 * h)
        return grad

    def _compute_hessian(self, x: np.ndarray, delta: float = 1e-5) -> np.ndarray:
        n = len(x)
        hessian = np.zeros((n, n))
        fx = self.function(x)

        # Diagonal principal
        for i in range(n):
            x_plus = x.copy()
            x_minus = x.copy()
            x_plus[i] += delta
            x_minus[i] -= delta
            hessian[i, i] = (self.function(x_plus) - 2 * fx + self.function(x_minus)) / delta ** 2

        # Elementos fuera de la diagonal
        for i in range(n):
            for j in range(i + 1, n):
                x_pp = x.copy()
                x_pn = x.copy()
                x_np = x.copy()
                x_nn = x.copy()

                x_pp[i] += delta
                x_pp[j] += delta
                x_pn[i] += delta
                x_pn[j] -= delta
                x_np[i] -= delta
                x_np[j] += delta
                x_nn[i] -= delta
                x_nn[j] -= delta

                hessian[i, j] = hessian[j, i] = (
                                                        self.function(x_pp) - self.function(x_pn) -
                                                        self.function(x_np) + self.function(x_nn)
                                                ) / (4 * delta ** 2)

        return hessian

    def optimize(self, initial_point: np.ndarray, verbose: bool = False) -> Tuple[np.ndarray, int]:
        """
        Ejecuta el algoritmo de optimización.

        Args:
            initial_point: Punto inicial para la optimización
            verbose: Si True, imprime información de cada iteración

        Returns:
            Tuple con (punto óptimo encontrado, número de iteraciones realizadas)
        """
        x = initial_point.copy()
        iterations = 0

        while iterations < self.max_iter:
            grad = self._compute_gradient(x)
            hess = self._compute_hessian(x)

            # Criterio de parada por gradiente pequeño
            if np.linalg.norm(grad) < self.grad_tol:
                if verbose:
                    print(f"Convergencia alcanzada: norma del gradiente < {self.grad_tol}")
                break

            try:
                step = np.linalg.solve(hess, grad)
                x_new = x - step
            except np.linalg.LinAlgError:
                if verbose:
                    print("Hessiano singular - usando descenso de gradiente con paso pequeño")
                x_new = x - 0.01 * grad

            # Criterio de parada por cambio pequeño en x
            if np.linalg.norm(x_new - x) / (np.linalg.norm(x) + 1e-10) < self.step_tol:
                if verbose:
                    print(f"Convergencia alcanzada: cambio en x < {self.step_tol}")
                break

            if verbose:
                print(f"Iter {iterations}: x = {x}, f(x) = {self.function(x):.4f}, "
                      f"||∇f|| = {np.linalg.norm(grad):.4f}")

            x = x_new
            iterations += 1

        return x, iterations


def himmelblau(x: np.ndarray) -> float:
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


if __name__ == "__main__":
    optimizer = NewtonOptimizer(himmelblau, grad_tol=1e-3, step_tol=1e-3, max_iter=100)

    initial_point = np.array([0.0, 0.0])
    solution, iterations = optimizer.optimize(initial_point, verbose=True)

    print("\nResultados de la optimización:")
    print(f"- Punto óptimo encontrado: {solution}")
    print(f"- Valor de la función: {himmelblau(solution):.6f}")
    print(f"- Iteraciones realizadas: {iterations}")