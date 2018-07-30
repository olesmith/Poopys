from File import *
from Vector import Vector
from Mesh   import Mesh

class Curve_dR():
    ##!
    ##! Calculate Numerical and, if defined, Analytical first order derivatives.
    ##! Store in self.dRs_Num and self.dRs_Ana.
    ##!
    ##! Analytical derivatives are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def dR(self,t)
    ##!

    dRs_Num=None
    dRs_Ana=None

    ddRs=[]
    ddR=0.0

    Singular_Num=[]
    Singular_Ana=[]
        
    def Calc_Num_dR(self,t):
        r1=self.R(t-self.eps)
        r2=self.R(t+self.eps)
        dr=None
        if (r1 and r2):
            dr=(  r2-r1 )*self.eps2
            
        return dr
    
    def Calc_Num_dRs(self):
        self.dRs_Num=self.Calc_Mesh_Type_Num("dR")
            
    def Calc_Ana_dRs(self):
        self.dRs_Ana=self.Calc_Mesh_Type_Ana("dR")
            
    ##!
    ##! Verify first order derivatives. Check for singular points.
    ##!
    
    def Verify_dRs(self):
        self.ddR,self.ddRs,self.ddR_Max=self.Verify_Mesh_Type("dR")
        return [
            "1st Derivative:\t\t",
            "%.2e" % self.ddR,
            str(self.ddR_Max)
        ]
            
    ##!
    ##! Write first order derivatives to files. Include Singular points.
    ##!
    
    def dRs_Write(self):
        if (self.dRs_Num):
            self.dRs_Num.Mesh_Write(   self.Curve_File_Name("d1R.N.txt")   )

        if (self.dRs_Ana):
            self.dRs_Ana.Mesh_Write(   self.Curve_File_Name("d1R.A.txt")   )

    ##!
    ##! Draw first order derivatives as SVG.
    ##!
    
    def dRs_SVG(self):
        return self.Curve_Type_Vectors_SVG(
            "dR",
            {
                #"R": True,
                "dR": True,
                #"d2R": True,
                #"d3R": True,
            },
            "d1R"
        )
