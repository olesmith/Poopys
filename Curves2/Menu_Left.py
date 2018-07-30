class Curves2_Menu_Left():
    Curve=None
    def Curves2_Left_Menu000000000(self):
        return self.HTML_List( self.Curves2_Links() )

    def HTML_Left_Menu_Link(self,curvename):
        if (curvename==self.Name): return curvename
        
        return self.A("?Curve="+curvename,curvename)
        
    def HTML_Left_Menu(self):
        html=[
            self.H(5,"Planar Curves")
        ]

        items=[]
        for curvename in self.Curves2_Names():
            items.append(  self.HTML_Left_Menu_Link(curvename)  )

        html.append( self.HTML_List(items) )
        return html

    
    def Curves2_Link(self,name):
        args={
            "Comp": "Curves2",
            "Name": name,
        }
        
        url="?"+self.CGI_Args2URL(args)
        return self.A(url,name)
    
    def Curves2_Links(self):
        html=[]
        for name in self.Curves2_Names():
            html.append( self.Curves2_Link(name) )
            
        return html
    
    def Curves2_Left_Menu(self):
        return self.HTML_List( self.Curves2_Links() )
    
    def Curves2_Regex(self):
        return "("+   "|".join( self.Curves2_Names() )  +")"
