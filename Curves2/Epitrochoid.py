from math import *
import re,sys
sys.path.insert(0,'/root/python')

from R_n import *
from Curve import Curve

class Epitrochoid(Curve):
    Name="Epitrochoid"

    r=1.0
    RR=1.0
    b=0.0
    N=400
    
    #Nondimensional quantities
    Omega=2.0
    Lambda2=3.0

    xmax=5.0
    ymax=5.0
    
    def Curve_Parameters(self):
        return [
            [ 1.0,],
            [
                1.0,2.0,3.0,4.0,5.0,
                1.0/2.0,1.0/3.0,1.0/4.0,1.0/5.0,
            ],
            [
                0.0,1.0,2.0,3.0,4.0,5.0,
            ]
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
        
        self.Lambda=(self.r+self.b)/self.r
        self.Lambda2=self.Lambda**2
    
    def Curve_Parameter_Keys(self):
        return [ "RR","r","b" ]
    def Curve_Parameter_Names(self):
        return [ "R","r","b" ]
    

    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.RR,
            "%.6f" % self.r,
            "%.6f" % self.b,
            "%d"  % self.N,
        ]
    
    def Parametrization_Tex(self):
        return self.Latex_vect([
            "(R+r)\\cos{t}-(r+b) \\cos{\\omega t}",
            "(R+r)\\sin{t}+(r+b) \\sin{\\omega t}"
        ])+",\\quad t \\in \\mathbb{R}"
    
    def Vectors_Tex(self):        
        return ",\\quad".join( self.EF_Vectors() )

    def dVectors_Tex(self):        
        return ";\\quad".join([
            ",\\quad".join( self.EF_dVectors() ),
            ",\\quad".join( self.EF_VectorsN() )
        ])
    
    def R(self,t):
        return (    E(t)*self.Omega-E(t,self.Omega)*self.Lambda    )*self.r
    
    def R_Tex(self):        
        return "r\\left(   "+" ".join([
            "\\omega"+self.Latex_Vector("e")+"(t)",
            "-",
            "\\lambda"+self.Latex_Vector("e")+"(\\omega t)"
        ])+"   \\right)"
        
    def dR(self,t):
        return (    F(t)-F(t,self.Omega)*self.Lambda    )*(self.r*self.Omega)
    
    def dR_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            self.Latex_Vector("f")+"(t)",
            "-",
            "\\lambda"+self.Latex_Vector("f")+"(\\omega t)"
        ],"(")
        
        
    def d2R(self,t):
        return (    -E(t)+E(t,self.Omega)*(self.Lambda*self.Omega)    )*(self.r*self.Omega)

    def d2R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            "-",
            self.Latex_Vector("e")+"(t)",
            "+",
            "\\lambda\\omega"+self.Latex_Vector("e")+"(\\omega t)"
        ],"(")
        
    def d3R(self,t):
        return (    -F(t)+F(t,self.Omega)*(self.Lambda*self.Omega**2)    )*(self.r*self.Omega)
        return P(t)*(   -self.Lambda*self.r   )
    
    def d3R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            "-",
            self.Latex_Vector("f")+"(t)",
            "+",
            "\\lambda\\omega^2"+self.Latex_Vector("f")+"(\\omega t)"
        ])
        
    def v2(self,t):
        return (1.0+self.Lambda2-2.0*self.Lambda*cos( (self.Omega-1.0)*t ))*((self.r*self.Omega)**2)

    def v2_Canonical_Tex(self):        
        return "1+\\lambda^2-2\\lambda \cos{ (\omega-1)t}"
    
    def v2_Tex(self):        
        return "r^2\\omega^2"+self.Latex_Left_Right(  self.v2_Canonical_Tex(),"("  )
    
    def t(self,t):
        return self.dR(t).Normalize()

    def n(self,t):
        return self.dR(t).Hat2().Normalize()

    def VN(self,t):
        return (    -E(t)+E(t,self.Omega)*self.Lambda    )*(self.r*self.Omega)

    def VN_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right([
            "-",
            self.Latex_Vector("e"),
            "+",
            "\\lambda"+self.Latex_Vector("e")+"(\\omega t)"
        ])

    def Det(self,t):
        lambda2=(self.Lambda**2)
        omegap=self.Omega+1.0
        omegam=self.Omega-1.0
        
        return (1.0+lambda2*self.Omega-self.Lambda*omegap*cos( omegam*t ))*((self.r*self.Omega**2))
    
    def Det_Canonical_Tex(self):        
        return "1+\\lambda^2 \\omega - \\lambda(\\omega+1) \\cos{ (\\omega-1)t}"
    
    def Det_Tex(self):
        return "r^2\\omega^2"+self.Latex_Left_Right(  self.Det_Canonical_Tex(),"("  )
    
    
    def Phi(self,t):
        cost=cos( self.Omega_M*t )
        
        det=1.0+self.Lambda2*self.Omega-self.Lambda*self.Omega_P*cost
        v2=1+self.Lambda2-2*self.Lambda*cost
        
        phi=0.0
        if (det!=0.0):
            phi=v2/det
            
        return phi

    def Phi_Tex(self):
        return "\\frac{  "+self.v2_Canonical_Tex()+"    }{"+ self.Det_Canonical_Tex()+"}"
    
    def Kappa(self,t):
        cost=cos( self.Omega_M*t )
        
        det=1.0+self.Lambda2*self.Omega-self.Lambda*self.Omega_P*cost
        v2=1+self.Lambda2-2.0*self.Lambda*cost
        
        kappa=None
        if (v2!=0.0):
            kappa=det/(v2**1.5*self.r*self.Omega)
            
        return kappa

    def Kappa_Tex(self):
        latex="\\sqrt{"+ self.v2_Canonical_Tex()+"}"
        
        return "\\frac{1}{r \omega}\\cdot \\frac{  "+self.Det_Canonical_Tex()+"    }{"+latex+"^3   }"
    
    def Rho(self,t):
        cost=cos( self.Omega_M*t )
        det=1.0+self.Lambda2*self.Omega-self.Lambda*self.Omega_P*cost
        v2=1+self.Lambda2-2.0*self.Lambda*cost
        
        rho=0.0
        if (det!=0.0):
            rho=(v2**1.5)/det
            
        return rho*(self.r*self.Omega)
    def dRho(self,t):
        cost=cos( self.Omega_M*t )
        det=1.0+self.Lambda2*self.Omega-self.Lambda*self.Omega_P*cost
        v2=1+self.Lambda2-2.0*self.Lambda*cost
        
        rho=0.0
        if (det!=0.0):
            rho=(v2**1.5)/det
            
        return rho*(self.r*self.Omega)

    def Rho_Tex(self):
        latex="\\sqrt{"+ self.v2_Canonical_Tex()+"}"
        return "r \\omega \\cdot\\frac{ "+latex+"^3    }{"+ self.Det_Canonical_Tex()+"}"
    
    def RhoV(self,t):
        r=-E(t)+E( self.Omega*t )*self.Lambda

        return r*(self.Phi(t)*self.r*self.Omega)
    
    def RhoV_Tex00(self):
        return "-r"+self.Latex_Vector("e")+"(t)"
            
    def Evolute(self,t):
        phi=self.Phi(t)
        fact1=(1.0-phi)*self.Omega
        fact2=self.Lambda*(1-self.Omega*phi)
        return (    E(t)*fact1-E( self.Omega*t )*fact2    )*self.r
    
    def Evolute_Tex(self):
        latex=[
            "\\omega(1-\\varphi)"+self.Latex_Vector("e")+"(t)",
            "-",
            "(1-\\omega \\varphi)"+self.Latex_Vector("e")+"(\\omega t)",
        ]
        return "r"+self.Latex_Left_Right(  "\n".join(latex),"("  )
    
if (re.search('Epitrochoid.py$',sys.argv[0])):
    curve=Epitrochoid({
    })

    curve.Run()
