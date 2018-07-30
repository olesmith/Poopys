from math import *
from Vector import Vector
from Mesh   import Mesh

class Curve_S():
    ##!
    ##! Calculate Numerical and, if defined, arc lengths.
    ##! Store in self.Ss_Num and self.Ss_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def S(self,t)
    ##!

    Ss_Num=None
    Ss_Ana=None

    dSs=[]
    dS=0.0
    
    def Calc_Num_dS(self,ts,n):
        if (n==0): return 0.0
                
        dr1=self.Calc_Num_v(self.ts[n-1])
        dr2=self.Calc_Num_v(self.ts[n])
        
        ds=None
        if (dr1 and dr2):
            ds=0.5*(dr2+dr1)*(self.ts[n]-self.ts[n-1])
            
        return ds
    
    def Calc_Num_Ss(self,):
        self.Ss_Num=Mesh(self.N,"S","Num")

        s=0.0
        for n in range(self.N ):
            self.Ss_Num[n]=None
            ds=self.Calc_Num_dS(self.ts,n)
            #print n,self.ts[n],ds,s
            if (ds.__class__.__name__=="float"):
                s+=ds
                self.Ss_Num[n]=Vector([ self.ts[n],s  ])
            
 
    def Calc_Ana_Ss(self):
        self.S1=self.S( self.t1 )
        self.Ss_Ana=Mesh(self.N,"S","Ana")
        for n in range( self.N ):
            self.Ss_Ana[n]=None
            s=self.S( self.ts[n] )-self.S1
            if (s.__class__.__name__=="float"):
                self.Ss_Ana[n]=Vector([  self.ts[n],s ])
            
    ##!
    ##! Verify arc length.
    ##!
    
    def Verify_Ss(self):
        ds,self.dSs,ds_Max=self.Verify_Mesh_Type("S")
            
        return [  "Arc Length:\t\t","%.2e" % ds  ]
            
    ##!
    ##! Draw arc length as SVG (function).
    ##!
    
    def Ss_SVG(self):
        self.Mesh_Function_SVGs("S")
