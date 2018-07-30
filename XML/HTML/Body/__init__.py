from Top    import HTML_Body_Top
from Middle import HTML_Body_Middle
from Bottom import HTML_Body_Bottom

class HTML_Body(
        HTML_Body_Top,
        HTML_Body_Middle,
        HTML_Body_Bottom
    ):
    ##! 
    ##! Generates HTML BODY.
    ##!
    
    def HTML_Body(self):
        html=[]
        html=html+[ self.XML_Tag_Start("BODY") ]
        html=html+[ self.HTML_Body_Generate() ]
        html=html+[ self.XML_Tag_End("BODY") ]

        return [html]
    
    ##! 
    ##! Generates HTML BODY.
    ##!
    
    def HTML_Body_Generate(self):
        args={
            "class": "Body_Table",
        }
        
        html=[]
        html=html+[ self.XML_Tag_Start("TABLE",args) ]

        n=0
        rhtml=[]
        for cellmethods in self.HTML_Body_Matrix:
            rhtml=rhtml+[ self.HTML_Body_Row(n) ]         
            n+=1

        html=html+[ rhtml ]
        html=html+[ self.XML_Tag_End("TABLE") ]

        if (self.HTML_Cell_Mode):
            html=[ self.XML_Tag_Start("FONT",{"size": "+5", }) ]+html+[ self.XML_Tag_End("FONT") ]
        
        return html

    ##! 
    ##! Generates HTML BODY row no n.
    ##!
    
    def HTML_Body_Row(self,n):
        m=0
        args={
            "class": self.HTML_Body_Matrix_TR_CSS[ n ],
        }
                
        html=[ self.XML_Tag_Start("TR",args) ]

        rhtml=[]
        for cellmethod in self.HTML_Body_Matrix[ n ]:
            rhtml=rhtml+[ self.HTML_Body_Row_Cell(n,m) ]

            m+=1
        html=html+[ rhtml ]
        html=html+[ self.XML_Tag_End("TR") ]

        return html
    
    ##! 
    ##! Generates HTML BODY row no n.
    ##!
    
    def HTML_Body_Row_Cell(self,n,m):
        cellmethod="HTML_"+self.HTML_Body_Matrix[ n ][ m ]
        cellcontent=cellmethod+": undef"
        if ( hasattr(self,cellmethod) ):
            method=getattr(self,cellmethod)
            cellcontent=method()

        klass=" ".join([
            self.HTML_Body_Matrix_TR_CSS[ n ],
            self.HTML_Body_Matrix_TD_CSS[ m ],
            ])
        klass="_".join([
            "Body",
            self.HTML_Body_TR_CSS[ n ],
            self.HTML_Body_TD_CSS[ m ]
        ])
        args={
            "class": klass,
        }
                
        html=[ self.XML_Tag_Start("TD",args) ]
        html=html+[ cellcontent ]
        html=html+[ self.XML_Tag_End("TD") ]

        return html
    
    ##! 
    ##! Generates Bottom row left cell.
    ##!
    
  
    def HTML_Bottom000(self):         
        html=[]
        html=html+[ self.XML_Tag_Start("TR") ]   
        
        
        html=html+self.HTML_Cell("Bottom","Left")
        html=html+self.HTML_Cell("Bottom","Center")
        html=html+self.HTML_Cell("Bottom","Right")
        
        html=html+self.HTML_Indent(indent)
        html=html+self.XML_Tag_End("TR")+"\n" 

        return html

    ##! 
    ##! Generates Left menu.
    ##!
    
    def HTML_Left_Menu(self):        
        html=[]
        html=html+[ self.H(3,self.HTML_Title+":") ]

        return html


    ##! 
    ##! Generates central screen.
    ##!
    
    def HTML_Central_Screen(self):
        html=[]
        html=html+[ self.H(3,self.HTML_Title+":") ]

        return html
