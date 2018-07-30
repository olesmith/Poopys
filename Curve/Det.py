from Vector import Vector
from Mesh   import Mesh

class Curve_Det():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curve determinant.
    ##! Store in self.Det_Num and self.Det_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Det(self,t)
    ##!

    Dets_Num=None
    Dets_Ana=None

    dDets=[]
    dDet=0.0
    
    
    def Calc_Num_Det(self,t):
        vn=self.Calc_Num_VN(t)
        d2r=self.Calc_Num_d2R(t)
        det=None
        if (vn and d2r):
            det=vn*d2r
        return det
    
    def Calc_Num_Dets(self):
        self.Dets_Num=Mesh(self.N,"Det","Num")
        for n in range( self.N ):
            self.Dets_Num[n]=None
            det=self.Calc_Num_Det( self.ts[n] )
            if (det.__class__.__name__=="float"):
                self.Dets_Num[n]=Vector([ self.ts[n],det  ])
            
    def Calc_Ana_Dets(self):
        self.Dets_Ana=Mesh(self.N,"Det","Ana")
        for n in range( self.N ):
            self.Dets_Ana[n]=None
            det=self.Det( self.ts[n] )
            if (det!=None):
                self.Dets_Ana[n]=Vector([ self.ts[n],det ])
            
    ##!
    ##! Verify curve determinants.
    ##!
    
    def Verify_Dets(self):
        ddet,self.dDets,ddet_Max=self.Verify_Mesh_Type("Det")
        
        return [
            "Curve Determinant:\t",
            "%.2e" % ddet,
            str(ddet_Max[1]),
        ]

    ##!
    ##! Draw curve determinants as SVG (function).
    ##!
    
    def Dets_SVG(self):
        self.Mesh_Function_SVGs("Det")

