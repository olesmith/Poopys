from Vector import Vector
from Mesh   import Mesh

class Curve_dKappa():

    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature derivative.
    ##! Store in:

    dKappas_Num=None
    dKappas_Ana=None

    
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Kappa(self,t)
    ##!

    ddKappas=[]
    ddKappa=0.0
    
    def Calc_Num_dKappa(self,t,eps=1.0E-6):
        v21=self.Calc_Num_v2(t-eps)
        v22=self.Calc_Num_v2(t+eps)
        
        dkappa=None
        if (v21!= None and v21!=None):
            dkappa=(v22-v21)/(2.0*eps)

        return dkappa
    
    def Calc_Num_dKappas(self):
        self.dKappas_Num=Mesh(self.N,"dKappa","Num")
        for n in range( self.N ):
            dkappa=self.Calc_Num_dKappa( self.ts[n] )
            v=None
            if (dkappa):
                v=Vector([self.ts[n],dkappa])
            self.dKappas_Num[n]=v
            
    def Calc_Ana_dKappas(self):
        if (not self.Curve_Type_Has_Analytical("dKappa")): return
        
        self.dKappas_Ana=Mesh(self.N,"dKappa","Ana")
        for n in range( self.N ):
            dkappa=self.dKappa( self.ts[n] )
            v=None
            if (dkappa):
                v=Vector([self.ts[n],dkappa])
                
            self.dKappas_Ana[n]=v
            
    ##!
    ##! Verify analytical velocity normals against the numerical.
    ##!
    
    def Calc_Verify_dKappa(self,n):
        
        ddkappa=0.0
        if (self.dKappas_Num[n] and self.dKappas_Ana[n]):
            ddkappa=abs(
                (self.dKappas_Num[n][1]-self.dKappas_Ana[n][1])
                /
                self.dKappas_Num[n][1]
            )
        
        self.ddKappas.append( ddkappa )
        self.ddKappa+=ddkappa
            
            
    ##!
    ##! Verify curvatures derivatives.
    ##!
    
    def Verify_dKappas(self):
        ddkappa,self.ddKappas,dkappa_Max=self.Verify_Mesh_Type("dkappa")
        
        return [  "Curvature Derivative:\t","%.2e" % ddkappa ]
           
    ##!
    ##! Draw curvatures as SVG (function).
    ##!
    
    def dKappas_SVG(self):
        self.Mesh_Function_SVGs("dKappa")

