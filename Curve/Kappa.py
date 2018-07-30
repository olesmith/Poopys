from Vector import Vector
from Mesh   import Mesh

class Curve_Kappa():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature.
    ##! Store in self.Kappa_Num and self.Kappa_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Kappa(self,t)
    ##!

    Kappas_Num=None
    Kappas_Ana=None

    dKappas=[]
    dKappa_=0.0

    def Calc_Num_Kappa(self,t):
        v2=self.Calc_Num_v2(t)
        
        kappa=None
        if (v2.__class__.__name__=="float" and v2!=0.0):
            det=self.Calc_Num_Det(t)
            if (det.__class__.__name__=="float"):
                kappa=self.Calc_Num_Det(t)/(v2**1.5)

        return kappa
    
    def Calc_Num_Kappas(self):
        self.Kappas_Num=Mesh(self.N,"Kappa","Num")
        for n in range( self.N ):
            kappa=self.Calc_Num_Kappa( self.ts[n] )
            v=None
            if (kappa):
                v=Vector([self.ts[n],kappa])
            self.Kappas_Num[n]=v
            
    def Calc_Ana_Kappas(self):
        self.Kappas_Ana=Mesh(self.N,"Kappa","Ana")
        for n in range( self.N ):
            kappa=self.Kappa( self.ts[n] )
            v=None
            if (kappa):
                v=Vector([self.ts[n],kappa])
                
            self.Kappas_Ana[n]=v
                       
    ##!
    ##! Calculate curvatures.
    ##!
    
    def Verify_Kappas(self):        
        dkappa_,self.dKappas,dkappa_Max=self.Verify_Mesh_Type("Kappa")
        
        return [
            "Curvature:\t\t",
            "%.2e\t" % dkappa_,
            str(dkappa_Max)
        ]
            
        return [
            "Curvature:\t\t",
            "%.6f" % dkappa
        ]



    
    ##!
    ##! Draw curvatures as SVG (function).
    ##!
    
    def Kappas_SVG(self):
        self.Mesh_Function_SVGs("Kappa")

