

def op_2_num(x, y):
    try:
        xf = float(x)
    except ValueError:
        return -1, 0, 0, 0
    else:
        try:
            yf = float(y)
        except ValueError:
            return -2, 0, 0, 0
        else:
            if (xf < yf):
                return -3, 0, 0, 0
            else:
                return 0, (xf - yf), (xf + yf), (xf * yf)
