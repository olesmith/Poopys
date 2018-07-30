from Canvas2 import Canvas2


class Curve_Canvas():    
    ##!
    ##! Set canvas for scaling points to pixels
    ##!

    def Curve_Canvas_Init_Curves(self):
        self.Rs.Mesh_Canvas(self.__Canvas__)

        curves=[]
        curves=curves+self.Curve_Types_Derivatives()
        curves=curves+self.Curve_Types_Frenet()
        curves=curves+self.Curve_Types_Evolutes()
        curves=curves+self.Curve_Types_Vectors()
        
        for var in curves:
            #Numerical values
            meshname=var+"s_"+"Num"
            mesh=getattr(self,meshname)
            canvas=self.__Canvas__
            minmethod=var+"_PMin"
            maxmethod=var+"_PMax"
            
            if ( hasattr(self,minmethod) and  hasattr(self,maxmethod)):
                minmethod=getattr(self,minmethod)
                pmin=minmethod()
                maxmethod=getattr(self,maxmethod)
                pmax=maxmethod()
            else:
                pmin=mesh.Min()
                pmax=mesh.Max()
                
            #canvas=Canvas2(pmin,pmax,self.Resolution)
            mesh.Mesh_Canvas(canvas)
            
            #Name clash between t, the parameter and T, unit tangent.
            rvar=var
            if (var=="T"): rvar="t"
            elif (var=="N"): rvar="n"


            #Analytical values
            if ( self.Curve_Type_Has_Analytical(var) ):
                meshname=var+"s_"+"Ana"
                mesh=getattr(self,meshname)
                if (mesh!=None):
                    mesh.Mesh_Canvas(canvas)

        functions=self.Curve_Types_Functions()
        meshes=self.Curve_Functions_2_Meshes(functions)
        

        #canvas=self.Curve_Functions_Canvas(meshes)
        self.Curve_Functions_Canvas_Init()
                
    ##!
    ##! Set canvas for scaling points to pixels
    ##!

    def Curve_Canvas_Init_Functions(self):
       for var in self.Curve_Types_Functions():
            #Numerical values
            meshname=var+"s_"+"Num"
            mesh=getattr(self,meshname)

            mesh.Mesh_Canvas_Init(self.Resolution)

            #Analytical values
            if ( hasattr(self,var) ):
                meshname=var+"s_"+"Ana"
                mesh=getattr(self,meshname)
                if (mesh!=None):
                    mesh.Mesh_Canvas_Init(self.Resolution)
        
    ##!
    ##! Set canvas for scaling points to pixels
    ##!

    def Curve_Canvas_Init(self):
        self.__Canvas__=Canvas2(self.Min(),self.Max(),self.Resolution)

        #First the curve meshes
        self.Curve_Canvas_Init_Curves()
        
        #Then the functions
        self.Curve_Canvas_Init_Functions()

