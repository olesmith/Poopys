from Vector import Vector
from Mesh   import Mesh

class Curve_dPsi():

    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature derivative.
    ##! Store in:

    dPsis_Num=None
    dPsis_Ana=None

    
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Kappa(self,t)
    ##!

    ddPsis=[]
    ddPsi=0.0
    
    def Calc_Num_dPsi(self,t,eps=1.0E-6):
        v21=self.Calc_Num_Psi(t-eps)
        v22=self.Calc_Num_Psi(t+eps)
        
        dpsi=None
        if (v21!= None and v21!=None):
            dpsi=(v22-v21)/(2.0*eps)

        return dpsi
    
    def Calc_Num_dPsis(self):
        self.dPsis_Num=Mesh(self.N,"dPsi","Num")
        for n in range( self.N ):
            dpsi=self.Calc_Num_dPsi( self.ts[n] )
            v=None
            if (dpsi):
                v=Vector([self.ts[n],dpsi])
            self.dPsis_Num[n]=v
            
    def Calc_Ana_dPsis(self):
        self.dPsis_Ana=self.Calc_Ana_Function("dPsi")
            
    ##!
    ##! Verify analytical velocity normals against the numerical.
    ##!
    
    def Calc_Verify_dPsi(self,n):
        
        ddpsi=0.0
        if (self.dPsis_Num[n] and self.dPsis_Ana[n]):
            ddpsi=abs(
                (self.dPsis_Num[n][1]-self.dPsis_Ana[n][1])
                /
                self.dPsis_Num[n][1]
            )
        
        self.ddPsis.append( ddpsi )
        self.ddPsi+=ddpsi
            
            
    ##!
    ##! Verify curvatures derivatives.
    ##!
    
    def Verify_dPsis(self):
        ddpsi,self.ddPsis,dpsi_Max=self.Verify_Mesh_Type("dPsi")
        
        return [  "Curvature Derivative:\t","%.2e" % ddpsi ]
           
    ##!
    ##! Draw curvatures as SVG (function).
    ##!
    
    def dPsis_SVG(self):
        self.Mesh_Function_SVGs("dPsi")

