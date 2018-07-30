from math import *
import re,sys
sys.path.insert(0,'/root/python')

from R_n import *
from Curve import Curve

class Epicycloid(Curve):
    Name="Epicycloid"

    r=1.0
    RR=1.0
    b=0.0
    N=400
    
    #Nondimensional quantities
    Omega=2.0

    xmax=5.0
    ymax=5.0
    
    Latex_Figs=[
            [
                [
                    "Epicycloid/Epicycloid_Ana_1_000000-1_000000-400.pdf",
                ],
                [ "Epicycloid, $r=1$", ],
            ],
            [
                [
                    "Epicycloid/Epicycloid_Functions_Ana_1_000000-1_000000-400.pdf",
                ],
                [ "Epicycloid Functions, $r=1$", ],
            ],
            [
                [
                    "Epicycloid/Epicycloid_Ana_1_000000-2_000000-400.pdf",
                ],
                [ "Epicycloid, $r=1$", ],
            ],
            [
                [
                    "Epicycloid/Epicycloid_Functions_Ana_1_000000-2_000000-400.pdf",
                ],
                [ "Epicycloid Functions, $r=1$", ],
            ],
            [
                [
                    "Epicycloid/Epicycloid_Ana_1_000000-3_000000-400.pdf",
                ],
                [ "Epicycloid, $r=1$", ],
            ],
            [
                [
                    "Epicycloid/Epicycloid_Functions_Ana_1_000000-3_000000-400.pdf",
                ],
                [ "Epicycloid Functions, $r=1$", ],
            ],
            [
                [
                    "Epicycloid/Epicycloid_Ana_1_000000-4_000000-400.pdf",
                ],
                [ "Epicycloid, $r=1$", ],
            ],
            [
                [
                    "Epicycloid/Epicycloid_Functions_Ana_1_000000-4_000000-400.pdf",
                ],
                [ "Epicycloid Functions, $r=1$", ],
            ],
             #[
            #    [
            #        "Epicycloid/Epicycloid_dFunctions_Ana_1_000000-400.pdf",
            #    ],
            #    [ "Epicycloid Function Derivatives, $r=1$", ],
            #],
    ]
    
    def Curve_Parameters(self):
        return [
            [ 1.0,],
            [
                1.0,2.0,3.0,4.0,5.0,
                1.0/2.0,1.0/3.0,1.0/4.0,1.0/5.0,
            ],
        ]
    
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([-self.xmax,-self.ymax])
    
    def Curve_Init_Parameters(self):
        self.t2=max(2*pi,2.0*self.r/self.RR*pi)
        
        self.Omega=(self.r+self.RR)/self.r
        self.Omega_P=self.Omega+1.0
        self.Omega_M=self.Omega-1.0
        
        self.R_Factor=self.RR/( self.RR+2.0*self.r)
        self.R_Factor_Tex="\\frac{R}{R+2r}"

     
    def Curve_Parameter_Keys(self):
        return [ "RR","r" ]
    def Curve_Parameter_Names(self):
        return [ "R","r" ]
    

    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.RR,
            "%.6f" % self.r,
            "%d"  % self.N,
        ]
    
    def Parametrization_Tex(self):
        return self.Latex_Vector("r")+"(t)="+self.Latex_vect([
            "(R+r)\\cos{t}-r \\cos{\\omega t}",
            "(R+r)\\sin{t}+r \\sin{\\omega t}"
        ])+",\\quad t \\in \\mathbb{R}"
    

    def Parameters_Tex(self):
        return "\\omega=\\frac{R+r}{r}"
    

    def Vectors_Tex(self):        
        return ",\\quad".join([
            "=".join([
                self.Latex_Vector("e")+"(\\omega t)",
                self.Latex_vect(["\\cos{\\omega t}","\\sin{\\omega t}"]),
            ]),
            "=".join([
                self.Latex_Vector("f")+"(\\omega t)",
                self.Latex_vect(["-\\sin{\\omega t}","\\cos{\\omega t}"]),
            ]),
        ])

    def dVectors_Tex(self):        
        return "=".join([
            "=".join([
                "\\cdot".join([
                    self.Latex_Vector("e")+"( t)",
                    self.Latex_Vector("e")+"(\\omega t)",
                ]),
                "\\cdot".join([
                    self.Latex_Vector("f")+"( t)",
                    self.Latex_Vector("f")+"(\\omega t)",
                ]),
                "\\cos{(\\omega-1)t}"
            ]),
        ])
    
    def R(self,t):
        return (    E(t)*self.Omega-E(t,self.Omega)   )*self.r
    
    def R_Tex(self):        
        return "r\\left\\{   "+" ".join([
            "\\omega"+self.Latex_Vector("e")+"(t)",
            "-",
            self.Latex_Vector("e")+"(\\omega t)"
        ])+"   \\right\\}"
        
    def dR(self,t):
        return (    F(t)-F(t,self.Omega)   )*(self.r*self.Omega)
    
    def dR_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            self.Latex_Vector("f")+"(t)",
            "-",
            self.Latex_Vector("f")+"(\\omega t)"
        ],"\\{")
        
    def S_Tex_Name(self):
        return "s(t)-s(0)"
    def S_Tex(self):        
        return "\\frac{2r\\omega}{\\omega-1} \cdot \\left(1-\\cos{ \\frac{\\omega-1}{2} t}\\right),~0 < t < \\frac{2\\pi}{\\omega-1}"

    def d2R(self,t):
        return (    -E(t)+E(t,self.Omega)*(self.Omega)    )*(self.r*self.Omega)

    def d2R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            "-",
            self.Latex_Vector("e")+"(t)",
            "+",
            "\\omega"+self.Latex_Vector("e")+"(\\omega t)"
        ],"\\{")
        
    def d3R(self,t):
        return (    -F(t)+F(t,self.Omega)*(self.Omega**2)    )*(self.r*self.Omega)
    
    def d3R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            "-",
            self.Latex_Vector("f")+"(t)",
            "+",
            "\\omega^2"+self.Latex_Vector("f")+"(\\omega t)"
        ])
        
    def v2(self,t):
        return 2.0*(1.0-cos( (self.Omega-1.0)*t ))*((self.r*self.Omega)**2)
    
    def v2_Canonical_Tex(self):        
        return "2(1- \\cos{ (\\omega-1)t})"
    
    def v2_Tex(self):        
        return "2r^2\\omega^2"+self.Latex_Left_Right( "1- \\cos{ (\\omega-1)t}" )
    
    def dv2(self,t):
        return 2.0*sin( (self.Omega-1.0)*t )*((self.r*self.Omega)**2)*(self.Omega-1.0)

    def dv2_Tex(self):        
        return "2r^2\\omega^2(\omega-1)\\sin{ (\omega-1)t}"
    
    def t(self,t):
        return self.dR(t).Normalize()

    def t_Tex(self):        
        return " ".join([
            "\\frac{",
            self.Latex_Vector("f")+"(t)",
            "-",
            self.Latex_Vector("f")+"(\\omega t)",
            "}{",
            "\\sqrt{",
            self.v2_Canonical_Tex(),
            "}}",
        ])
    
    def n(self,t):
        return self.dR(t).Hat2().Normalize()

    def n_Tex(self):        
        return " ".join([
            "-\\frac{",
            self.Latex_Vector("e")+"(t)",
            "-",
            self.Latex_Vector("e")+"(\\omega t)",
            "}{",
            "\\sqrt{",
            self.v2_Canonical_Tex(),
            "}}",
        ])
    
    def VN(self,t):
        return (    -E(t)+E(t,self.Omega)    )*(self.r*self.Omega)

    def VN_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            "-",
            self.Latex_Vector("e"),
            "+",
            self.Latex_Vector("e")+"(\\omega t)"
        ])

    def Det(self,t):
        omegap=self.Omega+1.0
        omegam=self.Omega-1.0
        
        return omegap*(1.0-cos( omegam*t ))*((self.r*self.Omega)**2)
    
    def Det_Canonical_Tex(self):        
        return "(1+ \\omega)(1 -\\cos{ (\\omega-1)t})"
    
    def Det_Tex(self):
        return "r^2\\omega^2"+ self.Det_Canonical_Tex()
    
    
    def dDet(self,t):
        omegap=self.Omega+1.0
        omegam=self.Omega-1.0
        
        return omegap*omegam*sin( omegam*t )*((self.r*self.Omega)**2)
    
    def dDet_Tex(self):
        return "r^2\\omega^2(\omega^2-1) \\sin{(\\omega-1)t}"
    
    
    def Phi(self,t):
        cost=cos( self.Omega_M*t )
        det=1.0+self.Omega-self.Omega_P*cost
        if (det!=0.0):
            return 2.0/(1.0+self.Omega)
        return 0.0
       
        return phi
    def Psi(self,t):
        cost=cos( self.Omega_M*t )
        v2=2.0*(1.0-cost)
        if (v2!=0.0):
            return (1.0+self.Omega)/2.0
        return 0.0

    def Phi_Tex(self):
        return "\\frac{2}{1+\omega}=\\frac{2r}{R+2r}"
    
    def Psi_Tex(self):
        return "\\frac{1+\omega}{2}=\\frac{R+2r}{2r}"
    
    def Kappa(self,t):
        cost=cos( self.Omega_M*t )
        sqr=(1.0-cost)**0.5
        
        kappa=None
        if (sqr!=0.0):
            kappa=self.Omega_P/(  2**1.5*self.r*self.Omega*sqr  )
            
        return kappa

    def Kappa_Tex(self):
        latex=self.v2_Canonical_Tex()
        
        return "\\frac{1+\\omega}{2\\sqrt{2}r\omega} \cdot \\frac{1}{\\sqrt{1 -\\cos{ (\\omega-1)t}}}"
    
    def Rho(self,t):
        cost=cos( self.Omega_M*t )
        sqr=(1.0-cost)**0.5

        rho=2**1.5*self.r*self.Omega*sqr/self.Omega_P

        return rho

    def dRho(self,t):
        cost=cos( self.Omega_M*t )
        sint=sin( self.Omega_M*t )
        sqr=(1.0-cost)**0.5

        drho=None
        if (sqr!=0.0):
            drho=2.0**0.5*self.r*self.Omega*sint/(  (1.0+self.Omega)*sqr  )

        return drho

    def Rho_Tex(self):
        latex=self.v2_Canonical_Tex()
        return "\\frac{2\\sqrt{2}r\omega}{1+\\omega} \cdot \\sqrt{1-\\cos{ (\\omega-1)t}}"
    
    def dRho_Tex(self):
        latex=self.v2_Canonical_Tex()
        return "\\sqrt{2}r\\omega \\cdot \\frac{\\omega-1 }{1+\\omega} \cdot \\frac{\\sin{(\\omega-1)t}}{\\sqrt{1 -\\cos{ (\\omega-1)t}}}"
    
    def RhoV(self,t):
        r=-E(t)+E( self.Omega*t )

        return r*(self.Phi(t)*self.r*self.Omega)
    
    def RhoV_Tex00(self):
        return "-r"+self.Latex_Vector("e")+"(t)"
            
    def Evolute(self,t):
        fact1=(self.RR+self.r)*self.R_Factor
        fact2=self.r*self.R_Factor
        
        return (    E(t)*fact1+E( self.Omega*t )*fact2    )
    
    def Evolute_Tex(self):
        latex=[
            "(R-r)"+self.Latex_Vector("e")+"(t)",
            "+",
            "r"+self.Latex_Vector("e")+"(\\omega t)"
        ]
        return self.R_Factor_Tex+self.Latex_Left_Right(  "\n".join(latex),"(" )
    
if (re.search('Epicycloid.py$',sys.argv[0])):
    curve=Epicycloid({
    })

    curve.Run()
