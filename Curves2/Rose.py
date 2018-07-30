from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve

class Rose(Curve):
    Name="Rose"

    a=1.0
    b=2.0
    
    xmax=4.25
    ymax=4.25

    xmax=2.0
    ymax=2.0

    t1=0.0
    t2=30.0*pi
    N=4000
    Parameters=[
        [
            2.0,3.0,4.0,5.0,6.0,7.0,#8.0,9.0,10.0,
            #3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,
        ],
    ]
    
    #Show_Point_Nos=[0,25,55,90,133,190]
    Latex_Figs=[
            [
                [
                    "Rose/Rose_Ana_2_000000-4000.pdf",
                    "Rose/Rose_Ana_3_000000-4000.pdf",
                ],
                [ "$n=2$","$n=3$", ],
            ],
            [
                [
                    "Rose/Rose_Ana_4_000000-4000.pdf",
                    "Rose/Rose_Ana_5_000000-4000.pdf",
                ],
                [ "$n=4$","$n=5$", ],
            ],
            [
                [
                    "Rose/Rose_Ana_6_000000-4000.pdf",
                    "Rose/Rose_Ana_7_000000-4000.pdf",
                ],
                [ "$n=6$","$n=7$", ],
            ],
    ]
    
    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        return 2.0
    
    def PMax(self):
        return 1.1*Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return 1.1*Vector([-self.xmax,-self.ymax])
    
    def Evolute_PMax000000(self):
        return Vector([2.0*self.xmax,2.0*self.ymax])
    
    def Evolute_PMin0000000(self):
        return Vector([-2.0*self.xmax,-2.0*self.ymax])
    
    def Curve_Parameters(self):
        return self.Parameters
          
    def Curve_Init_Parameters(self):
        return
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.a,
            "%d"   % self.N,
        ]
    
    def Curve_Parameter_Keys(self):
        return [ "a",]
    def Curve_Parameter_Names(self):
        return [ "n","b"]

    #E vector factor
    def fact(self,t):
        return cos( self.a*t )
    
    def dfact(self,t):
        return -self.a*sin( self.a*t )
    
    def d2fact(self,t):
        return -self.a**2.0*cos( self.a*t )
    
    def d3fact(self,t):
        return self.a**3.0*sin( self.a*t )
    
    def R(self,t):
        return E(t)*self.fact(t)
    
    def R_Tex(self):
        return "\\cos{nt}~"+self.Latex_Vector("e")+"(t)"
        
    def dR(self,t):
        ccos=cos( self.a*t )
        ssin=sin( self.a*t )
        efact=-self.a*ssin
        ffact=ccos
        
        return E(t)*efact+F(t)*ffact

    def dR_Tex(self):
        return "".join(
            [
                "-n \\sin{nt}~"+self.Latex_Vector("e")+"(t)",
                "+ \\cos{nt}~"+self.Latex_Vector("f")+"(t)",
            ]
        )
    def d2R(self,t):
        ccos=cos( self.a*t )
        ssin=sin( self.a*t )
        efact=-(self.a**2.0+1.0)*ccos
        ffact=-2.0*self.a*ssin
        
        return E(t)*efact+F(t)*ffact

    def d2R_Tex(self):
        return "".join(
            [
                "-(n^2+1) \\cos{nt}~"+self.Latex_Vector("e")+"(t)",
                "-2n\\sin{nt}~"+self.Latex_Vector("f")+"(t)",
            ]
        )
        
    def d3R(self,t):
        ccos=cos( self.a*t )
        ssin=sin( self.a*t )

        efact=(self.a**3+3.0*self.a)*ssin
        ffact=-(3.0*self.a**2+1.0)*ccos

        return E(t)*efact+F(t)*ffact

    def d3R_Tex(self):
        return "".join(
            [
                "n(n^2+3) \\sin{nt}~"+self.Latex_Vector("e")+"(t)",
                "-(3n^2+1) \\cos{nt}~"+self.Latex_Vector("f")+"(t)"
            ]
        )
        return self.Latex_vect([" a \sin{t}","-b \cos{t}"])
        
    def VN(self,t):
        ccos=cos( self.a*t )
        ssin=sin( self.a*t )
        ffact=-self.a*ssin
        efact=-ccos
        
        return E(t)*efact+F(t)*ffact
        
        

    def VN_Tex(self):        
        return "".join(
            [
                "-\\cos{nt}~"+self.Latex_Vector("e")+"(t)",
                "-n \\sin{nt}~"+self.Latex_Vector("f")+"(t)",
            ]
        )

     
    def v2(self,t):
        ccos=cos( self.a*t )
        return self.a**2+(1-self.a**2)*ccos**2
    
    def v2_Tex(self):
        return "n^2\\sin^2{n t}+\\cos^2{n t}"
    
    def dv2_Tex(self):
        return "n(2n^2-1) \\sin{n t}\\cos{n t}"
    
    def Det(self,t):
        ccos=cos( self.a*t )
        
        return (1-self.a**2)*ccos**2+2.0*self.a**2
    
    def Det_Tex(self):
        return "n^2+v(t)^2"
        
    def Phi(self,t):
        ccos=cos( self.a*t )

        a2=self.a**2
        
        return 1.0-a2/(2.0*a2+(1-a2)*ccos**2)

    def t_Tex(self):
        return "\\frac{"+self.dR_Tex()+"}{ v(t)}"
    
    def n_Tex(self):
        return "\\frac{"+self.VN_Tex()+"}{ v(t)}"
                
    def Phi(self,t):
        return self.v2(t)/(self.a**2+self.v2(t))
                
    def Psi(self,t):
        return (self.a**2+self.v2(t))/self.v2(t)
                
    def Phi_Tex(self):
        return "\\frac{v(t)^2}{ n^2+v(t)^2}"
                
    def Psi_Tex(self):
        return "\\frac{ n^2+v(t)^2  }{v(t)^2}"
                
    def Kappa(self,t):
        return (   self.a**2+self.v2(t)   )/(   self.v2(t)**1.5   )
    
    def Kappa_Tex(self):
        return "\\frac{ n^2+v(t)^2  }{v(t)^3}"

    def Rho(self,t):
        return (   self.v2(t)**1.5   )/(   self.a**2+self.v2(t)   )

    def Rho_Tex(self):
        return "\\frac{v(t)^3}{ n^2+v(t)^2  }"
    
    def dRho_Tex(self):
        return "(3n^2+v(t)^2)\\frac{v(t)^2v'(t)}{ (n^2+v(t)^2)^2  }"
        
    def Evolute(self,t):
        ccos=cos( self.a*t )
        ssin=sin( self.a*t )
        
        phi=self.Phi(t)

        efact=(1-phi)*ccos
        ffact=-self.a*ssin*phi

        Dt=self.Det(t)
        efact=self.a**2*ccos/Dt

        ffact=-self.a*ssin*(1.0- self.a**2/Dt )
        return E(t)*efact+F(t)*ffact
        

    def Evolute_Tex(self):
        comps=[
            "\\frac{    "+
            "   n^2 \\cos{nt}"+self.Latex_Vector("e")+"(t)"+
            "   -n \\sin{nt}"+self.Latex_Vector("f")+"(t)"+
            "}{ n^2+v^2 }"
        ]
        
        return "".join(comps)
        
        
if (re.search('Rose.py$',sys.argv[0])):
    curve=Rose({
    })

    curve.Run()
