
class Curve_SVG_Curves():
    ##!
    ##! Draw Curve Mesh type (Num or Ana) as SVG. 
    ##!

    def Mesh_Curve_SVG(self,meshname,dtype,color,pcolor="white",coordsys=True,addmeshes=[],addcolors=[]):
        if (coordsys):
            coordsys=self.Curve_Coordinate_System_Get()
        
        attr=meshname+"s"
        if (dtype!=""): attr=attr+"_"+dtype
        
        if (meshname=="dR"): meshname="d1R"
        
        svg=[]
        if (hasattr(self,attr)):
            mesh=getattr(self,attr)
            if (mesh):
                svg=mesh.Mesh_SVG(
                    self.Curve_SVG_Name(meshname,dtype),
                    color,
                    False,#tell
                    self.Mesh_Show_Point_Nos(),
                    self.Curve_Thickness,
                    "",
                    False,
                    coordsys,
                    addmeshes,
                    addcolors,
                    self.Symmetries
                )
            else:
                print "Unable to get mesh attribute: ",attr
                #exit()
        else:
            print "Mesh attribute unavaliable: ",attr
            #exit()

        return svg

    ##!
    ##! Draw numerical and analytical Curve Meshes as SVG. 
    ##!

    def Mesh_Curve_SVGs(self,meshname,nummeshes=[],anameshes=[],addcolors=[]):
        if ( len(nummeshes)==0 ):
            nummeshes=[ self.Rs ]
            addcolors= [
                self.Curve_Component_Get("R","Color","Num"),
            ]
            
        if ( len(anameshes)==0 ):
            anameshes=[ self.Rs ]
            addcolors= [
                self.Curve_Component_Get("R","Color","Ana"),
            ]

        svg=[]
        svg=svg+self.Mesh_Curve_SVG(
            meshname,
            "Num",
            self.Curve_Component_Get(meshname,"Color","Num"),
            "white",
            True,
            nummeshes,
            addcolors
        )

        svg=svg+self.Mesh_Curve_SVG(
            meshname,
            "Ana",
            self.Curve_Component_Get(meshname,"Color","Ana"),
            "white",
            True,
            anameshes,
            addcolors
        )

        return svg
    def Mesh_Curve_Draw(self,meshname,dtype,coordsys):
        thick=3
        pcolor="black"
        text=True
        addmeshes=[]
        addcolors=[]
        
         
        attr=meshname+"s"
        if (meshname!="R" and dtype!=""): attr=attr+"_"+dtype
        
        svg=[]
        if (hasattr(self,attr)):
            
            mesh=getattr(self,attr)
            if (mesh):
                svg=mesh.Mesh_SVG_CSS(
                    self.Curve_Component_Get(meshname,"Color","Num"),
                    thick
                )

                svg=svg+mesh.Mesh_SVG_Draw_Curve(
                    self.Curve_Component_Get(meshname,"Color","Num"),
                    self.Symmetries,
                    self.Mesh_Show_Point_Nos(),
                    thick,
                    self.Mesh_Show_Point_Colors(),
                    self.Show_Point_Size,
                    coordsys
                )
            #else: print "No mesh:",attr
        else: print "No attribute:",attr

        return svg
       
        
    def Mesh_Curves_Draw(self,dtype,coordsys,parameters=None):
        if (parameters==None):
            parameters={
                "R": True,
            }
        
        meshnames=["R","dR","d2R","d3R","Evolute","dEvolute",]
        showpoints=[]
        thick=3
        
        svg=[]
        for meshname in meshnames:
            if (parameters.has_key(meshname)):
                svg=svg+self.Mesh_Curve_Draw(meshname,dtype,coordsys)
                coordsys=False
        
        return svg


