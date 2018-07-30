
def Scalar(a):
    return 1.0*a

def Max(a,b):
    if (a>b): return a
    else:     return b

def Min(a,b):
    if (a<b): return a
    else:     return b

#class Scalar33(float):
#    def __init__(a,b=None):
#        if (b):
#            a=1.0*b

            
#    def __add__(a,b):
#        if (b.__class__.__name__ in [ 'int' ]):
#            b=1.0*b
#        return a+b
#    def __iadd__(a,b):
#        return a+b
    
#    def __sub__(a,b):
#        return a-1.0*b
#    def __isub__(a,b):
#        return a-b
