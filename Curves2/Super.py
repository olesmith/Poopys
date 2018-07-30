from math import *
import re,sys
sys.path.insert(0,'/root/python')

from R_n import *
from Curve import Curve

class Super(Curve):
    Name="Superellipsis"

    N=400
    a=1.0
    b=1.0
    rho=0.25
    #rho2=2.0/3.0
    t1=0.0
    t2=pi*2.0
    
    xmax=1.0
    ymax=2.0
    Resolution=[1200,1200]
    
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([-self.xmax,-self.ymax])
    
    def Curve_Parameters(self):
        return [
            [ 1.0,],
            [ 2.0],
            [
                0.1,0.2,0.3,0.4,
                0.5,
                0.6,0.7,0.8,0.9,1.0,
                1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
                2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,
            ]
        ]
    
    def Curve_Parameter_Keys(self):
        return [ "a","b","rho" ]
    
    def Curve_Parameter_Names(self):
        return [ "a","b","&rho;" ]
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.a,
            "%.6f" % self.b,
            "%.6f" % self.rho,
            "%d"  % self.N,
        ]

    def Curve_Init_Parameters(self):
        self.rho2=2.0/(1.0*self.rho)
                       
    def Sign(self,c):
        if (c>0.0):   return 1.0
        elif (c<0.0): return -1.0
        else:         return 0.0
        
    def R(self,t):
        cosine= cos(t)
        sine  = sin(t)
        
        return Vector([
            self.Sign(cosine)*self.a*(  abs(cos(t))  )**self.rho2,
            self.Sign(  sine)*self.b*(  abs(sin(t))  )**self.rho2,
        ])
    
    def Parametrization_Tex(self):
        return self.Latex_vect(["a \cos{t}","b \sin{t}"])
        
    def Equation_Tex(self):
        return "\\left( \\frac{x}{a} \\right)^n+\\left( \\frac{y}{b} \\right)^n=1"
        
    def dR(self,t):
        cosine= cos(t)
        sine  = sin(t)

        dx=0.0
        if (abs(cos(t))>0.0):
            dx=self.a*(  abs(cos(t))  )**(self.rho2-1.0)*sin(t)
        dy=0.0
        if (abs(sin(t))>0.0):
            dy=self.b*(  abs(sin(t))  )**(self.rho2-1.0)*cos(t)
        
        if (t<pi*0.5):
            dx*=-1.0
            dy*=1.0
        elif (t<pi):
            dx*=-1.0
            dy*=1.0
        elif (t<pi*1.5):
            dx*=-1.0
            dy*=1.0
        elif (t<pi*2.0):
            dx*=-1.0
            dy*=1.0

        return Vector([dx,dy])*self.rho2

    def dR_Tex00(self):
        return self.Latex_vect(["-a \sin{t}","b \cos{t}"])
        
        
if (re.search('Super.py$',sys.argv[0])):
    curve=Super({
    })

    curve.Run()
