print("\nTarea 2 Simple\n")


def op_2_num():
    try:
        xf = float(input("Inserte el valor de a: "))
    except ValueError:
        print("a es una expresion literal y no un numero, ejecute nuevamente")
        return -1, 0, 0, 0
    else:
        try:
            yf = float(input("Inserte el valor de b: "))
        except ValueError:
            print("b es una expresion literal y no un numero, \
ejecute nuevamente")
            return -1, 0, 0, 0
        else:
            if (xf < yf):
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
