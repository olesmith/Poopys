from Vector import Vector
from Mesh   import Mesh

class Curve_dDet():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curve determinant.
    ##! Store in self.Det_Num and self.Det_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Det(self,t)
    ##!

    dDets_Num=None
    dDets_Ana=None

    ddDets=[]
    ddDet=0.0
    
    
    def Calc_Num_dDet(self,t):
        detm=self.Calc_Num_Det(t-self.eps)
        detp=self.Calc_Num_Det(t+self.eps)

        ddet=None
        if (detm!=None and detp!=None):
            ddet=(detp-detm)/self.eps2

        return ddet
    
    def Calc_Num_dDets(self):
        self.dDets_Num=Mesh(self.N,"dDet","Num")
        for n in range( self.N ):
            self.dDets_Num[n]=None
            ddet=self.Calc_Num_dDet( self.ts[n] )
            if (ddet.__class__.__name__=="float"):
                self.dDets_Num[n]=Vector([ self.ts[n],ddet  ])
            
    def Calc_Ana_dDets(self):
        self.dDets_Ana=self.Calc_Ana_Function("dDet")
        
    ##!
    ##! Verify curve determinants.
    ##!
    
    def Verify_dDets(self):
        dddet,self.ddDets,dddet_Max=self.Verify_Mesh_Type("dDet")

        return [
            "Det. Derivative:\t",
            "%.2e" % dddet,
            str(dddet_Max[1]),
        ]

    ##!
    ##! Draw curve determinants as SVG (function).
    ##!
    
    def dDets_SVG(self):
        self.Mesh_Function_SVGs("dDet")

