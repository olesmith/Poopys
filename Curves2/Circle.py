from math import *
import re,sys
sys.path.insert(0,'/root/python')


from R_n import *
from Curve import Curve

class Circle(Curve):
    Name="Circle"
    Title="The Circle"

    r=3.0
    c=Vector([0.0,0.0])
    omega=1.0
    rho=2.0
    
    def PMax(self):
        xmax=self.r
        ymax=self.r
        return Vector([xmax,ymax])
    
    def PMin(self):
        xmin=-self.r
        ymin=-self.r
        return Vector([xmin,ymin])
    
    def Curve_Parameters(self):
        return [
            #Radiuses
            [ 1.0,],
            #Angular velocities
            [ 1.0 ],
        ]
    
    def Curve_Init_Parameters(self):
        return
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.r,
            "%.6f" % self.omega,
            "%d"  % self.N,
        ]
    def Curve_Parameter_Keys(self):
        return ["r","omega" ]
    
    def Curve_Parameter_Names(self):
        return ["r","\\omega"]
   
    def Equation_Tex(self):        
        return "(x-x_0)^2+(y-y_0)^2=r^2"
        
    def Parametrization_Tex(self):        
        return "\\Vector{r}(t)="+self.R_Tex()+",~t \in \mathbb{R}"
    
    def R(self,t):
        return self.c+E(self.omega*t)*self.r
    
    def R_Tex(self,t):
        return "r"+self.Latex_Vector("e", "\\omega t")
    
    def S(self,t):
        return self.omega*t*self.r
    
    def S_Tex(self):
        return "rt"
    
    def Vectors_Tex(self):
        return ",\\quad".join(  self.EF_Vectors("\\omega")  )
    
    def dVectors_Tex(self):
        return ",\\quad".join(  self.EF_dVectors("\\omega")  )
        
    def VectorsN_Tex(self):
        return ",\\quad".join(  self.EF_VectorsN("\\omega")  )
        
    def R_Tex(self):
        return "r"+self.Latex_Vector("e")+"(\\omega t)"
        
    def dR(self,t):
        return F(t)*self.r

    def dR_Tex(self):
        return "r\\omega "+self.Latex_Vector("f")+"(\\omega t)"
        
    def d2R(self,t):
        return E(t)*(-self.r)

    def d2R_Tex(self):
        return "-r\\omega^2"+self.Latex_Vector("e")+"(\\omega t)"
        
    def d3R(self,t):
        return F(t)*(-self.r)

    def d3R_Tex(self):
        return "-r\\omega^3 "+self.Latex_Vector("f")+"(\\omega t)"
        
    def v2(self,t):
        return self.r**2.0

    def v2_Tex(self):
        return "r^2\\omega^2"
        
    def t(self,t):
        return F(t)

    def t_Tex(self):
        return self.Latex_Vector("f")+"(\\omega t)"
        
    def n(self,t):
        return E(t)*(-1.0)

    def n_Tex(self):
        return "-"+self.Latex_Vector("e")+"(\\omega t)"
        
    def Phi(self,t):
        return 1.0
    
    def Phi_Tex(self):
        return "1"

    def VN(self,t):
        return E(t)*(-self.r)
    
    def VN_Tex(self):
        return "-r\\omega"+self.Latex_Vector("e")+"(\\omega t)"

    def Det(self,t):
        return self.r**2.0
    
    def Det_Tex(self):
        return "r^2\\omega^3"

    def Kappa(self,t):
        return 1.0/self.r

    def Kappa_Tex(self):
        return "\\frac{1}{r}"

    def Rho(self,t):
        return self.r

    def Rho_Tex(self):
        return "r"

    def dRho(self,t):
        return 0

    def dRho_Tex(self):
        return "0"

    def Psi(self,t):
        return self.omega

    def Psi_Tex(self):
        return "\\omega"

    def Phi(self,t):
        return 1.0/self.omega

    def Phi_Tex(self):
        return "\\frac{1}{\\omega}"

    def RhoV(self,t):
        return E(t)*(-self.r)
    
    def RhoV_Tex(self):
        return "-r"+self.Latex_Vector("e")+"(t)"


    def Evolute(self,t):
        return O(2)

    def Evolute_Tex(self):
        return self.Latex_Vector("0")
    
    def dEvolute(self,t):
        return O(2)

    def dEvolute_Tex(self):
        return self.Latex_Vector("0")

    def SPs_Tex(self):
        return "\\emptyset"

    def Evolute_SPs_Tex(self):
        return "\\emptyset"

if (re.search('Circle.py$',sys.argv[0])):
    curve=Circle({
    })

    curve.Run()
