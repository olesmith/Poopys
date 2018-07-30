from R_n import *
from System import *

class Mesh_SVG():
    def Point2Pixels(self,p):
        return self.__Canvas__.Point2Pixels(p)
    
    def Points2Pixels(self,ps):
        return self.__Canvas__.Points2Pixels(ps)
    
    def Vector2Pixels(self,p):
        return self.__Canvas__.Vector2Pixels(p)
    
    def Vectors2Pixels(self,ps):
        return self.__Canvas__.Vectors2Pixels(ps)
    
    def Dist2Pixels(self,r):
        return self.__Canvas__.Dist2Pixels(r)
    
    def Mesh_Title_Get(self):
        return ", ".join([ self.Type,self.Name ])
    
    def Mesh_SVG_CSS(self,color,thick):
        return self.SVG_CSS_2_Text(
            [
                "   ."+self.Name+" {",
                "      stroke: "+str(color)+";",
                "      stroke-width: "+str(self.SVG_Thickness(thick))+";",
                "      fill: none;",
                "   }",
            ]
        )
    
    def Mesh_SVG_CoordSys(self,color,coordsys,thickness=2):
        svg=[self.SVG_Comment("Coordinate System")]

        if (coordsys.__class__.__name__=='bool'):
            coordsys=1.0
            
        if (coordsys.__class__.__name__=='float'):
            coordsys=[
                Vector([ 0.0,-coordsys]),
                Vector([ 0.0, coordsys]),
                Vector([-coordsys,0.0]),
                Vector([ coordsys,0.0]),
            ]
            
        px0=self.Point2Pixels([0.0,0.0])

        px1=self.Point2Pixels(coordsys[0])
        px2=self.Point2Pixels(coordsys[1])

        px3=self.Point2Pixels(coordsys[2])
        px4=self.Point2Pixels(coordsys[3])

        pxs=self.SVG_Vector_Arrow_Calc(px1,px2)

        for i in range( len(pxs) ):
            pxs[i]=pxs[i]-px2
            tmp=pxs[i][0]
            pxs[i][0]=-pxs[i][1]
            pxs[i][1]=tmp
            pxs[i]=pxs[i]+px4

        aparms={
            "style": {
                "stroke": color,
                "fill":   color,
            }
        }           


        #Left and right points on x-axis
        return [
            self.SVG_Comment("X Axis"),
            self.SVG_Line(
                self.Point2Pixels(Vector(coordsys[2])),
                self.Point2Pixels(Vector(coordsys[3])),
                color,
                thickness
            ),
            #Arrow
            self.SVG_Polyline(
                self.SVG_Vector_Arrow_Calc(px3,px4),
                color,
                thickness,
                aparms
            ),
            
            self.SVG_Comment("Y Axis"),
            self.SVG_Line(
                self.Point2Pixels(Vector(coordsys[0])),
                self.Point2Pixels(Vector(coordsys[1])),
                color,
                thickness
            ),
            #Arrow
            self.SVG_Polyline(
                self.SVG_Vector_Arrow_Calc(px1,px2),
                color,
                thickness,
                aparms
            ),
       ]
    
    def Mesh_SVG_Comment(self,message=""):
        svg=[
            "<!-- ",
            "Mesh: "+self.Name+" "+self.Type,
        ]

        if (message!=None):
            svg.append(message)
            
        svg=svg+[
            "-->"
        ]

        return svg

    def Mesh_SVG_Curve(self,color,thick=5,symmetries=[]):            
        svg=[]
        svg=svg+self.Mesh_SVG_Comment("Drawing Mesh: "+self.Type)
        svg=svg+self.Mesh_SVG_Comment("Color: "+color)

        parms={
            "class": self.Name,
        }
        svg=svg+self.SVG_Polyline(
            self.Points2Pixels(self),
            color,
            thick,
            parms
        )

        i=0
        for symmetry in symmetries:
            mesh=self.Map(symmetry)
            mesh.__Canvas__=self.__Canvas__
            
            svg=svg+mesh.Mesh_SVG_Comment("Drawing Mesh: "+self.Mesh_Title_Get())
            svg=svg+mesh.Mesh_SVG_Polyline(
                mesh,
                color,
                thick,
                parms
            )

            i+=1

        return svg
        
    def Mesh_SVG_Polyline(self,mesh,color,thick,parms={}):
        return self.SVG_Group(
            self.Name,
            mesh.SVG_Polyline(
                mesh.Points2Pixels(mesh),
                color,
                thick,
                parms
            )
        )
    
    def Mesh_SVG_Point(self,p,color="black",thickness=3,text=False):
        return self.SVG_Point(
            self.Point2Pixels(p),
            thickness,
            color
        )
    
    def Mesh_SVG_Points(self,color,size=3,text=False):
        pxs=self.Points2Pixels(self)
        return self.SVG_Points(pxs,size,color)
    
    def Mesh_SVG_Nos_2_Points(self,pointnos):
        pxs=[]
        for pointno in pointnos:
            pxs.append( self.Point2Pixels(self[pointno]) )
            
        return pxs
    
    def Mesh_SVG_Nos_Draw(self,pointnos,pcolors,thick=5,parms={}):
        svg=[]
        svg=svg+[ self.SVG_Comment(
            "Show Points, "+" ".join(pcolors)+": "+self.Mesh_Title_Get()
        ) ]

        svg=[]
        svg=svg+self.SVG_Points(
            self.Mesh_SVG_Nos_2_Points(pointnos),
            thick,
            pcolors,
            parms
        )

        return svg
        
    def Mesh_SVG_Draw_Curve(self,color,symmetries=[],showpointnos=[],thick=5,pcolors=[],pointsize=5,coordsys=True,addmeshes=[],addcolors=[]):
        if (not pcolors): pcolors=[color,color,color]

        if (not self.__Canvas__):
            
            print "No canvas defined...",fname
            return []
        
        svg=[]
        if (coordsys):
            svg=svg+self.Mesh_SVG_CoordSys("black",coordsys,3)

        svg=svg+self.Mesh_SVG_Curve(color,thick,symmetries)

        if (showpointnos):
            svg=svg+self.Mesh_SVG_Nos_Draw(showpointnos,pcolors,pointsize)

        return svg
    
    def Mesh_SVG(self,fname,color,tell=True,showpoints=[],thick=3,pcolor="",text=False,coordsys=True,addmeshes=[],addcolors=[],symmetries=[],svg=[]):
        if (not pcolor): pcolor=color

        if (not self.__Canvas__):
            
            print "No canvas defined...",fname
            return []

        svg=svg+self.Mesh_SVG_CSS(color,thick)
        svg=svg+self.Mesh_SVG_Draw_Curve(
            color,
            symmetries,
            showpoints,
            thick,
            pcolor,
            text,
            coordsys,
            addmeshes,
            addcolors
        )


        res=self.SVG_Doc_Write(
            self.__Canvas__,
            svg,
            fname,
            tell,
            None
        )

        return svg
    
    def Mesh_SVG_Vectors(self,meshes,every,fname,mesh_color,vector_colors,vector_thick,tell=True,symmetries=[]):
        svg=self.Mesh_SVG_CSS(mesh_color,vector_thick)
        svg=svg+self.Mesh_SVG_Curve(mesh_color,5,symmetries)
        for m in range( len(meshes) ):
            for n in range( len(self) ):
                if (n % every): continue

                px=self.Point2Pixels(self[n])
                if (px and meshes[m][n]):
                    mx=self.Point2Pixels(self[n]+meshes[m][n])
                    if (mx):
                        svg.append( self.SVG_Vector(px,mx,vector_colors[m],vector_thick) )

            for symmetry in symmetries:
                rmesh=self.Map(symmetry)
                rrmesh=meshes[m].Map(symmetry)
                
                for n in range( len(self) ):
                    if (n % every): continue
                    
                    px=self.Point2Pixels(rmesh[n])
                    if (px and rrmesh[n]):
                        mx=self.Point2Pixels(self[n]+rrmesh[n])
                        if (mx):
                            svg.append( self.SVG_Vector(px,mx,vector_colors[m],vector_thick) )

        #print svgs
        res=self.SVG_Doc_Write(self.__Canvas__,svg,fname,tell)

        return svg
   
