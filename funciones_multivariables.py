import numpy as np

def function1(x1,x2):
    return (x1-10)**2 + (x2 - 10)**2

def f_rastrigin_3d(x):

    A = 10
    return 3*A + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

def f_rosenbrock(x):
    x = np.asarray(x)
    return np.sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)


def f_himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def f_sphere(x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]**2

    return sum

def f_booth(x):
    return (x[0]+ 2*x[1] + 7)**2 + (2*x[0] + x[1] - 5)**2

def get_mv_function(id):
    match(id):
        case "rastrigin":
            return f_rastrigin_3d
        case "rosenbrock":
            return f_rosenbrock
        case "himmelblau":
            return f_himmelblau
        case "sphere":
            return f_sphere
        case "booth":
            return f_booth

def get_mv_alpha(id):
    match(id):
        case "rastrigin":
            return 2
        case "rosenbrock":
            return 2
        case _:
            return 2

def get_mv_delta(id):
    match (id):
        case "rastrigin":
            return 0.5
        case "rosenbrock":
            return 0.5
        case "himmelblau":
            return 0.5
        case _:
            return 0.5

def get_mv_limit(id):
    match(id):
        case "rastrigin":
            return -5.12, 5.12
        case "rosenbrock":
            return -5, 5
        case "himmelblau":
            return -5,5
        case "sphere":
            return -5,5
        case "booth":
            return -10,10

def get_mv_x0(id):
    match(id):
        case "rastrigin":
            return [-2,-2,-2]
        case "rosenbrock":
            return [2,1.5,3,-1.5,-2]
        case "sphere":
            return [-1,1.5]
        case "himmelblau":
            return [0,0]
        case "booth":
            return [-5, -2.5]
