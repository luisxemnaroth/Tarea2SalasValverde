

def op_2_num(x, y):
    try:
        xf = float(x)
    except ValueError:
        return -1
    else:
        try:
            yf = float(y)
        except ValueError:
            return -1
        else:
            if (xf < yf):
                return -2, 0, 0, 0
            else:
                return 0, (xf - yf), (xf + yf), (xf * yf)


def pytestfunc(a, b):
    assert op_2_num(a, b) == 0, "Caso de Exito"
    assert op_2_num(a, b) == -2, "a < b"
    assert op_2_num(a, b) == -1, "Valor Literal"


#Descomentar una a una para ejecutar prueba a prueba
#pytestfunc(20, 10)
#pytestfunc(10, 20)
#pytestfunc("a", 10)
#pytestfunc(20, "b")
