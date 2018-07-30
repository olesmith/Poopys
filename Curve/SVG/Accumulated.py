from File import *

class Curve_SVG_Accumulated():
    ##! 
    ##! Do the drawing of individual accumulated curves, initializer.
    ##! 

    def Curve_SVG_Accumulated_Init(self):
        return []

    ##! 
    ##! Do the drawing of indivudal accumulated curves
    ##! 

    def Curve_SVG_Accumulateds(self,parms):
        for meshtype in self.Curve_Types_SVG():
            self.Curve_SVG_Accumulateds_Mesh(meshtype,parms)
            
        self.Curve_SVG_Accumulated_SVGs_Write(
            "d0R",
            "",
            parms,
            self.Curve_SVG_Accumulateds_Mesh_Type_SVGs("d0R","",parms)
        )
        
    ##! 
    ##! 
    ##! 

    def Curve_SVG_Accumulateds_Mesh(self,meshtype,parms):
        for ctype in ["Num","Ana"]:
            self.Curve_SVG_Accumulateds_Mesh_Type(meshtype,ctype,parms)

        
    ##! 
    ##! 
    ##! 

    def Curve_SVG_Accumulateds_Mesh_Type(self,meshtype,ctype,parms):
        self.Curve_SVG_Accumulated_SVGs_Write(
            meshtype,
            ctype,
            parms,
            self.Curve_SVG_Accumulateds_Mesh_Type_SVGs(meshtype,ctype,parms)
        )
            
    ##! 
    ##! 
    ##! 

    def Curve_SVG_Accumulated_SVGs_Write(self,meshtype,ctype,parms,svgfiles):
        svgname=self.Name+"_"+meshtype+"_"+ctype+".svg"
        if (meshtype=="d0R"): svgname=self.Name+".svg"
        
        self.SVGs_Images_Write(
            "/".join([
                "/usr/local/Curves",
                self.Name,
                svgname
            ]),
            svgfiles,
            self.Curve_SVG_Accumulateds_Mesh_Type_ViewBoxes(svgfiles),
            ctype,
            parms
        )
            

    ##! 
    ##! 
    ##! 

    def Curve_SVG_Accumulateds_Mesh_Type_ViewBoxes(self,svgfiles):
        viewboxes=[]
        for svgfile in svgfiles:
            rsvgname="/".join([
                "/usr/local/Curves",
                self.Name,
                svgfile
            ])
            
            viewboxes.append(self.SVG_File_2_ViewBox(rsvgname))

        return viewboxes

            
    ##! 
    ##! 
    ##! 

    def Curve_SVG_Accumulateds_Mesh_Type_SVGs(self,meshtype,ctype,parms):
        svgfiles=[]
        for cparms in parms:
            cparms=self.Curve_Parameters_2_Path(meshtype,ctype,cparms)
            #Last comp if file name
            cparms=cparms.pop()

            if (meshtype=="d0R"):
                cparms=re.sub('^Num_',"",cparms)
                
            if (meshtype=="dR"):
                meshtype="d1R"
                
            svgname=meshtype+"/"+cparms+".svg"
                    
            rsvgname="/".join([
                "/usr/local/Curves",
                self.Name,
                svgname
            ])

            if (   File_Exists(rsvgname)   ):
                #Add
                svgfiles.append(svgname)
            else:
                print "Nonexistent",svgname
                
        return svgfiles
                    
