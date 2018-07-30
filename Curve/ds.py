from math import *
from Vector import Vector
from Mesh   import Mesh

class Curve_ds():
    ##!
    ##! Calculate Numerical and, if defined, Analytical velocities.
    ##! Store in self.dRs_Num and self.dRs_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def v2(self,t)
    ##!

    ds_Num=None
    ds_Ana=None

    dss=[]
    ds=0.0
    
    def ds_Tex_Name(self):
        return "s(t)"
    
    def Calc_Num_ds(self,t):
        dr=self.Calc_Num_dR(t)
        
        v2=None
        if (dr):
            v2=dr.Square_Length()
            

        return v2
    
    def Calc_Num_v2s(self):
        self.v2s_Num=Mesh(self.N,"v2","Num")
        for n in range( self.N ):
            self.v2s_Num[n]=None
            v2=self.Calc_Num_v2( self.ts[n] )
            if (v2.__class__.__name__=="float"):
                self.v2s_Num[n]=Vector([  self.ts[n],v2  ])
            
    def Calc_Ana_v2s(self):
        self.v2s_Ana=Mesh(self.N,"v2","Ana")
        for n in range( self.N ):
            self.v2s_Ana[n]=None
            v2=self.v2( self.ts[n] )
            if (v2.__class__.__name__=="float"):
                self.v2s_Ana[n]=Vector([  self.ts[n],v2  ])
            
            
    ##!
    ##! Verify squared velocities.
    ##!
    
    def Verify_v2s(self):
        self.dv2=0.0
        for n in range( self.N ):
            dv2=abs(self.v2s_Num[n][1]-self.v2s_Ana[n][1])
            self.dv2s.append( dv2 )
            self.dv2+=dv2
            
        dv2="%.6f" % self.dv2
        sdv2="%.6f" % sqrt(self.dv2)
        
        return [  "Squared Velocity:",dv2,sdv2  ]
            
    ##!
    ##! Draw squared velocities as SVG (function).
    ##!
    
    def v2s_SVG(self):
        self.Mesh_Function_SVGs("v2")


