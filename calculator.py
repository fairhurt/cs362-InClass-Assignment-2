# #Command to run the code:
# #python3 division.py
def division(a, b):
    try:
        arg1=int(a)
        arg2=int(b)
        if arg2 <= 0:
            return('Value must be greater than zero')
            raise ValueError
        
    except ValueError:
        return('String values not allowed');
    return arg1 / arg2

def subtraction (a, b):
    try:
        arg1=float(a)
        arg2=float(b)
    except ValueError:
        return ('Must be non string input')
    return arg1-arg2 

def addition ( a, b):
    try:
        arg1=float(a)
        arg2=float(b)
    except ValueError:
        return ('Must be non string input')
    return arg1+arg2 


def multiplication(a,b):
    try:
        arg1=float(a)
        arg2=float(b)
    except ValueError:
        return ('String values not allowed')
    return arg1*arg2 