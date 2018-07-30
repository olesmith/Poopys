from Vector import Vector
from Mesh   import Mesh

class Curve_dPhi():

    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature derivative.
    ##! Store in:

    dPhis_Num=None
    dPhis_Ana=None

    
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Kappa(self,t)
    ##!

    ddPhis=[]
    ddPhi=0.0
    
    def Calc_Num_dPhi(self,t,eps=1.0E-6):
        v21=self.Calc_Num_Phi(t-eps)
        v22=self.Calc_Num_Phi(t+eps)
        
        dphi=None
        if (v21!= None and v21!=None):
            dphi=(v22-v21)/(2.0*eps)

        return dphi
    
    def Calc_Num_dPhis(self):
        self.dPhis_Num=Mesh(self.N,"dPhi","Num")
        for n in range( self.N ):
            dphi=self.Calc_Num_dPhi( self.ts[n] )
            v=None
            if (dphi):
                v=Vector([self.ts[n],dphi])
            self.dPhis_Num[n]=v
            
    def Calc_Ana_dPhis(self):
        self.dPhis_Ana=self.Calc_Ana_Function("dPhi")
            
    ##!
    ##! Verify analytical velocity normals against the numerical.
    ##!
    
    def Calc_Verify_dPhi(self,n):
        
        ddphi=0.0
        if (self.dPhis_Num[n] and self.dPhis_Ana[n]):
            ddphi=abs(
                (self.dPhis_Num[n][1]-self.dPhis_Ana[n][1])
                /
                self.dPhis_Num[n][1]
            )
        
        self.ddPhis.append( ddphi )
        self.ddPhi+=ddphi
            
            
    ##!
    ##! Verify curvatures derivatives.
    ##!
    
    def Verify_dPhis(self):
        ddphi,self.ddPhis,dphi_Max=self.Verify_Mesh_Type("dPhi")
        
        return [  "Curvature Derivative:\t","%.2e" % ddphi ]
           
    ##!
    ##! Draw curvatures as SVG (function).
    ##!
    
    def dPhis_SVG(self):
        self.Mesh_Function_SVGs("dPhi")

