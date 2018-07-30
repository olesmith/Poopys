
class HTML_Body_Middle():
    ##! 
    ##! Generates Middle row left cell: Left navigation menu.
    ##!
    
    def HTML_Middle_Left(self):
        return ["&nbsp;"+self.Anchor("TOP")]+self.HTML_Left_Menu()

    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def HTML_Middle_Center(self):
        return self.HTML_Central_Screen()

    ##! 
    ##! Generates Middle row right cell.
    ##!
    
    def HTML_Middle_Right(self):
        imgs=[]
        for logo in self.HTML_Middle_Right_Logos:
            url="/".join([ self.HTML_Icons,logo[ "Url" ] ])

            
            imgoptions={}
            imgoptions[ "src" ]=url
            imgoptions[ "title" ]=logo[ "Name" ]
            if (logo.has_key("Width")):
                imgoptions[ "width" ]=logo[ "Width" ]
            if (logo.has_key("Height")):
                imgoptions[ "height" ]=logo[ "Height" ]
            
            img=self.XML_Tag1("IMG",imgoptions)

            aoptions={}
            aoptions[ "target" ]="__blank"
            
            imgs.append( [ [ self.Center(self.A(logo[ "URL" ],img,aoptions)) ] ] )
                         
        html=[ self.HTML_Messages_Show() ]
        
        html=html+self.XML_Tags("CENTER",[ self.HTML_Table(imgs) ])

        return html
