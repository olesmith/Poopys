from math import *
from Vector import Vector
from Mesh   import Mesh

class Curve_dv2():
    ##!
    ##! Calculate Numerical and, if defined, Analytical velocities.
    ##! Store in self.dRs_Num and self.dRs_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def v2(self,t)
    ##!

    dv2s_Num=None
    dv2s_Ana=None

    ddv2s=[]
    ddv2=0.0
        
    def Calc_Num_dv2(self,t):
        v2_plus =self.Calc_Num_v2(t+self.eps)
        v2_minus=self.Calc_Num_v2(t-self.eps)

        
        dv2=None
        if (v2_plus and v2_minus):
            dv2=(v2_plus-v2_minus)/self.eps2
            
        return dv2
    
    def Calc_Num_dv2s(self):
        self.dv2s_Num=Mesh(self.N,"dv2","Num")
        for n in range( self.N ):
            self.dv2s_Num[n]=None
            dv2=self.Calc_Num_dv2( self.ts[n] )
            if (dv2.__class__.__name__=="float"):
                self.dv2s_Num[n]=Vector([  self.ts[n],dv2  ])
            
    def Calc_Ana_dv2s(self):
        self.dv2s_Ana=self.Calc_Ana_Function("dv2")
            
            
    ##!
    ##! Verify squared velocities.
    ##!
    
    def Verify_dv2s(self):
        ddv2,self.ddv2s,ddv2_Max=self.Verify_Mesh_Type("dv2")

        return [
            "Sq Vel. Derivative:\t",
            "%.2e" % ddv2,
            "%.2e" % ddv2_Max[1],
        ]
            
    ##!
    ##! Draw squared velocities as SVG (function).
    ##!
    
    def dv2s_SVG(self):
        self.Mesh_Function_SVGs("dv2")


