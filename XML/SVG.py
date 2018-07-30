from CGI  import CGI
from File import *
from R_n import *

from math import *
from re import *

class XML_SVG(CGI):
    #Size of Vector arrows
    VScale=0.05
    NScale=0.025


    ##!
    ##! Detect viewport in svgfile
    ##!
    
    def SVG_File_2_ViewBox(self,svgfile):
        svgs=File_Read(svgfile)
        for svg in svgs:
            srch=re.search("viewBox=\"([^\"]+)\"",svg)
            if (srch):
                return srch.group(1)

        
        return ""
        
    ##!
    ##! Run external command to convert svg to pdf 
    ##!
    
    def SVG_2_PDF(self,svgfile,outfile):
        return Command_Exec([
            "/var/www/cgi-bin/PDF",
            svgfile,
            outfile            
        ])
        
    ##!
    ##! Run external command to convert svg to png 
    ##!
    
    def SVG_2_PNG(self,svgfile,outfile):
        return Command_Exec([
            "/var/www/cgi-bin/PNG",
            svgfile,
            outfile            
        ])
        

    ##!
    ##! Return SVG preamble section:
    ##!
    
    def SVG_Pre_Amble(self,canvas,viewbox=None,css=None):
        svg=[]
        svg=svg+self.SVG_Head()
        if (css!=None):
            svg=svg+css
        svg=svg+self.SVG_Header(canvas,viewbox)
        svg=svg+[    "<!-- **** DRAWING START **** -->" ]

        return svg

    ##!
    ##! Return SVG postamble section:
    ##!
    
    def SVG_Post_Amble(self,canvas):
        return [
            "<!-- **** DRAWING END **** -->",
            self.SVG_Close()
        ]

        

    ##!
    ##! Return SVG version tag.
    ##!
    
    def SVG_Version(self):
        return [
            '<?xml version="1.0"?>',
        ]
    
    ##!
    ##! Return list of external styleheets
    ##!
    
    def SVG_CSS_External(self):
        return [
            #'<?xml-stylesheet type="text/css" href="style8.css" ?>',
            #'<?xml-stylesheet type="text/css" href="http://127.0.0.1/poops.css" ?>',            
        ]

    
    ##!
    ##! Return svg doctype tag
    ##!
    
    def SVG_DOCTYPE(self):
        return [
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"',
            '    "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">',
            '',
        ]

    ##!
    ##! Join svg head part.
    ##!
    
        
    def SVG_Head(self):
        return self.SVG_Version()+self.SVG_CSS_External()+self.SVG_DOCTYPE()


    
    ##!
    ##! Join svg header part.
    ##!

    def SVG_Header(self,canvas,viewbox=None):
         svg=[
             self.SVG_Open(canvas,viewbox),
             self.SVG_CSS_Internal(),
             self.SVG_Title(self.Title),
             self.SVG_Name(self.Name),
         ]

         svg=svg+self.SVG_Defs()
         
         return svg
       
    
    ##!
    ##! Join svg viewbox value
    ##!

    def SVG_ViewBox(self,canvas,viewbox=None):
        if (viewbox!=None): return "" #viewbox
        
        p=canvas.PMax-canvas.PMin
        
        return [
            canvas.PMin[0],canvas.PMin[1],
            p[0],p[1]
        ]

    
    ##!
    ##! Opening svg and g tag
    ##!

    def SVG_Open(self,canvas,viewbox=None):
        transforms=[
            "translate("+str(0.0)+","+str(canvas.PMax[1]+canvas.PMin[1])+")",
            "scale(1,-1)",
        ]
        return self.XML_Tag(
            "svg",
            {
                "xmlns":            'http://www.w3.org/2000/svg',
                "xmlns:xlink":      'http://www.w3.org/1999/xlink',
                "version":          "1.1",
                "height":            str(canvas.Resolution[0]),
                "width":           str(canvas.Resolution[1]),
                "viewBox":          self.SVG_ViewBox(canvas,viewbox),
            }
        )
    
    ##!
    ##! Closing svg and g tag
    ##!
    
    def SVG_Close(self):
        return "</svg>"

    ##!
    ##! URL to our CSS file
    ##!
    

    def SVG_CSS_URL(self,css="http://127.0.0.1/poops.css"):
        return css

    ##!
    ##! URL to our inline CSS file
    ##!
    
    def SVG_CSS_2_Text(self,css):
        css=["<![CDATA["]+css+["]]>"]
        return self.XML_Tags("style",css)
    
    ##!
    ##! URL to our inline CSS file
    ##!
    
    def SVG_CSS_Internal(self,css="poops.css"):
        return ""
    
        css=self.File_Read(css)
        css="\n/* CSS BEGIN */\n"+css
        css=css+"\n/* CSS END */\n"

        css="<![CDATA[\n"+css+"]]>"
        return self.XML_Tags("style",css)

    ##! 
    ##! SVG title tag
    ##!
    
    def SVG_Title(self,title):
        return self.XML_Tags("title",title)

    ##! 
    ##! SVG name tag
    ##!
    
    def SVG_Name(self,name):
        return self.XML_Tags("name",name)

    ##! 
    ##! SVG defs section
    ##!
    
    def SVG_Defs(self,svg=[]):
        return [
            '<defs>',
            svg,
            '</defs>',
        ]

 
    ##! 
    ##! Generate an SVG comment
    ##!
    
    def SVG_Comment(self,comment):
        return self.XML_Comment(comment)
   
    ##! 
    ##! Create minimum parms dictionary. Include style key, being dictionary.
    ##!
    
    def SVG_Parms(self,parms):
        lparms=dict(parms)
        if (not lparms.has_key("style")): lparms[ "style" ]={}
        
        lparms[ "style" ]=dict(lparms[ "style" ])

        return lparms
   
    ##! 
    ##! Sandwiches svg between pre and postambles.
    ##!
    
    def SVG_Ambles_Put(self,canvas,svg,viewBox=None,css=None):
        return self.SVG_Pre_Amble(canvas,viewBox,css)+svg+self.SVG_Post_Amble(canvas)
   
    ##! 
    ##! Writes SVG to file
    ##!
    def SVG_Doc_Write(self,canvas,svg,fname,tell=True,viewBox=None,css=None):
        rsvg=self.SVG_Pre_Amble(canvas,viewBox,css)+svg+self.SVG_Post_Amble(canvas)
        
        res= self.XML_Write(
            fname,
            rsvg,
            tell
        )

        return rsvg
    
   
    #### Drawing text
    
    def SVG_Text(self,px,text,color="black",size=1,parms={}):
        lparms=self.SVG_Parms(parms)
        lparms[ "x" ]=px[0]
        lparms[ "y" ]=px[1]

        lparms[ "style" ][ "stroke" ]=color
        lparms[ "style" ][ "fill" ]=color
        lparms[ "style" ][ "font-size" ]=size
        svg=self.XML_Tags("text",text,lparms)
         
        return svg
       
    #### Generate circle of points
    
    def SVG_Circle_Gen(self,px,r,n=20):
        dtheta=2.0*pi/(1.0*n)
        theta=0.0

        ps=[]
        for i in range(n):
            ps.append(px+E(theta)*r)
            theta+=dtheta

        return ps
       
    #### Drawing Points
    
    def SVG_Point(self,px,r,color,parms={},n=20):
        rparms=dict(parms)
        rparms[ "style" ]={}
        rparms[ "style" ][ "fill" ]=color
    
        ps=self.SVG_Circle_Gen(px,self.SVG_Thickness(r),n)
        
        return self.SVG_Polyline(ps,color,3,rparms,True)

    def SVG_Points(self,pxs,r,colors,parms={}):
        svg=[]
        n=1
        for i in range( len(pxs) ):
            
            svg.append( self.SVG_Point(pxs[i],r,colors[i],parms) )
            n+=1

        return svg
    
    #### Convert a line thickness factor to thickness

    def SVG_Thickness(self,thick):
        return self.__Canvas__.Thickness_Factor*thick
    
    #### Drawing Line segments

    def SVG_Line(self,px1,px2,color,thick=1,parms={}):
        lparms=self.SVG_Parms(parms)
        
        lparms[ "x1" ]=str(px1[0])
        lparms[ "y1" ]=str(px1[1])
        lparms[ "x2" ]=str(px2[0])
        lparms[ "y2" ]=str(px2[1])

        
        lparms[ "style" ][ "stroke" ]=color
        lparms[ "style" ][ "stroke-width" ]=self.SVG_Thickness(thick)

        return self.XML_Tag1("line",lparms)

    
    #### Drawing Polylines
    
    def SVG_Polyline(self,pxs,color=None,thick=None,parms={},close=False):
        lparms=self.SVG_Parms(parms)

        if (color!=None):
            lparms[ "style" ][ "stroke" ]=color
            
        if (not lparms[ "style" ].has_key("fill")):
            lparms[ "style" ][ "fill" ]="none"

        if (thick!=None):
            lparms[ "style" ][ "stroke-width" ]=self.SVG_Thickness(thick)

        if (close):
            pxs.append( pxs[0] )


        points=[]
        svgs=[]
        for px in pxs:
            if (px):
                points.append( str(px[0])+","+str(px[1]) )
            else:
                lparms[ "points" ]="\n   "+"\n   ".join(points)+"\n"
                svgs.append( self.XML_Tag1("polyline",lparms) )
                points=list([])

        if ( len(points)>0 ):
                lparms[ "points" ]="\n   "+"\n   ".join(points)+"\n"
                svgs.append( self.XML_Tag1("polyline",lparms) )
                        
        return svgs
    
    #### Drawing Polygones
    
    def SVG_Polygone(self,pxs,color,parms={},close=True):
        lparms=self.SVG_Parms(parms)

        lparms[ "style" ][ "stroke" ]=color
        lparms[ "style" ][ "fill" ]=color

        if (close):
            pxs.append( pxs[0] )


        points=[]
        svgs=[]
        for px in pxs:
            if (px):
                points.append( str(px[0])+","+str(px[1]) )
            else:
                lparms[ "points" ]="\n   "+"\n   ".join(points)+"\n"
                svgs.append( self.XML_Tag1("polygone",lparms) )
                points=list([])

        if ( len(points)>0 ):
                lparms[ "points" ]="\n   "+"\n   ".join(points)+"\n"
                svgs.append( self.XML_Tag1("polygone",lparms) )
                        

        return svgs

   #### Drawing Circles

    def SVG_Circle(self,cx,rx,color,parms={}):
        lparms=self.SVG_Parms(parms)

        lparms[ "cx" ]=str(cx[0])
        lparms[ "cy" ]=str(cx[1])
            
        lparms[ "style" ][ "stroke" ]=color
        lparms[ "style" ][ "fill" ]="none"
        
        if (rx.__class__.__name__=='list'):
            lparms[ "rx" ]=str(rx[0])
            lparms[ "ry" ]=str(rx[0])
            svg=self.XML_Tag1("ellipse",lparms)
        else:
            lparms[ "r" ]=str(rx)
            svg=self.XML_Tag1("circle",lparms)
        
        return svg
    
    #### Drawing a Vector

    def SVG_Vector_Arrow_Calc(self,px1,px2,flip=False):
        v=px2-px1
        if (v.Length()==0.0): return v

        v=v.Normalize()
        n=v.Hat2()*self.NScale
        v*=self.VScale
        if (flip):
            v*=-1.0

        return [px2,px2-v+n,px2-v-n,px2]
        
    #### Drawing a Vector

    def SVG_Vector_Arrow_SVG(self,px1,px2,color,thick,parms={}):
        lparms=self.SVG_Parms(parms)

        lparms[ "style" ][ "stroke" ]=color
        lparms[ "style" ][ "fill" ]=color
        return self.SVG_Polyline(
            self.SVG_Vector_Arrow_Calc(px1,px2),
            color,
            thick,
            lparms
        )
        
    def SVG_Vector(self,px1,px2,color,thick=1,parms={}):
        lparms=self.SVG_Parms(parms)
        
        #lparms[ "style" ][ "stroke" ]=color
        #lparms[ "style" ][ "stroke-width" ]=self.SVG_Thickness(thick)
        #lparms[ "style" ][ "fill" ]=color
        
        return [
            self.SVG_Line(px1,px2,color,thick,lparms),
            self.SVG_Vector_Arrow_SVG(px1,px2,color,thick,parms),
        ]
    
    def SVG_Image(self,image,height,width,x=None,y=None,parms={}):
        lparms=self.SVG_Parms(parms)
        if (x==None): x=0
        if (y==None): y=0

        lparms[ "x" ]=x
        lparms[ "y" ]=y
        lparms[ "height" ]=height
        lparms[ "width" ]=width
        lparms[ "xlink:href" ]=image

        del lparms[ "style" ]
        return self.XML_Tag1("image",lparms)
    
    def SVG_Images(self,images,height,width,x=None,y=None,parms={}):
        svg=[]
        for image in images:
            svg.append(
                self.SVG_Image(image,height,width,x,y,parms)
            )
            
        return svg

    
    def SVG_Group(self,id,svg,cls="",desc=None,parms={}):
        lparms=self.SVG_Parms(parms)

        lparms[ "id" ]=id

        return self.XML_Tags("g",svg,lparms)
