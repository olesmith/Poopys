
class HTML_Head():
   ##! 
    ##! Generates HTML Header section: everything untill just before <BODY>
    ##!
    
    def HTML_Header(self):
        html=[]
        
        html.append( self.HTML_Version )
        html.append( self.XML_Tag_Start("HTML") )
        
        html.append( self.HTML_Head() )

        return html

    ##! 
    ##! Generates HTML HEAD section:
    ##!
    ##! - META headers
    ##! - LINKs
    ##! - SCRIPT
    ##! - STYLE
    ##!
    
    def HTML_Head(self):
        
        html=[]
        html=html+ [ self.XML_Tag_Start("HEAD") ]

        rhtml=[]
        rhtml=rhtml+self.HTML_Head_Title()
        rhtml=rhtml+self.HTML_Head_METAs()
        rhtml=rhtml+self.HTML_Head_CSSs()
        rhtml=rhtml+self.HTML_Head_Script()
        
        html=html+[ rhtml ]
        html=html+[ self.XML_Tag_End("HEAD") ]

        return html

     
    ##! 
    ##! Generates HTML META section:
    ##!
    
    def HTML_Head_Title(self):

        return [ self.XML_Tags("TITLE",self.HTML_Title) ]

    ##! 
    ##! Generates HTML CSS section:
    ##!
    
    def HTML_Head_CSSs(self):
        html=[]

        args={
            "rel": "stylesheet",
        }
        
        for css in self.HTML_CSSs:
            args[ "href" ]=css
            html=html+[ self.XML_Tag_Start("LINK",args) ]

        return html

     
    ##! 
    ##! Generates HTML META tags section:
    ##!
    
    def HTML_Head_METAs(self):
        html=[]
        
        for meta in self.HTML_METAs:
            html=html+[ self.XML_Tag_Start("META",meta) ]

        return html

    ##! 
    ##! Generates HTML SCRIPT section:
    ##!
    
    def HTML_Head_Script(self):
        html=[]
        html=html+[ self.XML_Tag_Start("SCRIPT") ]
        html=html+[ self.XML_Tag_End("SCRIPT") ]

        return html
