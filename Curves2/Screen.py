            
class Curves2_Screen():
    
    def Curves2_Screen(self):
        self.CGI_HTTP_Header_Print()
        
        print self.HTML_Print(  [ self.HTML_Doc_Generate()]  )

    def HTML_Central_Screen(self):
        html=[]
        if (not self.Name):
            html.append( self.H(2,"Select Curve Family in Leftmenu") )
        elif (self.Curve):
            html=self.HTML_Curve_Screen()
        return html
    
    def HTML_Curve_Screen(self):
        html=self.Curve.Curve_Screen()
            
        return html 

    
