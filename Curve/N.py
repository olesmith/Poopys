from Vector import Vector
from Mesh   import Mesh

class Curve_N():
    ##!
    ##! Calculate Numerical and, if defined, Analytical unit normal vector.
    ##! Store in self.Ns_Num and self.Ns_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def N(self,t)
    ##!

    Ns_Num=None
    Ns_Ana=None

    dNs=[]
    dN=0.0
    
    def Calc_Num_N(self,t):
        T=self.Calc_Num_T(t)
        
        N=None
        if (T):
            N=T.Hat2()
        return N
    
    def Calc_Num_Ns(self):
        self.Ns_Num=self.Calc_Mesh_Type_Num("N")
            
    def Calc_Ana_Ns(self):
        self.Ns_Ana=self.Calc_Mesh_Type_Ana("n")
            
    ##!
    ##! Verify analytical unit normals against the numerical.
    ##!
    
    def Calc_Verify_N(self,n):
        dn=0.0
        if (self.Ns_Num[n] and self.Ns_Ana[n]):
            dn=self.Ns_Num[n]-self.Ns_Ana[n]
            dn=dn.Length()
        
        self.dNs.append( dn )
        self.dN+=dn
            
    ##!
    ##! Calculate unit normals.
    ##!
    
    def Verify_Ns(self):
        self.dN,self.dNs,self.dN_Max=self.Verify_Mesh_Type("dR")

        return [
            "Unit Normal:\t\t",
            "%.2e" % self.dN,
            str(self.dN_Max)
        ]

    ##!
    ##! Draw unit normals as SVG.
    ##!
    
    def Ns_SVG(self):
        return self.Mesh_Vector_SVGs(
            "N",
            self.Curve_Component_Get("N","Color","Thick")
        )


