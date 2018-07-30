from Vector import Vector
from Mesh   import Mesh

class Curve_T():
    ##!
    ##! Calculate Numerical and, if defined, Analytical unit tangent vector.
    ##! Store in self.Ts_Num and self.Ts_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def T(self,t)
    ##!

    Ts_Num=None
    Ts_Ana=None

    dTs=[]
    dT=0.0
    
    def Calc_Num_T(self,t):
        T=self.Calc_Num_dR(t)
        if (T):
            T=T.Normalize()
        return T
    
    def Calc_Num_Ts(self):
        self.Ts_Num=self.Calc_Mesh_Type_Num("T")
            
    def Calc_Ana_Ts(self):
        self.Ts_Ana=self.Calc_Mesh_Type_Ana("t")
            

    ##!
    ##! Verify unit tangents.
    ##!
    
    def Verify_Ts(self):
        self.dT,self.dTs,self.dT_Max=self.Verify_Mesh_Type("dR")
        return [
            "Unit Tangent:\t\t",
            "%.2e" % self.dT,
            str(self.dT_Max)
        ]

    ##!
    ##! Draw unit tangents as SVG.
    ##!
    
    def Ts_SVG(self):
        return self.Mesh_Vector_SVGs(
            "T",
            self.Curve_Component_Get("T","Color","Thick")
        )

