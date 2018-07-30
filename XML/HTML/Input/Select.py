import re

from Options     import HTML_Input_Options

class HTML_Input_Select(
        HTML_Input_Options
    ):
    def HTML_Select(self,fieldname,values,currvalue="",valuenames=[],valuetitles=[],options={},ooptions={}):
        if (not valuenames): valuenames=values

        if (currvalue.__class__.__name__=="str"):
            currvalue=re.sub('^\s+',"",currvalue)
            currvalue=re.sub('\s+$',"",currvalue)
            
        rhtml=[]
        for n in range(  len(values)  ):
            valuetitle=None
            if (len(valuetitles)>n):
                valuetitle=valuetitles[n]
                
            rhtml.append(
                self.HTML_Select_Option(values[n],valuenames[n],valuetitle,currvalue,ooptions)
           )

        return [
            self.XML_Tag_Start(
                "SELECT",
                self.HTML_Select_Options_Get(fieldname,options)
            ),
            rhtml,
            self.XML_Tag_End("SELECT")
        ]
            
        html=html+[ self.XML_Tag_End("SELECT") ]

        return html

    def HTML_Select_Options_Get(self,fieldname,options):
        roptions=dict(options)
        roptions[ "name" ]=fieldname

        return roptions
        
       
