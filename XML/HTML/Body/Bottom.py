
class HTML_Body_Bottom():
    ##! 
    ##! Generates Bottom row left cell.
    ##!
    

    def HTML_Bottom_Left(self):
        html=[]
        args={
            "src": self.HTML_Bottom_Logos[0],
            "align": "center",
            "height": "100px",
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    ##! 
    ##! Generates Bottom row center cell.
    ##!
    
    def HTML_Bottom_Center(self):        
        html=[]
        args={
            "src": self.HTML_Bottom_Logos[1],
            "align": "center",
            "height": "100px",
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    ##! 
    ##! Generates Bottom row right cell.
    ##!
    
    def HTML_Bottom_Right(self):
        html=[]
        args={
            "src": self.HTML_Bottom_Logos[2],
            "align": "center",
            "height": "100px",
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    
    
