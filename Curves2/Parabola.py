from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve

class Parabola(Curve):
    Name="Parabola"

    a=1.0
    N=400

    t1=-3.0
    t2=3.0

    s0=0.0
    
    Show_Point_Nos=[]
    Latex_Figs=[
            [
                [
                    "Parabola/Parabola_Ana_1_000000-400.pdf",
                    "Parabola/Parabola_Ana_2_000000-400.pdf",
                ],
                [ "$a=1$","$a=2$", ],
            ],
    ]
    
    def Curve_Parameters(self):
        return [
            [
                1.0,2.0,3.0,#4.0,5.0
            ],
        ]
    def Curve_Deviations(self):
        return [
            [
                ['$a=1$',[1.0]],
                ['$a=2$',[2.0]],
                ['$a=3$',[3.0]],
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
            "Rho",
            "Evolute","dEvolute",
        ]
    def PMax(self):
        return 0.6*Vector([ self.t2,0.5*self.t2**2 ])
    
    def PMin(self):
        return 0.6*Vector([ self.t1,-0.5*self.t2**2  ])
    
    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        return 2.0
    
    
    def Curve_SVG_Draw(self):
        self.Evolutes_Num.__Canvas__=self.Rs.__Canvas__
        self.dEvolutes_Num.__Canvas__=self.Rs.__Canvas__
        
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
            "",
            ["Parabola",self.a,self.N]
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
        sq=self.SQ(self.t1)

        #Value of curvature in t1
        self.s1=self.a*self.t1*sq/2.0+1.0/(2.0*self.a)*log(self.t1+sq)
        
        return
    
    def Curve_Parameter_Keys(self):
        return [ "a", ]
    
    def Curve_Parameter_Names(self):
        return [ "a", ]

    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.a,
            "%d"  % self.N,
        ]
    
    def R(self,t):
        return Vector([
            t,
            0.5*self.a*t**2,
        ])
    
    def Equation_Tex(self):        
        return "y-y_0=\\frac{1}{2} a (x-x_0)^2"
        
    def Parametrization_Tex(self):        
        return "\\Vector{r}(t)="+self.R_Tex()+",~t \in \mathbb{R}"
    
    def R_Tex(self):        
        return self.Latex_vect([ "t","\\frac{1}{2} at^2"])
        
    #1st Derivative
    def dR_Tex(self):        
        return self.Latex_vect([ "1","at"])
        
    def dR(self,t):
        return Vector([1.0,self.a*t])

    #Curve/Arc Length
    def SQ(self,t):
        return sqrt( t**2+1.0/(self.a**2) )
    
    def Primitive(self,t):
        sq=self.SQ(t)
        
        return 0.5*(   self.a*t*sq+ log(t+sq)/(self.a)   )
    
    def S(self,t):
        u=self.a*t
        sqrtu=(1+u**2)**0.5

        s=u*sqrtu+log(u+sqrtu)
        return s/(2*self.a)
        return self.Primitive(t)-self.s1

    def S_Tex(self):
        sqrt="\\sqrt{ t^2+\\frac{1}{a^2} }"
        return "\\frac{1}{2}\\left\\{ at"+sqrt+"+\\frac{1}{a}\\log{\\left(t+"+sqrt+"\\right)}  \\right\\}"


        
    def d2R(self,t):
        return Vector([0.0,self.a])

    def d2R_Tex(self):        
        return self.Latex_vect([ "0","a"])
        
    def d3R(self,t):
        return O(2)

    def d3R_Tex(self):        
        return self.Latex_Vector("0")
    
    def dv(self,t):
        return self.a*t/sqrt(   1.0+(self.a*t)**2   )
    
    def v2(self,t):
        return 1.0+(self.a*t)**2

    def v2_Tex(self):        
        return "1+a^2t^2\\geq 1"
    
    def dv2(self,t):
        return 2.0*(self.a)**2*t

    def dv2_Tex(self):        
        return "2a^2t"
    
    def t(self,t):
        fact=self.a*t
        sqfact=1.0/sqrt(1.0+fact**2)
        
        return Vector(  [  1.0,fact ]  )*sqfact
    
    def t_Tex(self):        
        return "\\frac{1}{\\sqrt{1+a^2t^2}}"+self.Latex_vect([ "1","at"])

    def n(self,t):
        fact=self.a*t
        sqfact=1.0/sqrt(1.0+fact**2)
        
        return Vector(  [ -fact,1.0 ]  )*sqfact

    def n_Tex(self):        
        return "\\frac{1}{\\sqrt{1+a^2t^2}}"+self.Latex_vect([ "-at","1"])

    def VN(self,t):
        fact=self.a*t
        return Vector(  [ -fact,1 ]  )
        

    def VN_Tex(self):        
        return self.Latex_vect([ "-at","1"])

    def Det(self,t):        
        return self.a
    
    def Det_Tex(self):        
        return "a"
    
    def dDet(self,t):        
        return 0.0
    
    def dDet_Tex(self):        
        return "0"
    
    def Phi(self,t):
        return (1.0+(self.a*t)**2)/(1.0*self.a)

    def Phi_Tex(self):
        return "\\frac{  1+a^2t^2    }{ a }"
    
    def dPhi(self,t):
        return 2.0*self.a*t

    def dPhi_Tex(self):
        return "2at"

    #Psi and derivative
    def Psi(self,t):
        return (1.0*self.a)/(1.0+(self.a*t)**2)

    def Psi_Tex(self):
        return "\\frac{ a }{  1+a^2t^2    }"
    
    def Psi(self,t):
        return (1.0*self.a)/(1.0+(self.a*t)**2)
    
    def dPsi(self,t):
        return -(2.0*self.a**3*t)/(   (1.0+(self.a*t)**2)   )**2
    
    def dPsi_Tex(self):
        return "-\\frac{ 2a^3t }{  (1+a^2t^2)^2    }"
    

    
    def Kappa(self,t):
        return (self.a)/(1.0+(self.a*t)**2)**1.5
    
    def Kappa_Tex(self):
        return "\\frac{a}{  \\sqrt{1+a^2t^2}^{~3}    }"

    #Rho and derivative
    def Rho(self,t):
        return (1.0+(self.a*t)**2)**1.5/(self.a)

    def Rho_Tex(self):
        return "\\frac{  \\sqrt{1+a^2t^2}^{~3}    }{a}"

    def dRho_Tex(self):
        return "3 a t\\sqrt{1+a^2t^2}"
    
    def dRho(self,t):
        return 0.0


    #Oscullating vector
    def RhoV(self,t):
        fact=1.0+(self.a*t)**2

        return Vector([-self.a*t,1])
    
    def RhoV_Tex_Ignoredunnowhy(self):
        return  "\\frac{  1+a^2t^2    }{ a }"+self.Latex_vect([ "-at","1"])
    
    def Evolute(self,t):
        return Vector([
            -t*(self.a*t)**2,
            1.5*self.a*t**2+1.0/self.a,
        ])
    
    def Evolute_Tex(self):
        latex=self.Latex_vect([ "-a^2t^3","\\frac{3}{2}at^2+\\dfrac{1}{a}"])
        return latex
    
    def dEvolute(self,t):
        return Vector([
            -self.a*t**2,
            t
        ])*(3.0*self.a)
    
    def dEvolute_Tex(self):
        latex="3a"+self.Latex_vect([ "-at^2","t"])
        return latex
    
if (re.search('Parabola.py$',sys.argv[0])):
    curve=Parabola({
    })

    curve.Run()
