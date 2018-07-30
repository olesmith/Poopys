from Canvas2 import Canvas2
from R_n import *

class Curve_SVG_Functions():
    def Mesh_Function_SVG(self,function,dtype):
        svg=[]
        print function,dtype
        attr=function+"s_"+dtype
        if (hasattr(self,attr)):
            dmesh=getattr(self,attr)

            if (dmesh):
                tell=self.Curve_SVG_Name(function,dtype)
                dmesh.__Canvas__=self.__Functions_Canvas__
                
                print function,dtype,self.Curve_SVG_Name(function,dtype)
                svg=svg+dmesh.Mesh_SVG(
                    self.Curve_SVG_Name(function,dtype),
                    self.Curve_Component_Get(function,"Color",dtype),
                    tell,
                    [], #showpoints
                    3,  #thick
                    "", #pcolor
                    True, #Text
                    self.Curve_Functions_Coord_System([ dmesh ])
                )

        return svg
                
    def Mesh_Function_SVGs(self,function):
        svg=[]
        svg=svg+self.Mesh_Function_SVG(function,"Num")
        svg=svg+self.Mesh_Function_SVG(function,"Ana")
        
        return svg

     ##! 
    ##! Returns function meshes canvas, default implementation,
    ##! detecting from functions list.
    ##!

    def Curve_Functions_Get(self,dtype,functions):
        rfunctions=[]
        for function in functions:
            rfunction=function+"s_"+dtype
            
            if (hasattr(self,rfunction)):
                rfunctions.append(rfunction)   
            else: print "Curve_Functions_SVG: Warning! No such attribute for function "+rfunction

        return rfunctions
    
    ##! 
    ##! Translates list of named meshes to meshes
    ##!

    def Curve_Functions_2_Meshes(self,functions,ctype="Num"):
        meshes=[]
        for function in functions:
            attrib=function+"s_"+ctype
            if (hasattr(self,attrib)):
                mesh=getattr(self,attrib)
                if (mesh):
                    meshes.append( mesh )

        return meshes
    
    ##! 
    ##! Translates list of named meshes to colors
    ##!

    def Curve_Functions_2_Colors(self,dtype,functions):
        colors=[]
        for function in functions:
            colors.append(   self.Curve_Component_Get(function,"Color",dtype)   )

        return colors
 
    ##! 
    ##! Calculates functions max/min values
    ##!

    def Curve_Functions_MaxMin(self,meshes):
        pmin=Vector([1.0E5,1.0E5])
        pmax=Vector([-1.0E5,-1.0E5])
        
        for mesh in meshes:
            pmin=pmin.Min( mesh.Min(meshes) )
            pmax=pmax.Max( mesh.Max(meshes) )
        
        return pmin,pmax
 
    ##! 
    ##! Calculates and initializes function canvas
    ##!

    def Curve_Functions_Canvas_MaxMin(self):
        return self.v2s_Num.Min(),self.v2s_Num.Max()

   ##! 
    ##! Calculates and initializes function canvas
    ##!

    def Curve_Functions_Canvas_Init(self):
        pmin,pmax=self.Curve_Functions_Canvas_MaxMin()
        self.__Functions_Canvas__=Canvas2(pmin,pmax,self.Resolution)

        
    ##! 
    ##! Calculates and initializes functions canvas
    ##!

    def Curve_Functions_Canvas(self,meshes):
        fmin,fmax=self.Curve_Functions_MaxMin(meshes)
        print "Curve_Functions_Canvas, Max/Min: ",fmin,",",fmax

        return Canvas2(
            fmin,
            fmax,
            self.Resolution
        )

    ##! 
    ##! Sets functions canvas
    ##!

    def Curve_Functions_Canvas_Set(self,meshes):
        canvas=self.Curve_Functions_Canvas(meshes)

        for mesh in meshes:
            mesh.__Canvas__=canvas

        
    ##! 
    ##! Returns coordinate system to user for function
    ##! 

    def Curve_Functions_Coord_System(self,meshes):        
        fmin,fmax=self.Curve_Functions_MaxMin(meshes)
        return [
            [ fmin[0],0.0 ],
            [ fmax[0],0.0 ],
            [ 0.0,fmin[1] ],
            [ 0.0,fmax[1] ],
        ]
 
    ##! 
    ##! Create a drawing of specified list of curve functions:
    ##!
    ##! v(t)^2, D(t), phi(t),psi(t),kappa(t),rho(t),s(t)
    ##! 

    def Curve_Functions_SVG(self,dtype,functionset,functions):        
        rfunctions=self.Curve_Functions_Get(dtype,functions)
        
        meshes=self.Curve_Functions_2_Meshes(rfunctions)
        colors=self.Curve_Functions_2_Colors(dtype,functions)
        if (len(meshes)==0): return []

        #self.Curve_Functions_Canvas_Set(meshes)
        
        svg=[]
        svg=svg+self.Curve_Legend_SVG(functions,meshes,colors)

        for n in range( len(meshes) ):
             svg=svg+meshes[n].Mesh_SVG_Draw_Curve(
                colors[n],
                [], #Symmetries???
                [],     #showpoints
                3,      #thick
                "",     #pcolor
                True,   #text
                self.Curve_Functions_Coord_System(meshes)
             )

             coordsys=False

        res=self.SVG_Doc_Write(
            meshes[0].__Canvas__,
            svg,
            self.Curve_SVG_Name(functionset+"_"+dtype),
            self.Curve_SVG_Name(functionset+"_"+dtype)
        )
            
        return svg
        
    ##! 
    ##! Create numerical and analytical drawings of specified list of curve functions:
    ##!
    ##! v(t)^2, D(t), phi(t),psi(t),kappa(t),rho(t),s(t),...
    ##! 

    def Curve_Functions_Sets_SVG(self,dtype):
        svg=[]

        for functionset in self.Functions_Show.keys():
            functions=self.Functions_Show[ functionset ]
            svg=svg+self.Curve_Functions_SVG(dtype,functionset,functions)
            
        return svg
    
    ##! 
    ##! Create list of drawings of specified list of curve functions:
    ##!
    ##! v(t)^2, D(t), phi(t),psi(t),kappa(t),rho(t),s(t)
    ##! 

    def Curve_Function_Sets_SVGs(self):
        for dtype in ["Num","Ana"]:
            self.Curve_Functions_Sets_SVG(dtype)
