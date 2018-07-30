
class HTML_Body_Top():
    ##! 
    ##! Generates TOP row left cell.
    ##!
    
    def HTML_Top_Left(self):
        html=[]
        args={
            "src": self.HTML_Top_Logos[0],
            "height": "100px",
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    ##! 
    ##! Generates TOP row center cell.
    ##!
    
    def HTML_Top_Center(self):
        html=[]

        html=html+self.Hs(self.HTML_Titles)
        
        return html

    
    ##! 
    ##! Generates TOP row left cell.
    ##!
    
    def HTML_Top_Right(self):
        html=[]

        args={
            "src": self.HTML_Top_Logos[1],
            "height": "100px",
        }

        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html
