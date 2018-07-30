from Vector import Vector
from Mesh   import Mesh

class Curve_dEvolute():
    ##!
    ##! Calculate Numerical and, if defined, Analytical evolute derivative.
    ##! Store in self.dEvolute_Num and self.dEvolute_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Evolute(self,t)
    ##!

    dEvolutes_Num=None
    dEvolutes_Ana=None

    ddEvolutes=[]
    ddEvolute=0.0
    ddEvolute_Max=[]
    
    def Calc_Num_dEvolute(self,t):
        cp=self.Calc_Num_Evolute(t+self.eps)
        cm=self.Calc_Num_Evolute(t-self.eps)
        dc=None
        if (cp and cm):
            dc=(cp-cm)*self.eps2
            
        return dc
    
    def Calc_Num_dEvolutes(self):
        self.dEvolutes_Num=self.Calc_Mesh_Type_Num("dEvolute")
          
    def Calc_Ana_dEvolutes(self):
        self.dEvolutes_Ana=self.Calc_Mesh_Type_Ana("dEvolute")
                
    ##!
    ##! Verify evolute derivatives and irregular points..
    ##!
    
    def Verify_dEvolutes(self):
        self.ddEvolute,self.ddEvolutes,self.ddEvolute_Max=self.Verify_Mesh_Type("dEvolute")
        return [
            "Evolute Derivative:\t",
            "%.2e" % self.ddEvolute,
            str(self.ddEvolute_Max)          
        ]


    ##!
    ##! Draw evolute derivatives as SVG
    ##!
    
    def dEvolutes_SVG(self):
        meshname="dEvolute"
        for dtype in ["Num","Ana" ]:
            self.Rs.SVG_Doc_Write(
                self.__Canvas__,
                self.Mesh_Curves_Draw(
                    dtype,
                    self.Curve_Coordinate_System_Get(),
                    {
                        #"R": True,
                        #"Evolute": True,
                        "dEvolute": True,
                    }
                ),
                self.Curve_SVG_Name(meshname,dtype),
                False
            )

