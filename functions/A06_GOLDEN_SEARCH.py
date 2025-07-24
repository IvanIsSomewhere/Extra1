from Test_Funcions import function_return_limit, aplicar_funcion
from functions.A03_ELIMINACION_REGIONES import eliminar_regiones

def golden_search(f, a, b, epsilon):
    _a = a + ((a+b)/2) * 0.001
    _b = b - ((a+b)/2) * 0.001

    _x = (a + b) / 2
    _w = (_x - _a) / (_b - _a)

    aw = 0
    bw = 1
    lw = 1
    k = 1

    state = -1

    x_history = [[],[]]

    while abs(lw) > epsilon:
        w1 = aw + (0.618) * lw
        w2 = bw - (0.618) * lw

        match(state):
            case -1:
                x1 = w1
                x2 = w2
                state = 1
            case 1:
                x1 = w1
                state = 2
            case 2:
                x2 = w2
                state = 1

        x_history[0].append(x1)
        x_history[1].append(x2)

        conclusion = eliminar_regiones(f,x1,x2)

        match(conclusion):
            case 0:
                aw = x1
            case 1:
                bw = x2
            case 2:
                bw = x2
                aw = x1

        lw = bw - aw
        #print(lw)

    return abs(lw), x_history

def execute_GS(id, epsilon):
    _f = aplicar_funcion(id)

    _var = function_return_limit(id)
    _a = _var["lo"]
    _b = _var["hi"]

    return golden_search(_f,_a,_b,epsilon)

execute_GS(1,.001)