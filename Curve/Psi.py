from Vector import Vector
from Mesh   import Mesh

class Curve_Psi():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature factor.
    ##! Store in self.Psi_Num and self.Psi_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Psi(self,t)
    ##!

    Psis_Num=None
    Psis_Ana=None

    dPsis=[]
    ddPsi=0.0
        
    def Psi_Tex(self):
        return "\\frac{1}{\\varphi(t)}"
    
    #Default is to estimate dPsi with a numerical derivative
    

    def dPsi(self,t):
        return (self.Psi(t+self.eps)-self.Psi(t-self.eps))/self.eps2

    def Calc_Num_Psi(self,t):
        v2=self.Calc_Num_v2(t)
        
        psi=None
        if (v2!=0.0):
            det=self.Calc_Num_Det(t)
            psi=det/v2

        return psi
    
    def Calc_Num_Psis(self):
        self.Psis_Num=Mesh(self.N,"Psi","Num")
        for n in range( self.N ):
            p=None
            psi=self.Calc_Num_Psi( self.ts[n] )
            if (psi):
                p=Vector([ self.ts[n],psi  ])
                  
            self.Psis_Num[n]=p
            
    def Calc_Ana_Psis(self):
        self.Psis_Ana=Mesh(self.N,"Psi","Ana")
        for n in range( self.N ):
            psi=self.Psi( self.ts[n] )
            v=None
            if (psi):
                v=Vector([self.ts[n],psi])
                
            self.Psis_Ana[n]=v
            
             
    ##!
    ##! Verify curvature factors.
    ##!
    
    def Verify_Psis(self):
        dpsi,self.dPsis,dpsi_Max=self.Verify_Mesh_Type("Psi")

        return [
            "Psi:\t",
            "%.2e" %dpsi,
            str(dpsi_Max[1]),
        ]
    ##!
    ##! Draw curvature factors as SVG (function).
    ##!
    
    def Psis_SVG(self):
        self.Mesh_Function_SVGs("Psi")

