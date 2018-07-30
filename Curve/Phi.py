from Vector import Vector
from Mesh   import Mesh

class Curve_Phi():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature factor.
    ##! Store in self.Phi_Num and self.Phi_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Phi(self,t)
    ##!

    Phis_Num=None
    Phis_Ana=None

    dPhis=[]
    dPhi=0.0
    
    def Phi_Tex(self):
        return "\\frac{1}{\\psi(t)}"
    
    def Calc_Num_Phi(self,t):
        det=self.Calc_Num_Det(t)
        
        phi=None
        if (det!=0.0):
            v2=self.Calc_Num_v2(t)
            phi=v2/det

        return phi
    
    def Calc_Num_Phis(self):
        self.Phis_Num=Mesh(self.N,"Phi","Num")
        for n in range( self.N ):
            p=None
            phi=self.Calc_Num_Phi( self.ts[n] )
            if (phi):
                p=Vector([ self.ts[n],phi  ])
                  
            self.Phis_Num[n]=p
            
    def Calc_Ana_Phis(self):
        self.Phis_Ana=Mesh(self.N,"Phi","Ana")
        for n in range( self.N ):
            phi=self.Phi( self.ts[n] )
            v=None
            if (phi):
                v=Vector([self.ts[n],phi])
                
            self.Phis_Ana[n]=v
            
    ##!
    ##! Verify oscullating factors.
    ##!
    
    def Verify_Phis(self):
        dphi,self.dPhis,dphi_Max=self.Verify_Mesh_Type("Phi")

        return [
            "Phi:\t",
            "%.2e" %dphi,
            str(dphi_Max[1]),
        ]

    ##!
    ##! Draw curvature factors as SVG (function).
    ##!
    
    def Phis_SVG(self):
        self.Mesh_Function_SVGs("Phi")

