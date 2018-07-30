
class HTML_Input_Options(
    ):
    def HTML_Select_Option_Selected_Is(self,value,currvalues):
        if (currvalues.__class__.__name__!="list"):
            currvalues=[currvalues]

        selected=False
        if (value is not None):
            for ival in currvalues:                
                if (str(value)==str(ival)):
                    selected=True
                    break

                    
        return selected
    
    def HTML_Select_Option_Options(self,value,valuetitle,currvalues,options):
        if (currvalues.__class__.__name__=="str"):
            currvalues=[currvalues]

        roptions=dict(options)
        roptions[ "value" ]=value
        if (valuetitle):
            roptions[ "title" ]=valuetitle

        if (self.HTML_Select_Option_Selected_Is(value,currvalues)):
            roptions[ "selected" ]=""

        return roptions
        
    def HTML_Select_Option(self,value,valuename,valuetitle,currvalues,ooptions):
        return self.XML_Tags(
            "OPTION",
            valuename,
            self.HTML_Select_Option_Options(value,valuetitle,currvalues,ooptions)
         )
 
