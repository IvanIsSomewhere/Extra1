import random as rng
from random import random

from Custom_Plots import cplot_1
from funciones_multivariables import get_mv_function, get_mv_limit, get_mv_x0


def random_walk(f, x0 = None,x_a = 0,x_b = 1,  max_iter = 1000):
    if x0 is None:
        x0 = [0,1]

    N = len(x0)

    step_range = (x_b - x_a) / 10000
    xbest = x0
    xnext = x0
    iteration = 0
    i_best = 0

    fx_history = []
    while iteration < max_iter:
        #print(iteration, xnext, f(xnext))


        for i in range(N):
            once = False
            while x_a > xnext[i] or xnext[i] > x_b or once == False:
                r = rng.randint(0,1)
                match(r):
                    case 0:
                        xnext[i] = xnext[i] + step_range
                    case 1:
                        xnext[i] = xnext[i] - step_range
                once = True

        fx_history.append(f(xbest))

        if f(xnext) < f(xbest):
            xbest = xnext
            i_best = iteration

        iteration += 1

    #print(xbest,i_best)
    return xbest,fx_history



def execute_rw(id):
    func = get_mv_function(id)
    a,b = get_mv_limit(id)
    x0 = get_mv_x0(id)

    return random_walk(func,x0,a,b)

a,b = execute_rw("rastrigin")
