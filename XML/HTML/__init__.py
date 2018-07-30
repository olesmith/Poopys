import time

from CGI  import CGI
from File import *

from Tags     import HTML_Tags
from Table    import HTML_Table

from Head     import HTML_Head
from Body     import HTML_Body
from Messages import HTML_Messages
from Input     import HTML_Input

class XML_HTML(
        CGI,
        HTML_Tags,
        HTML_Table,
        HTML_Head,
        HTML_Body,
        HTML_Messages,
        HTML_Input
    ):

    #Controls whether we are a Cell phone or not
    HTML_Cell_Mode=False
    HTML_Start=0
    
    HTML_Messages=[]
    HTML_Version="<!DOCTYPE html>"
    HTML_Title="PooPys"
    HTML_Titles=[
        "PooPys",
        "Computational and Differential Geometry",
        "Instituto de Matem&aacute;tica e Estat&iacute;stica",
        "Universidade Federal de Goi&aacute;s",
        "Prof. Ole Peter Smith"
    ]
 
    HTML_Icons="/icons"
    HTML_CSSs=[ "/W3.css","/Poops.css", ]
    HTML_METAs=[
        {
            "http-equiv": "Content-type",
            "content": "text/html; charset=utf-8",
        },
        {
            "name": "Autor",
            "content": "Prof. Dr. Ole Peter Smith, IME/UFG",
        },
    ]

    #Names of Methods to call to generate Body matrix/table
    HTML_Body_Matrix=[
        [ "Top_Left","Top_Center","Top_Right", ],
        [ "Middle_Left","Middle_Center","Middle_Right", ],
        [ "Bottom_Left","Bottom_Center","Bottom_Right", ],
    ]
    
    #Body table row classes
    HTML_Body_TR_CSS=[
        "Top","Middle","Bottom"
    ]
    HTML_Body_TD_CSS=[
        "Left","Center","Right"
    ]
    
    #Body table row classes
    HTML_Body_Matrix_TR_CSS=[
        "Body_Top","Body_Middle","Body_Bottom"
    ]
    
    #Body table column classes
    HTML_Body_Matrix_TD_CSS=[
        "Body_Left","Body_Center","Body_Right",
    ]

    HTML_Top_Logos=[
        "/icons/ufg.png",
        "/icons/cora.png"
    ]
    
    HTML_Bottom_Logos=[
        "/icons/sade_owl1.png",
        "/icons/kierkegaard.png",
        "/icons/sade_owl2.png"
    ]
    HTML_Middle_Right_Logos=[ 
        {
            "Name": "PooPys",
            "Url": "poop2.png",
            "Height": "",
            "URL": "/cgi-bin/Display",
        },
        {
            "Name": "Python",
            "Url": "python.jpg",
            "Width": "75px",
            "URL": "http://www.python.org",
        },
        {
            "Name": "SVG",
            "Url": "svg.jpg",
            "Width": "75px",
            "URL": "http://www.w3.org/Graphics/SVG",
        },
        {
            "Name": "Latex",
            "Url": "latex.png",
            "Width": "75px",
            "URL": "http://www.latex-project.org",
        },
        {
            "Name": "GreaseMonkey",
            "Url": "greasemonkey.png",
            "Width": "75px",
            "URL": "http://www.greasemonkey.net",
        },
        {
            "Name": "W3Schools",
            "Url": "w3.jpg",
            "Width": "75px",
            "URL": "http://www.w3schools.com",
        },
        {
            "Name": "Inkscape",
            "Url": "inkscape.png",
            "Width": "75px",
            "URL": "http://www.inkscape.org",
        },
        {
            "Name": "Gimp",
            "Url": "gimp.jpg",
            "Width": "75px",
            "URL": "http://www.gimp.org",
        },
        {
            "Name": "Geogebra",
            "Url": "geogebra.png",
            "Width": "75px",
            "URL": "http://www.geogebra.org",
        },
    ]
    
    def HTML_Doc_Generate(self):
        html=[]

        self.HTML_Message_Init()
    
        html=html+self.HTML_Header()
        html=html+self.HTML_Body()
        html=html+self.HTML_Tailer()
        

        return self.HTML_Print(html)

    def Run(self):
        self.CGI_HTTP_Header_Print()

        print self.HTML_Doc_Generate()

    
    ##! 
    ##! Generates HTML Header end section: Just BODY and HTML end tag.
    ##!
    
    def HTML_Tailer(self):
        html=[]
        html=html+[ self.XML_Tag_End("HTML") ]

        return html
    
    ##! 
    ##! Prints HTML list hierarchy.
    ##!
    
    def HTML_Print(self,htmls,level=0):
        return self.XML_Print(htmls,level)

    ##!
    ##! Makes sure that options[ "class" ] is set
    ##* make it list
    ##* and add classs to it.
    ##!
    
    def HTML_AddClass(self,classs,options={}):
        roptions=dict(options)
        if (not roptions.has_key("class")):
            roptions[ "class" ]=[]
            
        if (roptions[ "class" ].__class__.__name__!="list"):
            roptions[ "class" ]=[ roptions[ "class" ] ]
        
        roptions[ "class" ].append(classs)
        return roptions
    
