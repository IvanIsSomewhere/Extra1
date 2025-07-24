
#funciones basicas

def test_function_1(x):
    return x**2 + (54/x)

def test_function_2(x):
    return x**3 + (2*x) - 3

def test_function_3(x):
    return  x**4 + x**2 - 33

def test_function_4(x):
    return 3*x**4 +  8*x**3 - 6*x**2 + 12*x



#funciones a la primera derivada
def test_function_1_d(x):
    return 2*x + (54/(x**2))

def test_function_2_d(x):
    return 3*x**2 + 2

def test_function_3_d(x):
    return 4*x**3 + (2 * x)

def test_function_4_d(x):
    return 12*x**3 + 24*x**2 - 12*x + 12

#funciones a la 2da derivada
def test_function_1_dd(x):
    return 2 - 108/(x**3)

def test_function_2_dd(x):
    return 6*x

def test_function_3_dd(x):
    return 12*x**2 + 2

def test_function_4_dd(x):
    return 36*x**2 + 48*x - 12

def function_return_limit(id):
    match id:
        case 1: return {"lo" : -1, "hi": 10}
        case 2: return {"lo" : -1, "hi": 5}
        case 3: return {"lo" : -2.5, "hi": 2.5}
        case 4: return {"lo" : -1.5, "hi": 3}
        case _: return {"lo" : -1, "hi": 10}

    return 0

def function_higher_value(x):
    match x:
        case 1: return 10
        case 2: return 5
        case 3: return 2.5
        case 4: return 3
        case _: return 1

def aplicar_funcion_d(id):
    match(id):
        case 1:
            return test_function_1_d
        case 2:
            return test_function_2_d
        case 3:
            return test_function_3_d
        case 4:
            return test_function_4_d
        case _:
            return test_function_1_d

def aplicar_funcion_dd(id):
    match(id):
        case 1:
            return test_function_1_dd
        case 2:
            return test_function_2_dd
        case 3:
            return test_function_3_dd
        case 4:
            return test_function_4_dd
        case _:
            return test_function_1_dd

def aplicar_funcion(id):
    match id:
        case 1:
            return test_function_1
        case 2:
            return test_function_2
        case 3:
            return test_function_3
        case 4:
            return test_function_4
        case _:
            return test_function_1

def func_limit(id):
    match(id):
        case 1:
            return 0,10
        case 2:
            return 0,5
        case 3:
            return -2.5,2.5
        case 4:
            return -1.5,3
        case _:
            return -1,10

def func_text(id):
    match(id):
        case 1:
            return( "f(x)   = x**2 + (54/x) \n"
                    "f'(x)  = x**2 + (54/(x**2))\n"
                    "f''(x) = x**2 + (54/(x**2))\n")
        case 2:
            return ("f(x)   = x**3 + (2*x) - 3 \n"
                    "f'(x)  = 3*x**2 + 2\n"
                    "f''(x) = 3*x**2 + 2\n")
        case 3:
            return ("f(x)   = x**3 + (2*x) - 3 \n"
                    "f'(x)  = 3*x**2 + 2\n"
                    "f''(x) = 3*x**2 + 2\n")
