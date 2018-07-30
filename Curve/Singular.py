from File import *
from Vector import Vector
from Mesh   import Mesh

class Curve_Singular():
    ##!
    ##! Detect Numerical and, if defined, Analytical Singular Points.
    ##! Store in self.Singular_Num and self.Singular_Ana.
    ##!
    ##! Analytical derivatives are calculated, if provided by
    ##! actual Curve class (ie, Circle, Ellipse,....): def dR(self,t)
    ##!

    Singular_Num=[]
    Singular_Ana=[]
        
    def Calc_Num_Singulars(self):
        self.Singular_Num=list()

        norm=self.Rs.Norm()
        for n in range( self.N ):
            #print self.Singular_Eps,norm,n,self.dRs_Num[n].Length(),self.dRs_Num[n].Length()/norm
            if (   self.dRs_Num[n].Length()/norm<self.Singular_Eps   ):
                self.Singular_Num.append(n)
                #print "yep"
            
    def Calc_Ana_Singulars(self):
        self.Singular_Ana=list()
        
        norm=self.Rs.Norm()
        for n in range( self.N ):
            if (   self.dRs_Ana[n].Length()/norm<self.Singular_Eps   ):
                self.Singular_Ana.append(n)
            
    ##!
    ##! Show irregular points.
    ##!
    
    def Singular_Show_Num(self):
        text=[]
        for n in self.Singular_Num:
            text.append( str(n) )
            
        return ", ".join(text)
    ##!
    ##! Show irregular points.
    ##!
    
    def Singular_Show_Ana(self):
        text=[]
        for n in self.Singular_Ana:
            text.append( str(n) )
            
        return ", ".join(text)
    
    ##!
    ##! Write first order derivatives to files. Include Singular points.
    ##!
    
    def Singular_Write(self):
        res=File_Write(
            self.Curve_File_Name("Singular.Num.txt"),
            [ self.Singular_Show_Num() ]
        )
        
        if (self.dRs_Ana):
            res=File_Write(
                self.Curve_File_Name("Singular.Ana.txt"),
                [ self.Singular_Show_Ana() ]
            )
