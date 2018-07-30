from Vector import Vector
from Mesh   import Mesh

class Curve_Rho():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature.
    ##! Store in self.Rho_Num and self.Rho_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Rho(self,t)
    ##!

    Rhos_Num=None
    Rhos_Ana=None

    dRhos=[]
    dRho=0.0
    
    def Calc_Num_Rho(self,t):
        det=self.Calc_Num_Det(t)
        
        rho=None
        if (det.__class__.__name__=="float" and det!=0.0):
            v2=self.Calc_Num_v2(t)
            if (v2.__class__.__name__=="float"):
                rho=(  v2**1.5  )/det

        return rho
    
    def Calc_Num_Rhos(self):
        self.Rhos_Num=Mesh(self.N,"Rho","Num")
        for n in range( self.N ):
            v=None
            rho=self.Calc_Num_Rho( self.ts[n] )
            if (rho.__class__.__name__=="float"):
                v=Vector([ self.ts[n],rho ])
                
            self.Rhos_Num[n]=v
            
    def Calc_Ana_Rhos(self):
        self.Rhos_Ana=Mesh(self.N,"Rho","Ana")
        for n in range(self.N ):
            v=None
            rho=self.Rho( self.ts[n] )
            if (rho):
                v=Vector([ self.ts[n],rho ])
                
            self.Rhos_Ana[n]=v
            
    ##!
    ##! Verify analytical curvature ratios against the numerical.
    ##!
    
    def Calc_Verify_Rho(self,n):
        dphi=0.0
        if (self.Rhos_Num[n] and self.Rhos_Ana[n]):
            dphi=abs(  (self.Rhos_Num[n][1]-self.Rhos_Ana[n][1])/self.Rhos_Num[n][1]  )
        
        self.dRhos.append( dphi )
        self.dRho+=dphi
                        
    ##!
    ##! Verify curvature ratios.
    ##!
    
    def Verify_Rhos(self):
        self.dRho=0.0
        for n in range( len(self.ts) ):
            self.Calc_Verify_Rho(n)
            
        drho="%.2e" % self.dRho
        return [  "Curvature Ratio:\t",drho  ]
    
    ##!
    ##! Draw curvature ratios as SVG (function).
    ##!
    
    def Rhos_SVG(self):
        self.Mesh_Function_SVGs("Rho")
 
