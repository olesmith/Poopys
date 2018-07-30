from math import *
from Vector import Vector
from Mesh   import Mesh

class Curve_v2():
    ##!
    ##! Calculate Numerical and, if defined, Analytical velocities.
    ##! Store in self.dRs_Num and self.dRs_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def v2(self,t)
    ##!

    v2s_Num=None
    v2s_Ana=None

    dv2s=[]
    dv2=0.0
    
    def v(self,t):
        return sqrt(  self.v2(t)  )
    
    def dv(self,t):
        return (self.v(t+self.eps)-self.v(t-self.eps))/self.eps2
    
    def Calc_Num_v2(self,t):
        dr=self.Calc_Num_dR(t)
        
        v2=None
        if (dr):
            v2=dr.Square_Length()
            

        return v2
    
    def Calc_Num_v(self,t):
        v2=self.Calc_Num_v2(t)
        
        v=None
        if (v2):
            v=sqrt(v2)
            
        return v
    
    def Calc_Num_v2s(self):
        self.v2s_Num=Mesh(self.N,"v2","Num")
        for n in range( self.N ):
            self.v2s_Num[n]=None
            v2=self.Calc_Num_v2( self.ts[n] )
            if (v2.__class__.__name__=="float"):
                self.v2s_Num[n]=Vector([  self.ts[n],v2  ])

    def Calc_Ana_v2s(self):
        self.v2s_Ana=self.Calc_Ana_Function("v2")
            
            
    ##!
    ##! Verify squared velocities.
    ##!
    
    def Verify_v2s(self):
        dv2,self.dv2s,v2_Max=self.Verify_Mesh_Type("v2")

        
        return [
            "Squared Velocity:\t",
            "%.2e\t" % dv2,
            "%.2e" % sqrt(dv2)
        ]
            
    ##!
    ##! Draw squared velocities as SVG (function).
    ##!
    
    def v2s_SVG(self):
        self.Mesh_Function_SVGs("v2")


