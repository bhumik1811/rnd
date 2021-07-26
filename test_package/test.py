def add(x,y):
    return x + y

def sub(x,y):
    if x >= y:
        return x - y
    else:
        return y -x

def mult(x,y):
    return x * y

def div(x,y):
    if y ==0:
        print("cannot divide by zero")
    else:
        return x / y
