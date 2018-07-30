
class Curve_SVG_Vectors():
    def Mesh_Vector_SVG(self,derivative,dtype,vector_thick):
        attr=derivative+"s_"+dtype
        derivativename=derivative
        if (derivative=="dR"): derivativename="d1R"
        if (derivative=="T"): derivativename="t"
        if (derivative=="N"): derivativename="n"

        svg=[]
        if (hasattr(self,attr)):
            dmesh=getattr(self,attr)
            if (dmesh):
                svgname=derivativename+"_V"
                tell=svgname+".svg"
                
                svg=svg+self.Rs.Mesh_SVG_Vectors(
                    [ dmesh ],
                    self.Derivative_Every,
                    self.Curve_SVG_Name(svgname,dtype),
                    self.Curve_Component_Get("R","Color"),
                    [
                        self.Curve_Component_Get(derivative,"Color",dtype),
                    ],
                    vector_thick,
                    tell
                )

        return svg
    
    def Mesh_Vector_SVGs(self,derivative,vector_thick):
        svg=[]
        svg=svg+self.Mesh_Vector_SVG(derivative,"Num",vector_thick)
        svg=svg+self.Mesh_Vector_SVG(derivative,"Ana",vector_thick)
        
        return svg
    
    ##! 
    ##! Do the drawing of indivudal accumulated curves
    ##! 

    def Curve_Type_Vectors_SVG(self,meshname,inc_meshes,alt_meshname=None,tell=False):
        if (alt_meshname==None): alt_meshname=meshname

        for dtype in ["Num","Ana" ]:
            self.Rs.SVG_Doc_Write(
                self.__Canvas__,
                self.Mesh_Curves_Draw(
                    dtype,
                    self.Curve_Coordinate_System_Get(),
                    inc_meshes
                ),
                
                self.Curve_SVG_Name(alt_meshname,dtype),
                tell
            )

        return self.Mesh_Vector_SVGs(
            meshname,
            self.Curve_Component_Get(meshname,"Color","Thick")
        )
