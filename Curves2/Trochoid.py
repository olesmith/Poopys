from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve

class Trochoid(Curve):
    Name="Trochoid"
    Cycloid_Draw=False

    Resolution=[600,1200]

    r=1.0
    b=1.0
    Lambda=3.0
    
    t1=0.0
    t2=4.0*pi
    
    N=400
    
    xmax=4.2*pi
    ymax=2.5
    xmin=-0.2*pi
    ymin=-2.0

    
    rolling_t=5.0/3.0*pi
    rolling_ts=[
        2.0/3.0*pi,
        5.0/3.0*pi,
    ]

    Parameters=[
        [ 1.0,],
        [
            1.0,1.25,1.5,
            1.0/1.25,1.0/1.5,
        ]
    ]
    
    Cycloid=None
    PDFs000=[
        [
            "Evolute","Ana",
            [
                [1.0,1.5],
                [1.0,1.0],
                [1.0,1.0/1.5],
            ],
            "Trochoid_Evolute_Ana.tex",
            1  #b, second parameter, in title
        ],
    ]

    Latex_Figs=[
            [
                [ "Trochoid/Trochoid_Ana_1_000000-0_666667-400.pdf", ],
                [ "", ],
            ],
            [
                [ "Trochoid/Trochoid_Functions_Num_1_000000-0_666667-400.pdf", ],
                [ "Trochoids, $b=2/3a$", ],
            ],
            [
                [ "Trochoid/Trochoid_Ana_1_000000-1_000000-400.pdf", ],
                [ "", ],
            ],
            [
                [ "Trochoid/Trochoid_Functions_Num_1_000000-1_000000-400.pdf", ],
                [ "Trochoids, $b=a$", ],
            ],
            [
                [ "Trochoid/Trochoid_Ana_1_000000-1_500000-400.pdf", ],
                [ "", ],
            ],
            [
                [ "Trochoid/Trochoid_Functions_Num_1_000000-1_500000-400.pdf", ],
                [ "Trochoids, $b=3/2a$", ],
            ],
    ]

     
    ##!
    ##! Override Curve_Functions_Canvas_MaxMin
    ##!

    def Curve_Functions_Canvas_MaxMin(self):
        return Vector([self.t1,-5.0]),Vector([self.t2,5.0])
    
    ##!
    ##! Override Cycloid_Calc:
    ##!
    ##! Calculate the Cycloid
    ##!

    def Cycloid_Calc(self):
        if (self.b!=self.r):
            if (self.Cycloid==None):
                self.Cycloid=Trochoid()
                self.Cycloid.Name="Cycloid"
                self.Cycloid.N=self.N
                self.Cycloid.r=self.r
                self.Cycloid.b=self.r
                self.Cycloid.Lambda=1.0
                self.Cycloid.rolling_t=self.rolling_t
                self.Cycloid.Curve_Thickness=1
                
                self.Cycloid.__Calc__()
                self.Cycloid.__Canvas__=self.__Canvas__
        

    ##!
    ##! Override Trochoid_Rolling_Center(t):
    ##!
    ##! Calculate Rolling Center
    ##!

    def Rolling_Center(self,t):
        rolling_center=I()*self.rolling_t+J()

        print "Rolling Center",rolling_center*self.r
        return rolling_center*self.r
        
    ##!
    ##! Override Trochoid_SVG:
    ##!
    ##! Calculate the Cycloid
    ##!

    def Trochoid_SVG(self,type):
        return
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
                self.Curve_Point_Size
            )
            svg=svg+self.Point_Draw(
                self.Evolute(t),
                self.Curve_Component_Get("Evolute","Color","Points"),
                self.Curve_Point_Size
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
        self.Lambda=self.b/self.r
        
    def Curve_Parameters(self):
        return self.Parameters
    
        
    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        pmin=self.PMin()
        pmax=self.PMax()
        
        return [
            [ 0.0, pmin[1]],
            [ 0.0, pmax[1]],
            [ pmin[0], 0.0],
            [ pmax[0], 0.0],
        ]    
    

    def Curve_Parameter_Keys(self):
        return [ "r","b" ]
    
    def Curve_Parameter_Names(self):
        return [ "r","b" ]
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.r,
            "%.6f" % self.b,
            "%d"  % self.N,
        ]
    

    def Parametrization_Tex(self):        
        return self.Latex_vect([ "rt-b\\sin{t}","r-b\\cos{t}" ])
        
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


    def R(self,t):
        return (    I(2)*t + J(2) + Q(t)*self.Lambda    )*self.r
    
    def R_Tex(self):        
        return "r\\left(   "+" ".join([
            "t"+self.Latex_Vector("i"),
            "+",
            self.Latex_Vector("j"),
            "+",
            "\\lambda"+self.Latex_Vector("q")+"(t)"
        ])+"   \\right)"
        
    def dR(self,t):
        return (  I(2)+P(t)*self.Lambda  )*self.r
    
    def dR_Tex(self):        
        return "r\\left(   "+" ".join([
            self.Latex_Vector("i"),
            "+",
            "\\lambda"+self.Latex_Vector("p")+"(t)"
        ])+"   \\right)"
        
    def d2R(self,t):
        return Q(t)*(   -self.Lambda*self.r   )

    def d2R_Tex(self):        
        return " ".join([
            "-r\\lambda"+self.Latex_Vector("q")+"(t)"
        ])
            
    def d3R(self,t):
        return P(t)*(   -self.Lambda*self.r   )

    def d3R_Tex(self):        
        return " ".join([
            "-r\\lambda"+self.Latex_Vector("p")+"(t)"
        ])
        
    def v2(self,t):
        return 1.0+self.Lambda**2-2*self.Lambda*cos(t)

    def v2_Tex(self):        
        return "r^2\\left(  1+\\lambda^2-2 \lambda \cos{t}  \\right)"
    
    def t(self,t):
        return self.dR(t).Normalize()

    def t_Tex(self):        
        return "\\frac{"+" ".join([
            self.Latex_Vector("i"),
            "+",
            "\\lambda"+self.Latex_Vector("p")+"(t)"
        ])+"}{\\sqrt{  1+\\lambda^2-2 \lambda \cos{t}  }}"
        
    def n_Tex(self):        
        return "\\frac{"+" ".join([
            self.Latex_Vector("j"),
            "+",
            "\\lambda"+self.Latex_Vector("q")+"(t)"
        ])+"}{\\sqrt{  1+\\lambda^2-2 \lambda \cos{t}  }}"
        
    def n(self,t):
        T=self.t(t)
        if (T!=None):
            return self.t(t).Hat2()

        return None

    def VN(self,t):
        return (  J(2)+Q(t)*self.Lambda  )*self.r

    def VN_Tex(self):        
        return "r\left(  "+" ".join([
            self.Latex_Vector("j"),
            "+",
            "\\lambda"+self.Latex_Vector("q")+"(t)"
        ])+"   \\right)"
    
    def Det(self,t):
        return (-self.Lambda**2+self.Lambda*cos(t))*self.r
    
    def Det_Tex(self):        
        return "r^2\\lambda\\left(   \cos{t}-\\lambda  \\right)"
    
    
    def Phi(self,t):
        det=-self.Lambda**2+self.Lambda*cos(t)
        v2=1+self.Lambda**2-2*self.Lambda*cos(t)
        
        phi=0.0
        if (det!=0.0):
            phi=v2/det
            
        return phi
    
    def dPhi(self,t):
        llambda=(self.Lambda**2-1.0)/self.Lambda
        coss=cos(t)-self.Lambda
        
        dphi=None
        if (  coss!=0.0  ):
            dphi=llambda*sin(t)/( (cos(t)-self.Lambda)**2 )
        
        return dphi

    def Phi_Tex(self):        
        return "\\frac{   1+\\lambda^2-2 \lambda \cos{t}    }{   \\lambda\\left(    \cos{t}-\\lambda  \\right)}"
    
    def Psi_Tex(self):        
        return "\\frac{   \\lambda\\left(    \cos{t}-\\lambda  \\right)}{   1+\\lambda^2-2 \lambda \cos{t}    }"
    
    def Kappa_Tex(self):        
        return "\\frac{1}{r} \\cdot \\frac{   \\lambda\\left(    \cos{t}-\\lambda  \\right)}{   (1+\\lambda^2-2 \lambda \cos{t})^{3/2}    }"
    
    def Rho_Tex(self):        
        return "r\\frac{   (1+\\lambda^2-2 \lambda \cos{t})^{3/2}    }{   \\lambda\\left(    \cos{t}-\\lambda  \\right)}"
    
    def Kappa(self,t):
        det=-self.Lambda**2+self.Lambda*cos(t)
        v2=1+self.Lambda**2-2*self.Lambda*cos(t)
        
        kappa=0.0
        if (v2!=0.0):
            kappa=det/(v2**1.5)
            
        return kappa

    def Rho(self,t):
        det=-self.Lambda**2+self.Lambda*cos(t)
        v2=1+self.Lambda**2-2*self.Lambda*cos(t)
        
        rho=0.0
        if (det!=0.0):
            rho=(v2**1.5)/det
            
        return rho

    def dRho(self,t):
        det=-self.Lambda**2+self.Lambda*cos(t)
        v2=1+self.Lambda**2-2*self.Lambda*cos(t)
        
        rho=0.0
        if (det!=0.0):
            rho=(v2**1.5)/det
            
        return rho

    def RhoV(self,t):
        rho=self.Phi(t)
        vn=self.VN(t)

        rhov=None
        if (rho!=None and vn!=None):
            rhov=vn*rho
            
        return rhov

    def Evolute(self,t):
        fact=1.0+self.Phi(t)
        lfact=fact*self.Lambda
        
        return (    I(2)*t + J(2)*fact + Q(t)*lfact    )*self.r
    
    def dEvolute(self,t):
        phi=self.Phi(t)
        dphi=self.dPhi(t)

        dc=None
        if (phi!=None and dphi!=None):
            ij=I(2)+J(2)*dphi
            pq=dphi*Q(t)+(1.0+phi)*P(t)

            dc=(    ij+pq*self.Lambda   )*self.r
            
        return dc
    
    def Evolute_Tex(self):
        latex=[
            "t"+self.Latex_Vector("i"),
            self.Latex_Left_Right(
                "1+\\varphi(t)",
                "["
            )+self.Latex_Vector("j"),
            "\\lambda"+self.Latex_Left_Right(
                "1+\\varphi(t)",
                "["
            )+self.Latex_Vector("q")+"(t)"
        ]
        return "r"+self.Latex_Left_Right(  "\n+".join(latex),"("  )
    
    def dEvolute_Tex(self):
        latex=[
            self.Latex_Vector("i"),
            "\\varphi'(t)"+self.Latex_Vector("j"),
            "\\lambda \\varphi'(t)"+self.Latex_Vector("q")+"(t)"
            +
            "+\\lambda"+self.Latex_Left_Right(
                "1+\\varphi(t)",
                "["
            )+self.Latex_Vector("p")+"(t)"
        ]
        return "r"+self.Latex_Left_Right(  "\n+".join(latex),"("  )
    
if (re.search('Trochoid.py$',sys.argv[0])):
    curve=Trochoid({
    })

    curve.Run()
