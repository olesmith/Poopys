from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve

class Descartes(Curve):
    Name="Descartes"

    a=2.0
    
    xmax=2.0
    ymax=2.0

    t1=-1.0
    t2=1.0

    
    Symmetries=[
        Matrix(
            [
                [ 0.0,1.0],
                [ 1.0,0.0],
            ]
        ),
    ]
    
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([-self.xmax,-self.ymax])
    
    def Curve_Parameters(self):        
        return [
            [
                1.0,
            ],
        ]
    
    def Run_Curves_Post(self):
        self.Run_Curves_Post_Type("Evolute")
        self.Run_Curves_Post_Type("dEvolute")
        
    def Run_Curves_Post_Type(self,type):
        ass=[
            [
                1.0,
            ],
        ]

        pdffiles=[]
        titles=[]
        for rass in ass:
            rpdffiles=[]
            rtitles=[]
            for a in rass:
                paths=self.Curve_Parameters_2_Path(
                    type,"Num",
                    self.Curve_Parameters_Values_Format([a,self.N])
                )

                pdffile="/".join(paths)+".pdf"
                
                paths.pop(0)
                paths.pop(0)
                paths.pop(0)

                svgfile="/".join(paths)+".svg"
                print Command_Exec(
                    [
                        "/var/www/cgi-bin/PDF",
                        svgfile,
                        pdffile
                    ]
                )
        
    def Curve_Init_Parameters(self):
        return
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.a,
            "%d"  % self.N,
        ]
    
    def Curve_Parameter_Keys(self):
        return [ "a"]
    
    def Curve_Parameter_Names(self):
        return [ "a"]

    
    def F(self,t):
        return 3.0*self.a*t/(1.0+t**3.0)
    def r(self,t):
        
        return Vector([1.0,t])
    
    def dF(self,t):
        return 3.0*self.a*(1-2.0*t**3)/(  (1.0+t**3.0)**2 )
    
    def dr(self,t):
        return Vector([0.0,1.0])
                      
    def d2F(self,t):
        return 3.0*self.a*6.0*t**2* (2-t**3 )/(  (1.0+t**3.0)**3 )
    
    def d2r(self,t):
        return Vector([0.0,0.0])
                      
    
    def R(self,t):
        if ( abs(t+1.0)<1.0E-6 ): return None

        return Vector([1.0,t])*self.F(t)
    
    #def R_trig(self,t):
    #    if ( abs(t-1.0)<1.0E-2 ): return None
    #    
    #    theta=t*pi
    #    
    #    cosine=cos(theta)
     #    sine=sin(theta)
    #    r=sine*cosine/(sine**3.0+cosine**3.0)
        
        return Vector([ cosine,sine ])*(3.0*r*self.a)
    
    def R_Tex(self):
        return "\\frac{ 3at}{1+t^3}"+self.Latex_vect(["1","t"])
        
    def dR0(self,t):
        return Vector([
            -self.a*sin(t),
            self.b*cos(t),
        ])

    def dR000_Tex(self):
        return self.Latex_vect(["\\frac{3at}{1+t^3}","\\frac{3at^2}{1+t^3}"])

    
    def d20R(self,t):
        return self.R(t)*(-1.0)

    def d2R000_Tex(self):
        return self.Latex_vect(["-a \\cos{t}","-b \\sin{t}"])
        
    def d3R_00(self,t):
        return self.dR(t)*(-1.0)

    def d3R000_Tex(self):
        return self.Latex_vect([" a \\sin{t}","-b \\cos{t}"])
        
    def v20(self,t):
        return (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0
    
    def v2000_Tex(self):
        return "a^2 \\sin^2{t}+b^2 \\cos^2{t}"
       

    def t0(self,t):
        return Vector([
            -self.a*sin(t),
            self.b*cos(t),
        ])*(1.0/sqrt( (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  ) )

    def t_Tex0(self):
        return " \\frac{1}{  "+self.v2_Tex()+"  } \\cdot "+self.Latex_vect(["-a \\sin{t}"," b \\cos{t}"])
        
    def n00(self,t):
        return Vector([
            -self.b*cos(t),
            -self.a*sin(t),
        ])*(1.0/sqrt( (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  ) )

    def n_Tex0(self):
        return "-\\frac{1}{  "+self.v2_Tex()+"  } "+self.Latex_vect(["b \\cos{t}","a \\sin{t}"])
        
    def VN0(self,t):
        return Vector([
            -self.b*cos(t),
            -self.a*sin(t),
        ])

    def VN_Tex0(self):
        return "-"+self.Latex_vect(["b \\cos{t}","a \\sin{t}"])
        
    def Det0(self,t):
        return self.a*self.b
    
    def Det_Tex0(self):
        return "ab"
        
    def Phi0(self,t):
        return (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )/(self.a*self.b)

    def Phi_Tex0(self):
        return "\\frac{  "+self.v2_Tex()+"   }{ab}"
        
    def Kappa0(self,t):
        return (self.a*self.b)/(  (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )**1.5  )
    
    def Kappa_Te0x(self):
        return "\\frac{ab}{   ("+self.v2_Tex()+")^{3/2}   }"

    def Rho0(self,t):
        return (  (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )**1.5  )/(self.a*self.b)

    def Rho_Te0x(self):
        return "\\frac{   ("+self.v2_Tex()+")^{3/2}   }{ab}"
        
    def Evolute0(self,t):
        return Vector([
            cos(t)**3.0/self.a,
            -sin(t)**3.0/self.b,
        ])*(self.a**2-self.b**2)

    def Evolute_Tex0(self):
        return "\\frac{a^2-b^2}{ab} "+self.Latex_vect(["b \\cos^3{t}","-a \\sin^3{t}"])
        
    def dEvolute_Tex0(self):
        return "-3\\frac{a^2-b^2}{ab} "+self.Latex_vect(["b \\cos^2{t}\\sin{t}","a \\sin^2{t}\\cos{t}"])
        
if (re.search('Descartes.py$',sys.argv[0])):
    curve=Descartes({
    })

    curve.Run()
