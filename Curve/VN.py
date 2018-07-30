from Vector import Vector
from Mesh   import Mesh

class Curve_VN():
    ##!
    ##! Calculate Numerical and, if defined, Analytical velocity normal.
    ##! Store in self.VN_Num and self.VN_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def VN(self,t)
    ##!

    VNs_Num=None
    VNs_Ana=None

    dVNs=[]
    dVN=0.0
    
    def Calc_Num_VN(self,t):
        dr=self.Calc_Num_dR(t)
        if (dr):
            dr=dr.Hat2()
            
        return dr
    
    def Calc_Num_VNs(self):
        self.VNs_Num=self.Calc_Mesh_Type_Num("VN")
            
    def Calc_Ana_VNs(self):
        self.VNs_Ana=self.Calc_Mesh_Type_Ana("VN")
            
            
    ##!
    ##! Verify analytical velocity normals against the numerical.
    ##!
    
    def Verify_VNs(self):
        self.dVN,self.dVNs,self.dVN_Max=self.Verify_Mesh_Type("VN")

        return [
            "Velocity Normal:\t",
            "%.2e" % self.dVN,
            str(self.dVN_Max)
        ]
            

    ##!
    ##! Draw velocity normals as SVG.
    ##!
    
    def VNs_SVG(self):
        return self.Mesh_Vector_SVGs(
            "VN",
            self.Curve_Component_Get("VN","Color","Thick")
        )

