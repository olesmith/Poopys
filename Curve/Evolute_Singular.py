from File import *
from Vector import Vector
from Mesh   import Mesh

class Curve_Evolute_Singular():
    ##!
    ##! Calculate Numerical and, if defined, Analytical singular points.
    ##! Store in self.Evolute_Singular_Num and self.Evolute_Singular_Ana.
    ##!
    ##! Analytical values are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def Evolute(self,t)
    ##!
    
    Evolute_Singular_Num=[]
    Evolute_Singular_Ana=[]
    
    def Calc_Num_Evolute_Singulars(self):
        self.Evolute_Singular_Num=list()

        norm=self.Evolutes_Num.Norm()
        for n in range( self.N ):
            if (self.dEvolutes_Num[n]):
                if (self.dEvolutes_Num[n].Length()/norm<self.Singular_Eps):
                    self.Evolute_Singular_Num.append(n)
                
    def Calc_Ana_Evolute_Singluars(self):
        self.Evolute_Singular_Ana=list()
        
        norm=self.Evolutes_Ana.Norm()
        for n in range( self.N ):
            if (self.dEvolutes_Ana[n]):
                if (self.dEvolutes_Ana[n].Length()/norm<self.Singular_Eps):
                    self.Evolute_Singular_Ana.append(n)
                

    ##!
    ##! Show evolute irregular points.
    ##!
    
    def Evolute_Singular_Num_Show(self):
        text=[]
        for n in self.Evolute_Singular_Num:
            text.append( str(n) )
            
        return ", ".join(text)
    
    ##!
    ##! Show evolute irregular points.
    ##!
    
    def Evolute_Singular_Ana_Show(self):
        text=[]
        for n in self.Evolute_Singular_Ana:
            text.append( str(n) )
            
        return ", ".join(text)
    
    def Evolute_Singulars_Write(self):
        if (self.dEvolutes_Num):
            res=File_Write(
                self.Curve_File_Name("Evolute.Singular.Num.txt"),
                [ self.Evolute_Singular_Num_Show() ]
            )

        if (self.dEvolutes_Ana):
            res=File_Write(
                self.Curve_File_Name("Evolute.Singular.Ana.txt"),
                [ self.Evolute_Singular_Ana_Show() ]
            )

