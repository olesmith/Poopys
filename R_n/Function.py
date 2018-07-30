from Scalar import Scalar
from Vector import Vector
from Mesh import Mesh

from math import *
Eps=None

class Function():
    eps=1.0E-3
    
    def __init__(self,f,eps=None):
        self.f=f
        if (Eps):
            self.epsEeps
            
        if (eps):
            self.eps=eps
            
        self.__Init__()
            
        return
    
    def __Init__(self):
        self.eps2inv=0.5/self.eps
        
    def df(self,t,n=1):
        if (n==0):
            return self.f(t)

        return (self.df(t+self.eps,n-1)-self.df(t-self.eps,n-1))*self.eps2inv
        
    def Mesh(self,t1,t2,N,n=0):
        dt=(t2-t1)/(1.0*(N-1))
        mesh=Mesh(N)

        t=t1
        for i in range(N):
            mesh[i]=Vector([t,self.df(t,n)])
            t+=dt
            
        return mesh

    
if (False):
    def f(t):
        return cos(t)

        ff=Function(f)
        print ff.Mesh(0.0,pi,100,4)
