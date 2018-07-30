from Vector import Vector
from Mesh   import Mesh

class Curve_d3R():
    ##!
    ##! Calculate Numerical and, if defined, Analytical third order derivatives.
    ##! Store in self.d3Rs_Num and self.d3Rs_Ana.
    ##!
    ##! Analytical derivatives are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def d3R(self,t)
    ##!

    d3Rs_Num=None
    d3Rs_Ana=None

    dd3Rs=[]
    dd3R=0.0
    dd3R_Max=[]
    
    def Calc_Num_d3R(self,t):
        d2r1=self.Calc_Num_d2R(t-self.eps)
        d2r2=self.Calc_Num_d2R(t+self.eps)
        d3r=None
        if (d2r1 and d2r2):
            d3r=(  d2r2-d2r1 )*self.eps2
            
        return d3r
    
    def Calc_Num_d3Rs(self):
        self.d3Rs_Num=self.Calc_Mesh_Type_Num("d3R")
            
    def Calc_Ana_d3Rs(self):
        self.d3Rs_Ana=self.Calc_Mesh_Type_Ana("d3R")
                                
    ##!
    ##! Verify third order derivatives.
    ##!
    
    def Verify_d3Rs(self):
        self.dd3R,self.dd3Rs,self.dd3R_Max=self.Verify_Mesh_Type("d3R")
        
        return [
            "3rd Derivative:\t\t",
            "%.2e" % self.dd3R,
            str(self.dd3R_Max),
        ]
           

    ##!
    ##! Draw third order derivatives as SVG.
    ##!
    
    def d3Rs_SVG(self):
        return self.Curve_Type_Vectors_SVG(
            "d3R",
            {
                #"R": True,
                #"dR": True,
                #"d2R": True,
                "d3R": True,
            }
        )
       
