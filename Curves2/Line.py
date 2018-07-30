from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n     import *
from Curve   import Curve

class Line(Curve):
    Name="Line"

    Resolution=[1200,400]
    
    N=400

    a=1.0
    b=0.0
    
    t1=0.0
    t2=4.0*pi
    
    N=100
    
    xmax=4.0*pi
    ymax=1.0
    xmin=-0.25
    ymin=-0.25

    
        
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([self.xmin,self.ymin])
    
    def Curve_Init_Parameters(self):            
        return
    
    def Curve_Parameters(self):
        return [
            [
                #0.5,0.6,0.7,0.8,0.9,
                1.0 ],
        ]

    def Curve_Parameter_Keys(self):
        return [ "a",b ]
    
    def Curve_Parameter_Names(self):
        return [ "a,b" ]
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.a,
            "%.6f" % self.b,
            "%d"  % self.N,
        ]
    


    def S(self,t):
        return sqrt(self.a**2+self.b**2)*t
    
    def S_Tex(self):        
        return "\\sqrt{a^2+b^2}t"
    
    def R(self,t):
        return Vector([self.a*t,self.b*t])
    
    def R_Tex(self):        
        return self.Latex_vect([ "at","bt)" ])
        
    def dR(self,t):
        return Vector([self.a,self.b])
    
    def dR_Tex(self):        
        return self.Latex_vect([ "a","t)" ])
        
    def d2R(self,t):
        return Vector([0.0,0.0])

    def d2R_Tex(self):        
        return self.Latex_Vector("0")
            
    def d3R(self,t):
        return Vector([0.0,0.0])

    def d3R_Tex(self):        
        return self.Latex_Vector("0")
        
    def v2(self,t):
        return self.a**2+self.b**2

    def v2_Tex(self):        
        return "a^2+b^2"
    
    def t(self,t):
        return Vector([1.0,0.0])

    def t_Tex(self,t):
        return self.Latex_Vector("I")

    def n(self,t):
        return Vector([0.0,1.0])

    def n_Tex(self,t):
        return self.Latex_Vector("J")

    def VN(self,t):
        return Vector([-self.b,self.a])

    def VN_Tex(self):        
        return self.Latex_vect([ "-bt","at)" ])
    
    def Det(self,t):
        return 0.0
    
    def Det_Tex(self):        
        return "0"
    
    
    def Phi(self,t):
        return None
    
    def dPhi(self,t):
        return None

    def Phi_Tex(self):        
        return "+\\infty"
    
    def Kappa_Tex(self):
        return "0"
    
    def Kappa(self,t):
        return 0.0

    def Rho(self,t):
        return None

    def RhoV(self,t):

        return None

    def Evolute(self,t):
        return None
    
    def dEvolute(self,t):
        return None
    
    def Evolute_Tex(self):
        return self.Latex_Vector("\\infty")
    
    def dEvolute_Tex(self):
        return self.Latex_Vector("\\infty")
    
if (re.search('Line.py$',sys.argv[0])):
    curve=Line()
    curve.Run()
