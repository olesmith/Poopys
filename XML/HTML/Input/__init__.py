from Select import HTML_Input_Select

class HTML_Input(
        HTML_Input_Select
    ):
    def HTML_Radios(self,fieldname,values,value="",valuenames=[],options={}):
        if (not valuenames): valuenames=values
        
        radios=[]
        
        roptions=dict(options)
        roptions[ "type" ]="radio"
        roptions[ "name" ]=fieldname
        
        for i in range( len(values) ):
            roptions[ "value" ]=values[i]
            radios.append(
                valuenames[i]+": "+
                self.XML_Tag(
                    "INPUT",
                    roptions
                )
            )

        return radios
    
    def HTML_Color(self,fieldname,color=None,options={}):
        roptions=dict(options)
        
        roptions[ "name" ]=fieldname
        roptions[ "type" ]="color"
        if (color is not None):
            roptions[ "value" ]=color

        return self.XML_Tag(
            "INPUT",
            roptions
        )
 
    def HTML_Hidden(self,fieldname,value,options={}):
        roptions=dict(options)
        
        roptions[ "name" ]=fieldname
        roptions[ "type" ]="hidden"
        roptions[ "value" ]=value
        return self.XML_Tag(
            "INPUT",
            roptions
        )
    
    def HTML_Check(self,fieldname,checked=False,value=1,options={}):
        roptions=dict(options)
        
        roptions[ "name" ]=fieldname
        roptions[ "type" ]="checkbox"
        roptions[ "value" ]=value
        
        if (checked): roptions[ "checked" ]=""
        
        return self.XML_Tag(
            "INPUT",
            roptions
        )
    
    def HTML_Button(self,btype="submit",title="GO",options={}):
        roptions=dict(options)
        
        roptions[ "type" ]=btype
        return self.XML_Tags(
            "BUTTON",
            title,
            roptions
        )
