def esBisiesto(y):
    if int(y) % 400 == 0:
        return True
    elif int(y) % 100 ==0:
        return False
    elif int(y) % 4 == 0:
        return True
    else:
        return False
