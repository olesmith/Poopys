from math import *

from Scalar import Scalar

def Max(x,y):
    if (x>=y): return x
    else:      return y

def Min(x,y):
    if (x<=y): return x
    else:      return y

class Vector(list):
    ##
    ## Vector creator: allocates and/or initializes
    ##
    
    def __init__(self,v=None):
        if (v):
            if (v.__class__.__name__=='int'):
                for i in range(v):
                    self.append(0.0)
            elif (v.__class__.__name__ in ['list','Vector'] ):
                for i in range( len(v) ):
                    self.append( Scalar(v[i]) )
            else:
                print "Vector.init: Invalid second argument",v
                exit()
                
    ##
    ## Vector add: per coordinate
    ##
    
    def __add__(u,v):
        if ( len(u)!=len(v) ):
            print "Vector.add: Incompatible vector dimensions",len(u),len(v)
            exit()

        w=Vector(u)
        for i in range( len(v) ):
            w[i]+=Scalar(v[i])

        return w
            
    def __iadd__(u,v):
        return u+v
            
    ##
    ## Vector sub: per coordinate
    ##
    
    def __sub__(u,v):
        return u+(v*(-1.0))
            
    def __isub__(u,v):
        return u-v
            
    ##
    ## Vector mul: per coordinate
    ##
    
    def __mul__(u,v):
        if (v.__class__.__name__ in [ 'int' ]):
            v=Scalar(v)
            
        if (v.__class__.__name__ in [ 'float' ]):
            w=Vector(u)
            for i in range( len(w) ):
                w[i]*=v

            return w

        if (v.__class__.__name__ in [ 'Vector' ]):
            if ( len(u)!=len(v) ):
                print "Vector.mul: Incompatible vector dimensions",len(u),len(v)
                exit()

            dot=0.0
            for i in range( len(u) ):
                dot+=u[i]*v[i]

            return dot
        
        if (v.__class__.__name__ in [ 'Matrix' ]):
            w=Vector()
            for i in range( len(v) ):
                w.append(0.0)
                for j in range( len(u) ):
                    w[i]+=v[i][j]*u[j]

            return w
        
            
    def __imul__(u,v):
        return u*v
     
    def __rmul__(u,v):
        if (u.__class__.__name__=='float'):
            return v*u

        return u*v
     
    ##
    ## Vector neg: opposed vector
    ##
    
    def __neg__(u):
        return u*(-1.0)
    
    ##
    ## Vector div: only by scalar!
    ##
    
    def __div__(u,v):
        if (v.__class__.__name__ in [ 'int' ]):
            v=Scalar(v)
            
        if (v.__class__.__name__ in [ 'float' ]):
            w=Vector(u)
            for i in range( len(w) ):
                w[i]*=v

            return w

        print "Vector.div: Incompatible second argument type",v
        exit()
        
            
    def __idiv__(u,v):
        return u/v
     
    ##
    ## Vector print: print formatted by %.6f
    ##
    
    def __str__(u):
        text=[]
        for i in range( len(u) ):
            text.append( ("%.6f" % u[i]) )

        return "["+",".join(text)+"]"
    
    def Abs_Max(v,vv):
        if (len(v)==0): v=Vector( len(vv) )

        for i in range( len(vv) ):
            v[i]=Max(   abs(v[i]),abs(vv[i])  )
                
        return v
                
    ##
    ## Dot product, square length and length
    ##
    
    def Dot(u,v):
        return u*v
     
    def Square_Length(u):
        return u.Dot(u)
 
    def Length(u):
        return sqrt(  u.Square_Length()   )
 
    def Hat2(u):
        if (u):
            return Vector([  -u[1],u[0]  ])

        return None
 
    def Normalize(u):
        length=u.Length()
        if (length!=0.0):
            return u*(1.0/u.Length())

        return None
 
    ##
    ## Norms.
    ##
    
    def Norm(u,p=2.0):
        norm=0.0
        for i in range( len(u) ):
            norm+= abs(u[i])**p

        return norm**(1.0/Scalar(p))
     
 
    ##
    ## Returns per coordinate max of 2 vectors
    ##
    
    def Max(v,vv):
        if (len(v)==0): v=Vector( len(vv) )

        for i in range( len(vv) ):
            if (v[i]<vv[i]): v[i]=vv[i]
                
        return v
                
    ##
    ## Returns per coordinate min of 2 vectors
    ##
    
    def Min(v,vv):
        if (len(v)==0): v=Vector( len(vv) )
        
        for i in range( len(vv) ):
            if (v[i]>vv[i]): v[i]=vv[i]
                
        return v
                
