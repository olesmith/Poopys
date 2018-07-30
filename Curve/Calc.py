
from R_n import *
from Mesh import Mesh

class Curve_Calc():    
    def __Calc__(self,tell=False):
        self.Calc_ts()
        self.Calc_Rs()

        print "Calc:",", ".join(   self.Curve_Types_Calc()   )
        for ttype in self.Curve_Types_Calc():
            if (tell): print "__Calc__:",ttype,tell
            self.Curve_Run_Method_Types("Calc",ttype,tell)
        

        #Now, finally, set canvas
        self.Curve_Canvas_Init()

        return self.__Verify__()
        
    def Calc_Mesh_Type_Num(self,mtype):
        mesh=Mesh(self.N,mtype,"Num")

        method=getattr(self,"Calc_Num_"+mtype)
        
        for n in range( self.N ):
            mesh[n]=method(  self.ts[n]  )

        mesh.__Canvas__=self.__Canvas__
        return mesh
    
    def Calc_Mesh_Type_Ana(self,mtype):
        mesh=Mesh(self.N,mtype,"Ana")

        method=getattr(self,mtype)
        for n in range( self.N ):
            mesh[n]=None
            if (method):
                mesh[n]=method(  self.ts[n]  )

        mesh.__Canvas__=self.__Canvas__
        return mesh
    
    ##Calculates and returns as mesh, (t,func(t))
    ##Calculates protected, using try/except.
    
    def Calc_Ana_Function(self,function):
        attr=function
        if (not self.Curve_Type_Has_Analytical(function)):
            print "No analytical method:",attr
            return None

        if (not hasattr(self,attr)):
            print "No class attribute:",attr
            return None

        method=getattr(self,attr)
        mesh=Mesh(self.N,function,"Ana")
        
        errors=0
        for n in range( self.N ):
            mesh[n]=None

            value=None
            try:
                value=method( self.ts[n] )
            except:
                errors+=1
                
            if (value!=None):
                mesh[n]=Vector([  self.ts[n],value  ])
            
        return mesh
