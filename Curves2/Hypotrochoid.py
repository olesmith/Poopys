from math import *
import re,sys
sys.path.insert(0,'/root/python')


from R_n import *
from Curve import Curve

class Hypotrochoid(Curve):
    Name="Hypotrochoid"

    r=1.0
    RR=3.0
    b=-2.0
    N=400
    
    #Nondimensional quantities
    Omega=2.0
    Lambda2=3.0
    
    def PMax(self):
        xmax=self.RR+self.r+abs(self.b)
        return Vector([xmax,xmax])
    
    def PMin(self):
        xmax=self.RR+self.r+abs(self.b)
        return Vector([-xmax,-xmax])
    
    def Curve_Parameters(self):
        return [
            [ 1.0,],
            [
                2.0,3.0,4.0,5.0,
                1.0/2.0,1.0/3.0,1.0/4.0,1.0/5.0,
            ],
            [
                0.0,1.0,2.0,3.0,4.0,5.0,
            ]
        ]
    
    def Curve_Init_Parameters(self):
        self.t2=max(2*pi,2.0*self.r/self.RR*pi)
        
        self.Omega=(self.r-self.RR)/self.r
        self.Omega_P=self.Omega+1.0
        self.Omega_M=self.Omega-1.0
        
        self.Lambda=(self.r+self.b)/self.r
        self.Lambda2=self.Lambda**2
    
        self.rOmega=self.r*self.Omega
        self.rOmega2=self.rOmega**2.0
        
        self.LambdaOmega=self.Lambda*self.Omega
        self.Lambda2Omega=self.Lambda**2.0*self.Omega
        self.LambdaOmega2=self.Lambda*(self.Omega**2.0)
        
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
    
    def Parameters_Tex(self):
        return "\\omega=\\frac{R-r}{r}, \\quad \\lambda=\\frac{r+b}{r}"
    
    def Parametrization_Tex(self):
        return self.Latex_vect([
            "(R-r)\\cos{t}+(r+b) \\cos{\\omega t}",
            "(R-r)\\sin{t}-(r+b) \\sin{\\omega t}"
        ])+",~R,r>0,~b \\in \mathbb{R}, ~ t \\in \\mathbb{R}"
    
    def Vectors_Tex(self):        
        return ",\\quad".join( self.PQ_Vectors() )

    def dVectors_Tex(self):        
        return ";\\quad".join([
            ",\\quad".join( self.PQ_dVectors() ),
            ",\\quad".join( self.PQ_VectorsN() )
        ])

    def R(self,t):
        tt=t*self.Omega
        return (    E(t)*self.Omega-P(tt)*self.Lambda    )*self.r
    
    def R_Tex(self):        
        return "r"+self.Latex_Left_Right(
            " ".join([
                "\\omega"+self.Latex_Vector("e")+"(t)",
                "-",
                "\\lambda"+self.Latex_Vector("p")+"(\\omega t)"
            ]),"\\{")
        
    def dR(self,t):
        tt=t*self.Omega
        return (    F(t)+Q(tt)*self.Lambda    )*(self.rOmega)
    
    def dR_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                self.Latex_Vector("f")+"(t)",
                "+",
                "\\lambda"+self.Latex_Vector("q")+"(\\omega t)"
            ],
            "\\{"
        )
        
        
    def d2R(self,t):
        return (    -E(t)+P(t,self.Omega)*(self.LambdaOmega)    )*(self.rOmega)

    def d2R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                "-",
                self.Latex_Vector("e")+"(t)",
                "+",
                "\\lambda\\omega"+self.Latex_Vector("p")+"(\\omega t)"
            ],
            "\\{"
        )
        
    def d3R(self,t):
        return (    -F(t)-Q(t,self.Omega)*(self.LambdaOmega2)    )*(self.rOmega)
    
    def d3R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                "-",
                self.Latex_Vector("f")+"(t)",
                "-",
                "\\lambda\\omega^2"+self.Latex_Vector("q")+"(\\omega t)"
            ],
            "\\{",
        )
        
    def Cost(self,t):
        return cos( self.Omega_P*t )
    
    def Cost(self,t):
        return cos( self.Omega_P*t )
    
    def v2(self,t):
        cost=self.Cost(t)
        return (1.0+self.Lambda2-2.0*self.Lambda*cost)*(self.rOmega2)

    def v2_Canonical_Tex(self):        
        return "1+\\lambda^2-2\\lambda \cos{ (\omega+1)t}"
    
    def v2_Tex(self):        
        return "r^2\\omega^2"+self.Latex_Left_Right(  self.v2_Canonical_Tex(),"\\{"  )
    
    def t(self,t):
        return self.dR(t).Normalize()

    def n(self,t):
        return self.dR(t).Hat2().Normalize()

    def VN(self,t):
        tt=t*self.Omega
        return (    -E(t)-P(tt)*self.Lambda    )*(self.rOmega)

    def VN_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                "-",
                self.Latex_Vector("e")+"(t)",
                "-",
                "\\lambda"+self.Latex_Vector("p")+"(\\omega t)"
            ],
            "\\{"
        )

    def Det(self,t):
        cost=self.Cost(t)
        return (   1.0-self.Lambda2Omega   +   self.Lambda*self.Omega_M*cost   )*(self.rOmega2)
    
    def Det_Canonical_Tex(self):        
        return "1-\\lambda^2 \\omega   + \\lambda(\\omega-1) \\cos{ (\\omega+1)t}"
    
    def Det_Tex(self):
        return "r^2\\omega^2"+self.Latex_Left_Right(  self.Det_Canonical_Tex(),"\\{"  )
    
    
    def Phi(self,t):
        cost=self.Cost(t)

        det=1.0-self.Lambda2Omega   +   self.Lambda*self.Omega_M*cost
         
        phi=0.0
        if (det!=0.0):
            v2=1.0+self.Lambda2-2.0*self.Lambda*cost
            phi=v2/det
            
        return phi

    def Phi_Tex(self):
        return "\\frac{  "+self.v2_Canonical_Tex()+"    }{"+ self.Det_Canonical_Tex()+"}"
    
    def Kappa(self,t):
        cost=self.Cost(t)
        
        v22=(1.0+self.Lambda2  -  2.0*self.Lambda*cost)*(self.rOmega2)
        #v2= (1.0+self.Lambda2  -  2.0*self.Lambda*cost)
         
        kappa=None
        if (v22!=0.0):
            det2=(1.0-self.Lambda2Omega   +   self.Lambda*self.Omega_M*cost)*(self.rOmega2)
            #det= (1.0-self.Lambda2Omega   +   self.Lambda*self.Omega_M*cost)
            kappa=det2/pow(v22,1.5)
            #kappa=kappa/self.rOmega
            
        return kappa

    def Kappa_Tex(self):
        latex="\\sqrt{"+ self.v2_Canonical_Tex()+"}"
        
        return "\\frac{1}{ r \\omega }\\cdot \\frac{  "+self.Det_Canonical_Tex()+"    }{   "+latex+"^3   }"
    
    def Rho(self,t):
        cost=self.Cost(t)
                
        det=self.Det(t)
        
        rho=None
        if (det!=0.0):
            rho=self.v2(t)**1.5/det
            
        return rho

    def Rho_Tex00(self):
        latex="\\sqrt{"+ self.v2_Canonical_Tex()+"}"
        return "r \\omega \\cdot \\frac{   "+latex+"^3    }{"+ self.Det_Canonical_Tex()+"}"
    
    def RhoV(self,t):
        r=-E(t)-E( self.Omega*t )*self.Lambda

        return r*self.Phi(t)*self.r
    
    def RhoV_Tex00(self):
        return "-r"+self.Latex_Vector("e")+"(t)"
            
    def Evolute(self,t):
        phi=self.Phi(t)
        fact1=(1.0-phi)*self.Omega
        fact2=self.Lambda*(1+self.Omega*phi)
        
        return (    E(t)*fact1-P( self.Omega*t )*fact2    )*self.r
    
    def Evolute_Tex(self):
        latex=[
            "\\omega(1-\\varphi(t))"+self.Latex_Vector("e")+"(t)",
            "-",
            "\\lambda (1+\\omega \\varphi(t))"+self.Latex_Vector("p")+"(\\omega t)",
        ]
        return "r"+self.Latex_Left_Right(  "\n".join(latex),"\\{"  )
    
if (re.search('Hypotrochoid.py$',sys.argv[0])):
    curve=Hypotrochoid({
    })

    curve.Run()
