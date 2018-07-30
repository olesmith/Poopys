from Vector import Vector
from Mesh   import Mesh

class Curve_dRho():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature derivative.
    ##! Store in:

    dRhos_Num=None
    dRhos_Ana=None

    
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Kappa(self,t)
    ##!

    ddRhos=[]
    ddRho=0.0
        
    def Calc_Num_dRho(self,t,eps=1.0E-6):
        v21=self.Calc_Num_Rho(t-eps)
        v22=self.Calc_Num_Rho(t+eps)
        
        drho=None
        if (v21!= None and v21!=None):
            drho=(v22-v21)/(2.0*eps)

        return drho
    
    def Calc_Num_dRhos(self):
        self.dRhos_Num=Mesh(self.N,"dRho","Num")
        for n in range( self.N ):
            drho=self.Calc_Num_dRho( self.ts[n] )
            v=None
            if (drho):
                v=Vector([self.ts[n],drho])
            self.dRhos_Num[n]=v
            
    def Calc_Ana_dRhos(self):
        self.dRhos_Ana=self.Calc_Ana_Function("dRho")
        
            
    ##!
    ##! Verify analytical velocity normals against the numerical.
    ##!
    
    def Calc_Verify_dRho(self,n):
        
        ddrho=0.0
        if (self.dRhos_Num[n] and self.dRhos_Ana[n]):
            ddkappa=abs(
                (self.dRhos_Num[n][1]-self.dRhos_Ana[n][1])
                /
                self.dRhos_Num[n][1]
            )
        
        self.ddRhos.append( ddrho )
        self.ddRho+=ddrho
            
            
    ##!
    ##! Verify curvatures derivatives.
    ##!
    
    def Verify_dRhos(self):
        ddrho,self.ddRhos,dkappa_Max=self.Verify_Mesh_Type("dRho")
        
        return [  "Rho':\t","%.2e" % ddrho ]
           
    ##!
    ##! Draw curvatures as SVG (function).
    ##!
    
    def dRhos_SVG(self):
        self.Mesh_Function_SVGs("dRho")

