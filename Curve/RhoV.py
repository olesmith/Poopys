from Vector import Vector
from Mesh   import Mesh

class Curve_RhoV():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature.
    ##! Store in self.RhoV_Num and self.RhoV_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def RhoV(self,t)
    ##!

    RhoVs_Num=None
    RhoVs_Ana=None

    dRhoVs=[]
    dRhoV=0.0

    def Calc_Num_RhoV(self,t):
        vn=self.Calc_Num_VN(t)
        phi=self.Calc_Num_Phi(t)

        rhov=None
        if (vn!=None and phi!=None):
            rhov=vn*phi
            
        return rhov
    
    def Calc_Num_RhoVs(self):
        self.RhoVs_Num=self.Calc_Mesh_Type_Num("RhoV")
            
    def Calc_Ana_RhoVs(self):
        self.RhoVs_Ana=self.Calc_Mesh_Type_Ana("RhoV")
            
    ##!
    ##! Verify analytical curvature ratios against the numerical.
    ##!
    
    def Calc_Verify_RhoV(self,n):
        drhov=None
        if (self.RhoVs_Num[n] and self.RhoVs_Ana[n]):
            drhov=self.RhoVs_Num[n]-self.RhoVs_Ana[n]
            drhov=drhov.Length()
            self.dRhoV+=drhov
            
        self.dRhoVs.append( drhov )
            
    ##!
    ##! Calculate curvature ratio vectors.
    ##!
    
    def Verify_RhoVs(self):
        self.dRhoV,self.dRhoVs,self.dRhoV_Max=self.Verify_Mesh_Type("RhoV")
        return [
            "Osculating Vector:\t",
            "%.2e" % self.dRhoV,
            str(self.dRhoV_Max)
        ]
            
    ##!
    ##! Draw curvature ratio vectors as SVG.
    ##!
    
    def RhoVs_SVG(self):
        self.Mesh_Curve_SVGs("RhoV")
        return self.Mesh_Vector_SVGs(
            "RhoV",
            self.Curve_Component_Get("RhoV","Color","Thick")
        )

