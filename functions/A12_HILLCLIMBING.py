import random as rng
from random import random

from numpy.ma.core import append

from Custom_Plots import cplot_1, cplot_2
from funciones_multivariables import get_mv_function, get_mv_limit, get_mv_x0


def random_step(step_size=1):
    return step_size if rng.choice([True, False]) else -step_size


def hillclimbing(f, x0 = None,x_a = 0,x_b = 1, step = 0.2,  max_iter = 1000):
    if x0 is None:
        x0 = [0,1]

    N = len(x0)

    l = (x_b - x_a)
    xbest = x0
    xnext = x0
    iteration = 0
    i_best = 0
    print(xbest)
    x = x0
    fx_history = []


    for i in range(max_iter):
        xnext=[]
        for j in range(N):
            dnext = xbest[j] + random_step(step)

            if dnext < x_a: dnext = x_a + step
            if dnext > x_b: dnext = x_b - step

            xnext.append(dnext)


        if f(xnext) < f(xbest):
            print("new_minimum")
            xbest = xnext
            i_best = iteration

        fx_history.append(f(xbest))



        iteration += 1
        #print(xbest, i_best)
    return xbest,fx_history



def execute_hc(id):
    func = get_mv_function(id)
    a,b = get_mv_limit(id)
    x0 = get_mv_x0(id)

    return hillclimbing(func,x0,a,b)

#a,c = execute_hc("rastrigin")

#cplot_1(c)

