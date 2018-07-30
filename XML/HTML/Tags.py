import re


class HTML_Tags():
    Default_Anchor="TOP"
    
    def A(self,url,content,options={},title=""):
        options[ "href" ]=url+"#"+self.Default_Anchor
        if (title):
            options[ "title" ]=title
            
        return self.XML_Tag("A",options)+content+self.XML_Tag_End("A")
    
    def Anchor(self,anchor,options={}):
        options[ "name" ]=anchor
        return self.XML_Tag("A",options)+self.XML_Tag_End("A")
    

    def B(self,contents,options={}):
        roptions=self.HTML_AddClass("B",options)

        if (contents.__class__.__name__!='list'):
            contents=[ contents ]

        html=[]
        for content in contents:
            html.append(
                self.XML_Tags("SPAN",content,roptions)
            )

        return html
    
    def I(self,content,options={}):
        roptions=self.HTML_AddClass("I",options)
        
        return self.XML_Tags("SPAN",content,roptions)
    
    def U(self,content,options={}):
        roptions=self.HTML_AddClass("U",options)
        
        return self.XML_Tags("SPAN",content,roptions)
    
    def Center(self,content,options={}):
        roptions=self.HTML_AddClass("Center",options)
        
        return self.XML_Tags("CENTER",content,roptions)
    
    def IMG(self,img,alttext="",options={}):
        options[ "src" ]=img
        
        return self.XML_Tag_Start("IMG",options)
    
    ##! 
    ##! Create title tag <Hn>
    ##!
    
    def H(self,n,title,options={}):
        roptions=self.HTML_AddClass("H"+str(n),options)
        
        return self.XML_Tags("DIV",title,roptions)
    
    ##! 
    ##! Create list of title tags: H1,H2,...
    ##!
    
    def Hs(self,titles,options={}):
        for n in range( len(titles) ):
            titles[n]=self.H(n+1,titles[n],options)
            
        return titles

    def BR(self,options={}):
        return self.XML_Tag_Start("BR",options)
    
    def HR(self,options={}):
        return self.XML_Tag_Start("HR",options)
    
    def Span(self,content,options={}):
        return self.XML_Tags("SPAN",content,options)
    
    def Div(self,content,options={}):
        return self.XML_Tags("DIV",content,options)
    
    def IFrame(self,url,options={}):
        options[ "src" ]=url
        return self.XML_Tags("IFRAME","",options)
    def HTML_List_Old(self,items,options={},lioptions={}):
        items=self.XML_Tags_List("LI",items,lioptions)

        return self.XML_Tags(
            "UL",
            "\n".join(items)+"\n",
            options
        )
    
        

    
    def HTML_List(self,items,ul="UL",options={},lioptions={}):
        html=[]
        html=html+[ self.XML_Tag_Start(ul,options) ]

        rhtml=[]
        for item in items:
            rhtml=rhtml+[ self.XML_Tags("LI",item,lioptions) ]

        html=html+[ rhtml ]
        html=html+[ self.XML_Tag_End(ul) ]
        
        return html
    
    def HTML_Frame(self,content):
        return self.XML_Tags(
            "CENTER",
            self.XML_Tags(
                "TABLE",
                self.XML_Tags(
                    "TR",
                    self.XML_Tags(
                        "TD",
                        content,
                        {
                            "class": "Table_Frame Code",
                        }
                    )
                )
            )
        )

    def HTML_Form(self,action,html,options={},method="post",fileupload=False):
        roptions=dict(options)
        roptions[ "action" ]=action
        roptions[ "method" ]=method
        roptions[ "enctype" ]="multipart/form-data"
        if (fileupload): roptions[ "enctype" ]="application/x-www-form-urlencoded"
        
        html=self.XML_Tags("FORM",html,roptions)

        return [ html ]
            


        
    def HTML_Form_Condicional(self,content,edit=1,action=None,options={},method="post",enctype="multipart/form-data",):

        html=[]
        if (edit==1):
            roptions=dict(options)

            roptions[ "method" ]=method
            roptions[ "enctype" ]=enctype

            if (action is None):
                args=self.CGI_GET_Get()
                action=self.CGI_Args_2_Url(args)
                
            roptions[ "action" ]=action
            
            html.append(
                self.XML_Tag("FORM",roptions)
            )

        html.append([ content])
        if (edit==1):
            html.append(
                self.XML_Tag("/FORM")
            )

        return html
        
        
