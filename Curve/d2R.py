from Vector import Vector
from Mesh   import Mesh

class Curve_d2R():
    ##!
    ##! Calculate Numerical and, if defined, Analytical second order derivatives.
    ##! Store in self.d2Rs_Num and self.d2Rs_Ana.
    ##!
    ##! Analytical derivatives are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def d2R(self,t)
    ##!

    d2Rs_Num=None
    d2Rs_Ana=None

    dd2Rs=[]
    dd2R=0.0
    
    def Calc_Num_d2R(self,t):
        dr1=self.Calc_Num_dR(t-self.eps)
        dr2=self.Calc_Num_dR(t+self.eps)
        d2r=None
        if (dr1 and dr2):
            d2r=(  dr2-dr1 )*self.eps2
            
        return d2r
    
    def Calc_Num_d2Rs(self):
        self.d2Rs_Num=self.Calc_Mesh_Type_Num("d2R")

    def Calc_Ana_d2Rs(self):
        self.d2Rs_Ana=self.Calc_Mesh_Type_Ana("d2R")
            
            
    ##!
    ##! Calculate second order derivatives.
    ##!
    
    def Verify_d2Rs(self):
        self.dd2R,self.dd2Rs,self.dd2R_Max=self.Verify_Mesh_Type("d2R")
        
        return [
            "2nd Derivative:\t\t",
            "%.2e\t" % self.dd2R,
            str(self.dd2R_Max)
        ]
            

    ##!
    ##! Draw second order derivatives as SVG.
    ##!
    
    def d2Rs_SVG(self):
        return self.Curve_Type_Vectors_SVG(
            "d2R",
            {
                #"R": True,
                #"dR": True,
                "d2R": True,
            }
        )
