from Vector import Vector
from Mesh   import Mesh

class Curve_Evolute():
    ##!
    ##! Calculate Numerical and, if defined, Analytical curvature.
    ##! Store in self.Evolute_Num and self.Evolute_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Evolute(self,t)
    ##!

    Evolutes_Num=None
    Evolutes_Ana=None

    dEvolutes=[]
    dEvolute_=0.0
    
    def Calc_Num_Evolute(self,t):
        r=self.R(t)
        vn=self.Calc_Num_VN(t)
        phi=self.Calc_Num_Phi(t)

        c=None
        if (r and vn and phi.__class__.__name__=="float"):
            c=r+vn*phi
            
        return c
    
    def Calc_Num_Evolutes(self):
        self.Evolutes_Num=self.Calc_Mesh_Type_Num("Evolute")
        
            
    def Calc_Ana_Evolutes(self):
        self.Evolutes_Ana=self.Calc_Mesh_Type_Ana("Evolute")
            
    ##!
    ##! Calculate evolute points.
    ##!
    
    def Verify_Evolutes(self):
        self.dEvolute_,self.dEvolutes,self.dEvolute_Max=self.Verify_Mesh_Type("Evolute")
        
        return [
            "Evolute:\t\t",
            "%.2e" % self.dEvolute_,
            str(self.dEvolute_Max),
        ]
            
    ##!
    ##! Draw evolute points as SVG.
    ##!

    def Evolutes_SVG(self):
        meshname="Evolute"
        for dtype in ["Num","Ana" ]:
            self.Rs.SVG_Doc_Write(
                self.__Canvas__,
                self.Mesh_Curves_Draw(
                    dtype,
                    self.Curve_Coordinate_System_Get(),
                    {
                        #"R": True,
                        "Evolute": True,
                    }
                ),
                self.Curve_SVG_Name(meshname,dtype),
                False
            )
