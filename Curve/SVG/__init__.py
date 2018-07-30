from Canvas2 import Canvas2
from File    import *

from Curves import Curve_SVG_Curves
from Vectors import Curve_SVG_Vectors
from Functions import Curve_SVG_Functions
from Legends import Curve_SVG_Legends
from Frenet import Curve_SVG_Frenet
from Accumulated import Curve_SVG_Accumulated

class Curve_SVG(
        Canvas2,
        Curve_SVG_Curves,
        Curve_SVG_Vectors,
        Curve_SVG_Functions,
        Curve_SVG_Legends,
        Curve_SVG_Frenet,
        Curve_SVG_Accumulated
    ):
    #Parameter controlling density of shown derivatives and Frenet systems.
    Derivative_Every=5
    Frenet_Every=20
    
    #Numbers of points to display show.
    #Ex Irregular points.
    Show_Point_Size=5
    Show_Points=[]
    Show_Point_Nos=[]
    Show_Point_Colors=['black','purple','midnightblue']
    
    Coord_System=None
    
    Symmetries=[]
    Functions_Show={
    }


    #Does nothing, meant to be overridden
    def Curve_SVG_Draw(self):
        return
    
    def SVG_Doc_Write(self,canvas,svg,fname,tell=False,viewBox=None,css=None):
        return self.Rs.VG_Doc_Write(canvas,svg,fname,tell,viewBox,css)
    
    def __SVG__(self):
        print "SVG:",", ".join(   self.Curve_Types_SVG()   )
        for ctype in self.Curve_Types_SVG():
            method=getattr(self,ctype+"s_SVG")
            method()

        self.Mesh_Frenet_SVGs()
        self.Curve_Function_Sets_SVGs()

        #Curve post drawing, specified in def Curve_SVG_Draw (meant to be overriden)
        self.Curve_SVG_Draw()

        self.SVGs()


        
    def SVGs(self):
        svgfiles=[]
        parms=self.Curve_Parameters_2_Paths()
        for ctype in ["Num","Ana"]:

            self.SVGs_MeshTypes(
                self.Curve_Meshes(),
                ctype,
                parms,
                self.Name+"_"+ctype+"_"+parms+".svg"
            )
            
            self.SVGs_MeshTypes(
                self.Curve_Types_Functions(),
                ctype,
                parms,
                self.Name+"_"+"Functions"+"_"+ctype+"_"+parms+".svg"
            )
            
            #self.SVGs_MeshTypes(
            #    self.Curve_Types_dFunctions(),
            #    ctype,
            #    parms,
            #    self.Name+"_"+"dFunctions"+"_"+ctype+"_"+parms+".svg"
            #)
 
            
    def SVGs_MeshTypes(self,meshes,ctype,parms,svgname):
        svgfiles=[]
        viewboxes=[]
            
        meshtypes=[]
        colors=[]
        for meshtype in meshes:
            if (meshtype=="dR"): meshtype="d1R"
                
            rsvgname=meshtype+"/"+ctype+"_"+parms+".svg"

            if (meshtype=="R"): rsvgname="d0R"+"/"+parms+".svg"

            fullsvgname="/".join([
                "/usr/local/Curves",
                self.Name,
                rsvgname
            ])

            if (   File_Exists(fullsvgname)   ):
                svgfiles.append(   rsvgname   )
                viewboxes.append(self.SVG_File_2_ViewBox(fullsvgname))
                    
                meshtypes.append(meshtype)
                colors.append( self.Curve_Component_Color(meshtype,ctype)  )
                    
            else:
                print "Nonexistent",svgname


        return self.SVGs_Images_Write(
            "/".join([
                "/usr/local/Curves",
                self.Name,
                svgname
            ]),
            svgfiles,
            viewboxes,
            ctype,
            parms,
            self.Curve_Legend_SVG(
                meshtypes,
                colors
            )
        )
            
    def SVGs_Images_Write(self,svgfile,svgfiles,viewboxes,ctype,parms,legend=[]):
        svg=self.SVG_Images(svgfiles,self.__Canvas__.Resolution[0],self.__Canvas__.Resolution[1])

        legend=[]
        rsvg=self.SVG_Doc_Write(
            self.__Canvas__,
            [ svg + legend ],
            svgfile,
            True, #tell
            " ".join([
                "0","0",
                str(self.__Canvas__.Resolution[1]),
                str(self.__Canvas__.Resolution[0]),
            ])
        )                

        pdffile=re.sub('\.svg$',".pdf",svgfile)
        self.SVG_2_PDF(svgfile,pdffile)

        
    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        return 1.0
    
    ##!
    ##! 
    ##!

    def Mesh_Show_Point_Nos(self):
        return self.Show_Point_Nos
    
    ##!
    ##! 
    ##!

    def Mesh_Show_Point_Colors(self):
        return self.Show_Point_Colors
    


   
    
    
