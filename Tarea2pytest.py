import pytest


print("\nTarea 2 Pytest\n")


def op_2_num():
    xf = 0
    yf = 0
    e = "0"
    with pytest.raises(ValueError) as exc_info:
        x = input("Inserte el valor de a: ")
        assert float(x)
        xf = float(x)
        raise ValueError("None")
    if "string to float" in str(exc_info.value):
        print("a es una expresion literal y no un numero, ejecute nuevamente")
        return -1, 0, 0, 0
    with pytest.raises(ValueError) as exc_info:
        y = input("Inserte el valor de b: ")
        assert float(y)
        yf = float(y)
        raise ValueError("None")
    if "string to float" in str(exc_info.value):
        print("b es una expresion literal y no un numero, ejecute nuevamente")
        return -1, 0, 0, 0
    with pytest.raises(ValueError) as exc_info:
        if(xf < yf):
            e = "E"
        else:
            e = "1"
        assert float(e)
        raise ValueError("None")
    if "string to float" in str(exc_info.value):
        print("a es de menor magnitud que b, ejecute nuevamente")
        return -1, 0, 0, 0
    else:
        return 0, (xf - yf), (xf + yf), (xf * yf)


e, dif, pl, mult = op_2_num()


if (e == -1):
    print("\nError en la ejecucion, argumento invalido\n")
else:
    print("\nEjecucion sin errores, desplegando resultados:\n")
    print("Resta: ", dif, "\n")
    print("Suma: ", pl, "\n")
    print("Multiplicacion: ", mult, "\n")
