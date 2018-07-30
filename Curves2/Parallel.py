from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve
from Parabola import Parabola
from Trochoid import Trochoid

class Parallel(Curve):
    __Base__=None
    Name="Parallel"

    #Parabola
    a=1.0
    d=1.0
    
    xmax=4.25
    ymax=4.25

    xmax=2.0
    ymax=4.0

    t1=-3.0
    t2=3.0
    
    N=100
    

    #Trochoid
    #r=1.0
    #b=1.0
    #Lambda=3.0
    
    #t1=0.0
    #t2=4.0*pi
    
    #N=400
    
    #xmax=5.0*pi
    #ymax=2.5
    #xmin=-1.0*pi
    #ymin=-2.0

    
    Show_Point_Nos=[]
    def Base_Curve(self):
        return self.Base_Curve_Parabola()
    
    def Base_Curve_Parabola(self):
        if (self.__Base__==None):
            args={
                "t1": self.t1,
                "t2": self.t2,
                "N":  self.N,
                "a": self.a,
            }
            
            self.__Base__=Parabola(args)
            self.__Base__.__Calc__()

        return self.__Base__
    
    def Base_Curve_Trochoid(self):
        if (self.__Base__==None):
            args={
                "t1": self.t1,
                "t2": self.t2,
                "N":  self.N,
                "r": self.r,
                "b": self.b,
            }
            
            self.__Base__=Trochoid(args)
            self.__Base__.__Calc__()

        return self.__Base__

    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        return 1.5
    
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([-self.xmax,-0.25*self.ymax])
        
    def Curve_Parameters(self):
        return [
            [
                1.0,
            ],
            [
                -1.75,-1.5,-1.25,
                -1.0,-0.75,-0.5,-0.25,
                0.0,0.25,0.5,0.75,
                1.0,1.25,1.5,1.75,
                2.0,2.25,2.5,2.75,
            ],
        ]
    
    def Curve_SVG_Accumulated_Init(self):
        self.Base_Curve().Evolutes_Ana.__Canvas__=self.Base_Curve().Rs.__Canvas__
        return self.Base_Curve().Evolutes_Ana.Mesh_SVG_Draw_Curve(
            'orange',
            [],
            [],
            4,
            "",
            False,
            False
        )+self.Base_Curve().Rs.Mesh_SVG_Draw_Curve(
            'blue',
            [],
            [],
            4,
            "",
            False,
            False
        )
        
    
        
    def Curve_Init_Parameters(self):
        return
    
    def Curve_Parameter_Values(self):
        return [
            "%.6f" % self.a,
            "%.6f" % self.d,
            "%d"   % self.N,
        ]
    
    def Curve_Parameter_Keys(self):
        return [ "a","d"]
    
    def Curve_Parameter_Names(self):
        return [ "a","d","n"]


    def R(self,t):
        n=self.Base_Curve().n(t)

        r=None
        if (n!=None):
            r=self.Base_Curve().R(t)+self.d*n

        return r

    def R_Tex(self):        
        return "".join([
            self.Latex_Vector("r"),
            "+d",
            self.Latex_Vector("n"),
            #"=",
            #self.Latex_vect([ "t","\\frac{1}{2} at^2"]),
            #"+\\frac{d}{\\sqrt{1+a^2t^2}}",
            #self.Latex_vect([ "-at","1"]),
        ])
    

    def dR(self,t):
        tv=self.Base_Curve().t(t)
        psi=self.Base_Curve().Psi(t)
        v=self.Base_Curve().v(t)
        
        r=None
        if (tv!=None and v!=None and psi!=None):
            r=tv*(v-self.d*psi)

        return r
    
    def dR_Tex(self):        
        return "".join([
            "(v-r \\psi)~"+self.Latex_Vector("t")
        ])
    
    def v2(self,t):
        psi=self.Base_Curve().Psi(t)
        v=self.Base_Curve().v(t)

        v2=None
        if (v!=None and psi!=None):
            v2=(v-self.d*psi)**2
        return v2

 
    def v2_Tex(self):        
        return "".join([
            "(v-r \\psi)^2"
        ])
    
    def d2R(self,t):
        tt=self.Base_Curve().t(t)
        nn=self.Base_Curve().n(t)
        v=self.Base_Curve().v(t)
        dv=self.Base_Curve().dv(t)
            
        psi=self.Base_Curve().Psi(t)
        dpsi=self.Base_Curve().dPsi(t)
            

        r=None
        if (tt!=None and psi!=None):
            t_fact=dv-self.d*dpsi
            n_fact=psi*(v-self.d*psi)
                               
            r=tt*t_fact+nn*n_fact

        return r
    
    def d2R_Tex(self):        
        return "".join([
            "(v'-r \\psi')~",
            self.Latex_Vector("t"),
            "+",
            "\\psi(v-r \\psi)~",
            self.Latex_Vector("n")
        ])
       
    def VN(self,t):
        n=self.Base_Curve().n(t)
        v=self.Base_Curve().v(t)
        psi=self.Base_Curve().Psi(t)

        r=None
        if (n!=None and v!=None and psi!=None):
            r=n*(v-self.d*psi)

        return r
    
    def VN_Tex(self):        
        return "".join([
            "(v-r \\psi)~"+self.Latex_Vector("n")
        ])
    
    def Det(self,t):
        v=self.Base_Curve().v(t)
        psi=self.Base_Curve().Psi(t)

        det=None
        if (v!=None and psi!=None):
            det=psi*(   (v-self.d*psi)**2   )
            
        return det
    
    def Det_Tex(self):        
        return "".join([
            "\\psi( v-r\\psi )^2"
        ])

    
    def Phi(self,t):
        return self.Base_Curve().Phi(t)
    
    def Phi_Tex(self):        
        return "".join([
            "\\phi"
        ])
    
    def Evolute(self,t):
        return self.Base_Curve().Evolute(t)
    def dEvolute(self,t):
        return self.Base_Curve().dEvolute(t)

    ##!
    ##! Draw curve as SVG polyline.
    ##!
    
    def Rs_SVG(self):
        svg=[]
        svg=svg+self.Rs.Mesh_SVG_CoordSys("black",True,3)

        self.Base_Curve().Rs.__Canvas__=self.Rs.__Canvas__
        
        color=self.Curve_Component_Get("R","Color","Num")
        for curve in [  self.Base_Curve(),self  ]:
            svg=svg+curve.Rs.Mesh_SVG_Draw_Curve(
                color,
                self.Symmetries,
                self.Show_Points,
                self.Show_Point_Size,
                self.Curve_Component_Get("R","Color","Points"),
                False,False
            )

            color='red'

        res=self.SVG_Doc_Write(self.__Canvas__,svg,self.Curve_SVG_Name("d0R"))
        return svg

    

if (re.search('Parallel.py$',sys.argv[0])):
    curve=Parallel()
    curve.Base_Curve()
    curve.Run()
