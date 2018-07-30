from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve

class Ellipsis(Curve):
    Name="Ellipsis"

    a=1.0
    b=2.0
    rho=2.0
    
    xmax=3.5
    ymax=3.5
    cfactor=0.0
    
    Show_Point_Nos=[]
    
    Latex_Figs=[
            [
                [
                    "Ellipsis/Ellipsis_Ana_0_500000-1_000000-100.pdf",
                    "Ellipsis/Ellipsis_Ana_1_000000-1_000000-100.pdf",
                    "Ellipsis/Ellipsis_Ana_2_000000-1_000000-100.pdf",
                ],
                [ "$a=\\frac{1}{2}$","$a=1$","$a=2$", ],
            ],
    ]
    
    def Curve_Parameters(self):
       b=1.0
       ass=[
            2.0,1.75,sqrt(2),
            1.25,1.0,1.0/1.25,
            1.0/sqrt(2),1.0/1.75,1.0/2.0,
       ]

       return [
            ass,
            [
                1.0,
            ],
        ]
   
    
    def Curve_Types_Deviations(self):
        return [
            "dR","d2R","VN",
            "v2",
            "Det",
            "Phi",
            "Psi",
            "Kappa",
            "Rho","dRho",
            "Evolute","dEvolute",
        ]
    def Curve_Deviations(self):
        return [
            [
                ['$a=\\frac{1}{2}$',[0.5,1.0]],
                ['$a=1$',[1.0,1.0]],
                ['$a=2$',[2.0,1.0]],
            ],
        ]
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([-self.xmax,-self.ymax])
    
    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        return 2.0
        return [
            [-1.0, 0.0],
            [ 2.0, 0.0],
            [ 0.0,-1.0],
            [ 0.0, 2.0],
        ]    
    
    def Curve_SVG_Draw(self):
        svgs=self.Mesh_Curves_Draw(
            "Num",
            self.Curve_Coordinate_System_Get(),
            {
                "R": True,
                "Evolute": True,
                "dEvolute": True,
            }
        )
        paths=self.Curve_Parameters_2_Path(
            "","",
            ["Ellipse",self.a,self.b,self.N]
        )

        svgfile="/".join(paths)+".svg"
        pdffile="/".join(paths)+".pdf"
        self.Rs.SVG_Doc_Write(self.Rs.__Canvas__,svgs,svgfile)

        paths.pop(0)
        paths.pop(0)
        paths.pop(0)
        svgfile="/".join(paths)+".svg"
        self.SVG_2_PDF(svgfile,pdffile)

        
       
    def Curve_Init_Parameters(self):
        self.cfactor=(self.a**2-self.b**2)/(self.a*self.b)
        return
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.a,
            "%.6f" % self.b,
            "%d"  % self.N,
        ]
    
    def Curve_Parameter_Keys(self):
        return [ "a","b"]
    def Curve_Parameter_Names(self):
        return [ "a","b"]

    
    def R(self,t):
        return Vector([
            self.a*cos(t),
            self.b*sin(t),
        ])
    
    def Equation_Tex(self):
        return "\\frac{ (x-x_0)^2 }{a^2}+\\frac{ (y-y_0)^2 }{b^2}=1"
    
    
    def R_Tex(self):
        return self.Latex_vect(["a \\cos{t}","b \\sin{t}"])+"+"+self.Latex_Vector("r","_0")
        
    def Factor(self):
        return (self.a**2-self.b**2)/(self.a*self.b)
    
    def Factor_Tex(self):
        return "\\frac{a^2-b^2}{ab}"
    
    def dR(self,t):
        return Vector([
            -self.a*sin(t),
            self.b*cos(t),
        ])

    def dR_Tex(self):
        return self.Latex_vect(["-a \\sin{t}","b \\cos{t}"])
        
    def d2R(self,t):
        return self.R(t)*(-1.0)

    def d2R_Tex(self):
        return self.Latex_vect(["-a \\cos{t}","-b \\sin{t}"])
        
    def d3R(self,t):
        return self.dR(t)*(-1.0)

    def d3R_Tex(self):
        return self.Latex_vect([" a \\sin{t}","-b \\cos{t}"])
        
    def v2(self,t):
        return (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0
    
    def v2_Tex(self):
        return "a^2 \\sin^2{t}+b^2 \\cos^2{t}"
       

    def t(self,t):
        return Vector([
            -self.a*sin(t),
            self.b*cos(t),
        ])*(1.0/sqrt( (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  ) )

    def t_Tex(self):
        return " \\frac{1}{  \\sqrt{"+self.v2_Tex()+"}  } \\cdot "+self.Latex_vect(["-a \\sin{t}"," b \\cos{t}"])
        
    def n(self,t):
        return Vector([
            -self.b*cos(t),
            -self.a*sin(t),
        ])*(1.0/sqrt( (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  ) )

    def n_Tex(self):
        return "\\frac{-1}{  \\sqrt{"+self.v2_Tex()+"}  } "+self.Latex_vect(["b \\cos{t}","a \\sin{t}"])
        
    def VN(self,t):
        return Vector([
            -self.b*cos(t),
            -self.a*sin(t),
        ])

    def VN_Tex(self):
        return "-"+self.Latex_vect(["b \\cos{t}","a \\sin{t}"])
        
    def Det(self,t):
        return self.a*self.b
    
    
    def Det_Tex(self):
        return "ab>0"
        
    def Phi(self,t):
        return (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )/(self.a*self.b)

    def Phi_Tex(self):
        return "\\frac{  "+self.v2_Tex()+"   }{ab}"
        
    def Psi(self,t):
        return (self.a*self.b)/(  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )

    def Psi_Tex(self):
        return "\\frac{ab}{  "+self.v2_Tex()+"   }"
        
    def Kappa(self,t):
        return (self.a*self.b)/(  (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )**1.5  )
    
    def Kappa_Tex(self):
        return "\\frac{ab}{   ("+self.v2_Tex()+")^{3/2}   }"

    def Rho(self,t):
        return (  (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )**1.5  )/(self.a*self.b)

    def Rho_Tex(self):
        return "\\frac{   ("+self.v2_Tex()+")^{3/2}   }{ab}"
        
    def dRho(self,t):
        sq=sqrt(   (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )
        fact=3.0*(self.a-self.b)/(self.a*self.b)
        
        return fact*sq*sin(t)*cos(t)
    
    def dRho_Tex(self):
        return "3 \\frac{a-b}{ab} \\sqrt{"+ self.v2_Tex()+"}\\sin{t}\\cos{t}"
        
    def Evolute(self,t):
        return Vector([
            self.b*cos(t)**3,
            -self.a*sin(t)**3,
        ])*self.Factor()
    
    def dEvolute(self,t):
        cs=cos(t)
        sn=sin(t)
        return Vector([
            self.b*cs,
            self.a*sn,
        ])*(-3.0*self.Factor()*cs*sn)

    def Evolute_Tex(self):
        return " ".join([
            self.Factor_Tex(),
            self.Latex_vect(["b \\cos^3{t}","-a \\sin^3{t}"])
        ])
        
    def dEvolute_Tex(self):
        return "-3\\frac{a^2-b^2}{ab}\\cos{t}\\sin{t} "+self.Latex_vect(["b \\cos{t}","a \\sin{t}"])
        
if (re.search('Ellipsis.py$',sys.argv[0])):
    curve=Ellipsis({
    })

    curve.Run()
