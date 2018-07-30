from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n     import *
from Curve   import Curve
from Rolling import Rolling
from Line    import Line

class Cycloid(Curve,Rolling):
    Name="Cycloid"

    Resolution=[600,1200]
    
    N=400
    Frenet_Every=45
    
    t1=-0.5*pi
    t2=2.5*pi
    
    xmax=2.25*pi
    xmin=-0.25*pi
    ymax=2.0
    ymin=-2.0

    
    rolling_t=5.0/3.0*pi
    rolling_ts=[
        2.0/3.0*pi,
        5.0/3.0*pi,
    ]

    Functions_Show={
        "Functions": [
            "v2","Det",
            "Psi","Phi",
            "Kappa","Rho",
        ],
         "vD": [
            "v2","Det","S"
        ],
        "Phsi": [
            "Psi","Phi",
        ],
        "Kaprho": [
            "Kappa","Rho",
        ]
    }

    Latex_Figs=[
            [
                [
                    "Cycloid/Cycloid_Ana_1_000000-400.pdf",
                ],
                [ "Cycloid, $r=1$", ],
            ],
            [
                [
                    "Cycloid/Cycloid_Functions_Ana_1_000000-400.pdf",
                ],
                [ "Cycloid Functions, $r=1$", ],
            ],
            #[
            #    [
            #        "Cycloid/Cycloid_dFunctions_Ana_1_000000-400.pdf",
            #    ],
            #    [ "Cycloid Function Derivatives, $r=1$", ],
            #],
    ]
    
    ##! 
    ##! Generate curve legends insertion point.
    ##!

    def Curve_Legend_Inserts000(self,meshes):
        return [-5.0,0.0],[0,-1.0]
    
    ##!
    ##! Override Curve_Functions_Canvas_MaxMin
    ##!

    def Curve_Functions_Canvas_MaxMin(self):
        return Vector([self.t1,-5.0]),Vector([self.t2,3.0])
    
    ##!
    ##! Initialize base curve: the x-axis
    ##!

    def Curve_Base_Get(self):
        curve=Line()
        parms={
            "N": self.N,
            "a": 1.0,
            "t1": self.t1,
            "t2": self.t2,
        }
        curve.__Init__(parms)
        curve.__Calc__()
            
        return curve
        
    ##! 
    ##! Calculates functions max/min values
    ##!1
    def Curve_Functions_MaxMin(self,meshes):
        return Vector([-1.570796,-5.0 ]), Vector([7.853982,3.999860])

 
    ##!
    ##! Generate cycloid with rolling circle as SVG.
    ##!

    def Cycloid_SVG(self,type):
        svg=[]
        svg=svg+self.Mesh_Curve_SVG(
            "R",
            "",
            self.Curve_Component_Get("R","Color",type)
        )

        svg=svg+self.Mesh_Curve_SVG(
            "Evolute",
            type,
            self.Curve_Component_Get("Evolute","Color",type)
        )

        #Number points inself.rolling_ts 
        for t in self.rolling_ts:
            svg=svg+self.Point_Draw(
                self.R(t),
                self.Curve_Component_Get("R","Color","Points"),
                self.Curve_Thickness+2
            )
            svg=svg+self.Point_Draw(
                self.Evolute(t),
                self.Curve_Component_Get("Evolute","Color","Points"),
                self.Curve_Thickness+2
            )

        #Draw rolling circle for t=self.rolling_t
        svg=svg+self.Circle_Draw(
            self.Rolling_Center(self.rolling_t),
            self.r,
            self.Curve_Component_Get("R","Color","Rolling"),
            2,
            True
        )

        return svg

                         
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([self.xmin,self.ymin])
    
    def Curve_Init_Parameters(self):

        self.__R__={}
        return
    
    def Curve_Parameters(self):
        return [
            [
                #0.5,
                #0.6,0.7,0.8,0.9,
                1.0
            ],
        ]
                
    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        return [
            [ self.xmin,0.0 ],
            [ self.xmax,0.0 ],
            [ 0.0,self.ymin ],
            [ 0.0,self.ymax ],
        ]

    def Curve_Parameter_Keys(self):
        return [ "r" ]
    
    def Curve_Parameter_Names(self):
        return [ "r" ]
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.r,
            "%d"   % self.N,
        ]
    

    def Parametrization_Tex(self):        
        return "\\Vector{r}(t)="+self.Latex_vect([ "r(t-\\sin{t})","r(1-\\cos{t})" ])
        
    def Vectors_Tex(self):        
        return ",\\quad".join( self.PQ_Vectors() )

    def dVectors_Tex(self):        
        return ";\\quad".join([
            ",\\quad".join( self.PQ_dVectors() ),
        ])
    
    def VectorsN_Tex(self):        
        return ";\\quad".join([
            ",\\quad".join( self.PQ_VectorsN() )
        ])

    def R000(self,t):
        return (    I(2)*t + J(2) + Q(t)    )*self.r
    
    def R_Tex(self):        
        return "r\\left(   "+" ".join([
            "t"+self.Latex_Vector("i"),
            "+",
            self.Latex_Vector("j"),
            "+",
            self.Latex_Vector("q")+"(t)"
        ])+"   \\right)"
        
    def dR(self,t):
        return (  I(2)+P(t)  )*self.r
    
    def dR_Tex(self):        
        return "r\\left(   "+" ".join([
            self.Latex_Vector("i"),
            "+",
            self.Latex_Vector("p")+"(t)"
        ])+"   \\right)"
        
    def SPs_Tex(self):        
        return "".join([
            "\\left\\{",
            "   \\left(\\begin{array}{c}",
            "      2 p \\pi\\\\0",
            "   \\end{array}\\right),",
            "   ~p \\in \\mathbb{Z}",
            "\\right\\}"
        ])
        
    def S(self,t):
        n=0
        while (t<0.0):
            n+=1
            t+=2.0*pi

        while (t>2.0*pi):
            n-=1
            t-=2.0*pi

        sround=8.0*n*self.r
        s=4.0*self.r*(1.0-cos(t/2.0))

        return s-sround
    
    def S_Tex(self):        
        return "4\\sqrt{2} r\\left[   \\cos{   \\frac{t}{2}   }   \\right]_{t}^{t_0} ,~0<t-t_0<2\\pi"

    
    def d2R(self,t):
        return Q(t)*(   -self.r   )

    def d2R_Tex(self):        
        return " ".join([
            "-r"+self.Latex_Vector("q")+"(t)"
        ])
            
    def d3R(self,t):
        return P(t)*(   -self.r   )

    def d3R_Tex(self):        
        return " ".join([
            "-r"+self.Latex_Vector("p")+"(t)"
        ])
        
    def v2(self,t):
        return 2.0*(1.0-cos(t))

    def v2_Tex(self):        
        return "2r^2\\left(  1-\\cos{t}  \\right)"
    
    def dv2(self,t):
        return 2.0*sin(t)

    def dv2_Tex(self):        
        return "2r^2\\sin{t}"
    
    def v_Tex(self):        
        return "\\sqrt{2} r\\sqrt{  1-\\cos{t}  }"
    
    def t(self,t):
        return self.dR(t).Normalize()

    def t_Tex(self):
        denominator=" ".join([
            self.Latex_Vector("i"),
            "+",
            self.Latex_Vector("p")+"(t)"
        ])
        
        return "\\frac{"+denominator+"}{\\sqrt{2(1-\cos{t})}}"

    def n_Tex(self):
        denominator=" ".join([
            self.Latex_Vector("j"),
            "+",
            self.Latex_Vector("q")+"(t)"
        ])
        
        return "\\frac{"+denominator+"}{\\sqrt{2(1-\cos{t})}}"

    def n(self,t):
        T=self.t(t)
        if (T!=None):
            return self.t(t).Hat2()

        return None

    def VN(self,t):
        return (  J(2)+Q(t)  )*self.r

    def VN_Tex(self):        
        return "r\left(   "+" ".join([
            self.Latex_Vector("j"),
            "+",
            self.Latex_Vector("q")+"(t)"
        ])+"   \\right)"
    
    def Det(self,t):
        return (-1.0+cos(t))*self.r**2
    
    def Det_Tex(self):        
        return "r^2\\left(  \\cos{t}-1   \\right)\\leq 0"
    
    def dDet(self,t):
        return -sin(t)*self.r**2
    
    def dDet_Tex(self):        
        return "-r^2\\sin{t}"
    
    
    def Phi(self,t):
        return -2.0
    
    def dPhi(self,t):
        return 0.0

    def Phi_Tex(self):        
        return "-2"
    
    def dPhi_Tex(self):        
        return "0"
    
    
    def Psi(self,t):
        return -0.5
    
    def dPsi(self,t):
        return 0.0

    def Psi_Tex(self):        
        return "-2"
    
    
    def Psi_Tex(self):        
        return "-\\frac{1}{2}"
    def dPsi_Tex(self):        
        return "0"
    
    def Kappa_Tex(self):
        return "-\\frac{1}{2\\sqrt{2}r} \\cdot \\frac{1}{\\sqrt{  1-\\cos{t}}  }"
    
    def Kappa(self,t):
        det=-1.0+cos(t)
        v2=2.0*(1.0-cos(t))
        
        kappa=0.0
        if (v2!=0.0):
            kappa=det/(v2**1.5)
            
        return kappa

    def Rho_Tex(self):
        return "-2\\sqrt{2}r \\sqrt{  1-\\cos{t}}"
    
    def Rho(self,t):
        det=-1.0+cos(t)
        v2=2.0*(1.0-cos(t))
        
        rho=0.0
        if (det!=0.0):
            rho=(v2**1.5)/det
            
        return rho
    def dRho(self,t):
        drho=None
        coss1t=1.0-cos(t)
        if (coss1!=0.0):
            drho=-2.0**1.5*self.r*sin(t)/sqrt(coss1t)
            
        return drho

    def dRho_Tex(self):
        return "-2\\sqrt{2} r \\frac{  \\sin{t}  }{   \\sqrt{  1-\\cos{t}}   }"
    
    def RhoV(self,t):
        rho=self.Phi(t)
        vn=self.VN(t)

        rhov=None
        if (rho!=None and vn!=None):
            rhov=vn*rho
            
        return rhov

    def Evolute(self,t):
        fact=1.0+self.Phi(t)
        lfact=fact
        
        return (    I(2)*t + J(2)*fact + Q(t)*lfact    )*self.r
    
    def dEvolute(self,t):
        phi=self.Phi(t)
        dphi=self.dPhi(t)

        dc=None
        if (phi!=None and dphi!=None):
            ij=I(2)+J(2)*dphi
            pq=dphi*Q(t)+(1.0+phi)*P(t)

            dc=(    ij+pq   )*self.r
            
        return dc
    
    def Evolute_Tex(self):
        latex=[
            "t"+self.Latex_Vector("i"),
            "-"+self.Latex_Vector("j"),
            "-"+self.Latex_Vector("q")+"(t)"
        ]
        return "r"+self.Latex_Left_Right(  "\n".join(latex),"("  )
    
    def Evolute_SPs_Tex(self):        
        return "".join([
            "\\left\\{",
            "   \\left(\\begin{array}{c}",
            "      (2 p+1) \\pi\\\\0",
            "   \\end{array}\\right),",
            "   ~p \\in \\mathbb{Z}",
            "\\right\\}"
        ])
        
    def dEvolute_Tex(self):
        latex=[
            self.Latex_Vector("i"),
            "-"+self.Latex_Vector("p")+"(t)"
        ]
        return "r"+self.Latex_Left_Right(  "\n".join(latex),"("  )
    
if (re.search('Cycloid.py$',sys.argv[0])):
    curve=Cycloid()
    curve.Run()
