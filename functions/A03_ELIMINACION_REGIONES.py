
def eliminar_regiones(function,x1,x2):

    f1 = function(x1)
    f2 = function(x2)


    if f1 > f2:
        return 0
    if f1 < f2:
        return 1
    if f1 ==f2:
        return 2