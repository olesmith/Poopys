from math import *
import re,sys
sys.path.insert(0,'/root/python')


from R_n import *
from Curve import Curve

from Circle import Circle

class Hypocycloid(Curve):
    Name="Hypocycloid"

    #Fixed to 1
    r=1.0

    #Method R is occupied
    RR=3.0
    b=-2.0
    N=400
    
    #Nondimensional quantities
    Omega=2.0
    
    Latex_Figs=[
            [
                [
                    "Hypocycloid/Hypocycloid_Ana_1_000000-0_333333-400.pdf",
                    "Hypocycloid/Hypocycloid_Ana_1_000000-0_250000-400.pdf",
                    "Hypocycloid/Hypocycloid_Ana_1_000000-0_200000-400.pdf",
                ],
                [ "$\\omega=2$","$\\omega=3$","$\\omega=4$", ],
            ],
            [
                [
                    "Hypocycloid/Hypocycloid_Ana_1_000000-0_166667-400.pdf",
                    "Hypocycloid/Hypocycloid_Ana_1_000000-0_142857-400.pdf",
                    "Hypocycloid/Hypocycloid_Ana_1_000000-0_125000-400.pdf",
                ],
                [ "$\\omega=5$","$\\omega=6$","$\\omega=7$", ],
            ],
            [
                [
                    "Hypocycloid/Hypocycloid_Ana_1_000000-2_000000-400.pdf",
                    "Hypocycloid/Hypocycloid_Ana_1_000000-3_000000-400.pdf",
                    "Hypocycloid/Hypocycloid_Ana_1_000000-4_000000-400.pdf",
                ],
                [ "$\\omega=-\\frac{1}{2}$","$\\omega=-\\frac{2}{3}$","$\\omega=-\\frac{3}{4}$", ],
            ],
    ]
    def Curve_Parameters(self):
        return [
            #R, radius fixed circle
            [ 1.0,],
            #r, radius rolling circle
            [
                2.0,3.0,4.0,5.0,
                #1.0/2.0,
                1.0/3.0,1.0/4.0,1.0/5.0,
                1.0/6.0,1.0/7.0,1.0/8.0,
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
                ['$\\omega=2$',[1.0,1.0/3.0]],
                ['$\\omega=3$',[1.0,1.0/4.0]],
                ['$\\omega=4$',[1.0,1.0/5.0]],
                ['$\\omega=5$',[1.0,1.0/6.0]],
            ],
        ]
    
    ##!
    ##! Override curve draw to inlcude fixed circle
    ##!
    
    def Rs_SVG(self,tell=False):
        
        fixed=Circle()
        fixed.r=self.RR
        fixed.N=100
        fixed.__Calc__()
        #svg=fixed.Rs.Mesh_SVG_Draw_Curve('black')

        rolling=Circle()
        rolling.r=self.r
        rolling.c=Vector([self.RR+self.r,0])
        rolling.N=100
        rolling.__Calc__()
        #svg=svg+rolling.Rs.Mesh_SVG_Draw_Curve('black')

        
        self.Rs.Mesh_SVG(
            self.Curve_SVG_Name("d0R",""),
            self.Curve_Component_Get("R","Color","Ana"),
            tell,
            self.Show_Points,
            self.Show_Point_Size,
            self.Curve_Component_Get("R","Color","Ana"),
            True, #text
            self.Curve_Coordinate_System_Get(),
            [],[],
            self.Symmetries,
            fixed.Rs.Mesh_SVG_Draw_Curve('black',[],[],2) #thickness
            #+
            #rolling.Rs.Mesh_SVG_Draw_Curve('black',[],[],2)
        )
        
    def PMax(self):
        xmax=self.RR+self.r+abs(self.b)
        return Vector([xmax,xmax])*0.8
    
    def PMin(self):
        xmax=self.RR+self.r+abs(self.b)
        return Vector([-xmax,-xmax])*0.8
    
    
    def Curve_Init_Parameters(self):
        self.t2=max(2*pi,2.0*self.r/self.RR*pi)
        
        self.Omega=(self.RR-self.r)/self.r
        self.Omega_P=self.Omega+1.0
        self.Omega_M=self.Omega-1.0

        self.R_Factor=self.RR/( self.RR-2.0*self.r)
        self.R_Factor_Tex="\\frac{R}{R-2r}"

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
    
    def Parameters_Tex(self):
        return "\\omega=\\frac{R-r}{r}"
    
    def Parametrization_Tex(self):
        return self.Latex_Vector("r")+"(t)="+self.R_Tex()
    
    def Equation_Tex(self):
        return self.Latex_Vector("r")+"(t)="+self.Latex_vect([
            "(R-r)\\cos{t}+r \\cos{\\omega t}",
            "(R-r)\\sin{t}-r \\sin{\\omega t}"
        ])+",~R,r>0, ~ t \\in \\mathbb{R}"
    
    def Vectors_Tex(self):        
        return ",\\quad".join([
            "=".join([
                self.Latex_Vector("p")+"(\\omega t)",
                self.Latex_vect(["-\\cos{\\omega t}","\\sin{\\omega t}"]),
            ]),
            "=".join([
                self.Latex_Vector("q")+"(\\omega t)",
                self.Latex_vect(["-\\sin{\\omega t}","-\\cos{\\omega t}"]),
            ]),
        ])

    def dVectors_Tex(self):        
        return ";\\quad".join([
            ",\\quad".join( self.PQ_dVectors() ),
            ",\\quad".join( self.PQ_VectorsN() )
        ])

    def VectorsN_Tex(self):
        return "=".join([
            "=".join([
                "\\cdot".join([
                    self.Latex_Vector("e")+"( t)",
                    self.Latex_Vector("p")+"(\\omega t)",
                ]),
                "\\cdot".join([
                    self.Latex_Vector("f")+"( t)",
                    self.Latex_Vector("q")+"(\\omega t)",
                ]),
                "-\\cos{(\\omega+1)t}"
            ]),
        ])
    
    def R(self,t):
        tt=t*self.Omega
        return (    E(t)*self.Omega-P(tt)    )*self.r
    
    def R_Tex(self):        
        return "r"+self.Latex_Left_Right(
            " ".join([
                "\\omega"+self.Latex_Vector("e")+"(t)",
                "-",
                ""+self.Latex_Vector("p")+"(\\omega t)"
            ]),"(")
        
    def dR(self,t):
        tt=t*self.Omega
        return (    F(t)+Q(tt)   )*(self.r*self.Omega)
    
    def dR_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                self.Latex_Vector("f")+"(t)",
                "+",
                ""+self.Latex_Vector("q")+"(\\omega t)"
            ],
            "("
        )
        
        
    def d2R(self,t):
        return (    -E(t)+P(t,self.Omega)*(self.Omega)    )*(self.r*self.Omega)

    def d2R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                "-",
                self.Latex_Vector("e")+"(t)",
                "+",
                "\\omega"+self.Latex_Vector("p")+"(\\omega t)"
            ],
            "("
        )
        
    def d3R(self,t):
        return (    -F(t)-Q(t,self.Omega)*(self.Omega**2)    )*(self.r*self.Omega)
    
    def d3R_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                "-",
                self.Latex_Vector("f")+"(t)",
                "-",
                "\\omega^2"+self.Latex_Vector("q")+"(\\omega t)"
            ],
            "(",
        )
        
    def Cost(self,t):
        return cos( self.Omega_P*t )
    
    def Sint(self,t):
        return sin( self.Omega_P*t )
    

    def v2_Canonical_Tex(self):        
        return "2(1+ \cos{ (\omega+1)t})"
    
    
    def v2(self,t):
        cost=self.Cost(t)
        return 2.0*(1.0-cost)*(self.r*self.Omega)**2
    def v2_Tex(self):        
        return "2r^2\\omega^2"+self.Latex_Left_Right(  "1-\\cos{ (\\omega+1)t}","("  )
    
    def dv2(self,t):
        sint=self.Sint(t)
        return 2.0*(self.r*self.Omega)**2*(1+self.Omega)*sint
    
    def dv2_Tex(self):        
        return "2r^2\\omega^2(\\omega+1)\\sin{ (\\omega+1)t}"
    
    def VN(self,t):
        tt=t*self.Omega
        return (    -E(t)-P(tt)   )*(self.r*self.Omega)

    def VN_Tex(self):        
        return "r\\omega"+self.Latex_Left_Right(
            [
                "-",
                self.Latex_Vector("e")+"(t)",
                "-",
                ""+self.Latex_Vector("p")+"(\\omega t)"
            ],
            "("
        )
    
    def Det_Canonical_Tex(self):        
        return "1- \\omega   + (\\omega-1) \\cos{ (\\omega+1)t}"

    def Det(self,t):
        cost=self.Cost(t)

        return (   1.0-self.Omega )*(1.0-cost)*(self.r*self.Omega)**2
    
    def Det_Tex(self):
        return "r^2\\omega^2(1- \\omega)"+self.Latex_Left_Right(  "1-\cos{(\\omega+1)t}","("  )
    
    def dDet(self,t):
        sint=self.Sint(t)

        return (self.r*self.Omega**2)*(1.0-self.Omega**2) *sint
    
    def dDet_Tex(self):
        return "r^2\\omega^2(1- \\omega^2)\\sin{(\\omega+1)t}"
    
    def t(self,t):
        return self.dR(t).Normalize()

    def t_Tex(self):
        vect=self.Latex_Vector("f")+"(t)+"+self.Latex_Vector("q")+"(\\omega t)"
        return "\\frac{1}{\\sqrt{2}}\\cdot \\frac{"+vect+"}{   \\sqrt{1- \\cos{ (\\omega+1)t}}   }"

    def n(self,t):
        return self.dR(t).Hat2().Normalize()

    def n_Tex(self):
        vect=self.Latex_Vector("e")+"(t)+"+self.Latex_Vector("p")+"(\\omega t)"
        return "-\\frac{1}{\\sqrt{2}}\\cdot \\frac{"+vect+"}{   \\sqrt{1- \\cos{ (\\omega+1)t}}   }"

    
    def Phi(self,t):
        phi=-2.0*self.r/(self.RR-2.0*self.r)
        
        return phi
    
    def Psi(self,t):
        psi=-0.5*(self.RR-2.0*self.r)/self.r
        
        return psi

    def Phi_Tex(self):
        return "\\frac{2}{1-\omega}=\\frac{2r}{2r-R}"
    
    def Psi_Tex(self):
        return "\\frac{1-\omega}{2}=\\frac{2r-R}{2r}"
    
    def Kappa(self,t):
        cost=self.Cost(t)
        kappa=None
        if (cost!=1.0):
            kappa=(1.0-self.Omega)/(2**1.5)
            kappa/=(self.r*abs(self.Omega))
            kappa/=sqrt(1-cost)

        return kappa

    def Kappa_Tex(self):
        latex="\\sqrt{1-\\cos{ (\\omega+1)t}}"
        
        return "\\frac{1}{2\\sqrt{2}}\\cdot \\frac{1-\\omega}{ r|\\omega|}\\cdot \\frac{1}{"+latex+"}"
    
    def Rho(self,t):
        cost=self.Cost(t)
                
        det=self.Det(t)
        
        rho=2.0*sqrt(2.0)*self.r*abs(self.Omega)/(1.0-self.Omega)* sqrt( 1.0-cost)
        
        return rho
    
    def dRho(self,t):
        cost=self.Cost(t)
        
        drho=None
        if (cost!=1.0):
            drho=sqrt(2.0)*(1.0+self.Omega)/(1.0-self.Omega)*abs(self.Omega)
            drho*=self.Sint(t)
            drho/=sqrt(1-cost)
            
        return drho

    def Rho_Tex(self):
        latex="\\sqrt{1-\\cos{ (\\omega+1)t}}"
        return "2\\sqrt{2} \\cdot \\frac{ r |\\omega|}{1-\\omega} \\cdot"+latex
    
    def dRho_Tex(self):
        counter="\\sin{ (\\omega+1)t}"
        denominator="\\sqrt{1-\\cos{ (\\omega+1)t}}"
        return "\\sqrt{2} r |\\omega| \\cdot \\frac{ 1+\\omega}{1-\\omega} \\cdot"+"\\frac{"+counter+"}{"+denominator+"}"
    
    def RhoV(self,t):
        phi=self.Phi(t)
        rhov=None
        if (phi!=None):
            r=-E(t)-E( self.Omega*t )

            rhov=r*self.Phi(t)*self.r
        return rhov
    
    def RhoV_Tex00(self):
        return "-r"+self.Latex_Vector("e")+"(t)"
            
    def Evolute(self,t):
        phi=self.Phi(t)
        fact1=(self.RR-self.r)*self.R_Factor
        fact2=self.r*self.R_Factor

        return (    E(t)*fact1+P( self.Omega*t )*fact2    )
    
    def Evolute_Tex(self):
        latex=[
            "(R-r)"+self.Latex_Vector("e")+"(t)",
            "-",
            "r"+self.Latex_Vector("p")+"(\\omega t+\pi)",
        ]
        return self.R_Factor_Tex+self.Latex_Left_Right(  "\n".join(latex),"("  )

    def dEvolute(self,t):
        fact=(1.0+self.Omega)/(1.0-self.Omega)*abs(self.Omega)

        return (    E(t)+P( self.Omega*t )    )*fact
    def dEvolute_Tex(self):
        fact="\\frac{1+\\omega}{1-\\omega}|\\omega|"

        vect="\\Vector{e}(t)+\\Vector{p}(\\omega t)"

        return fact+self.Latex_Left_Right(  vect,"("  )
    
if (re.search('Hypocycloid.py$',sys.argv[0])):
    curve=Hypocycloid({
    })

    curve.Run()
