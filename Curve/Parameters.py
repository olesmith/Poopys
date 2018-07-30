

class Curve_Parameters():       
    #!
    #! Generate the central curve screen parameters selection table.
    #!
    
    def Curve_Parameters_Form(self):
        return [
            self.HTML_Form
            (
                "?"+self.CGI_ENV_Get("QUERY_STRING"),
                self.Center([
                        self.Curve_Parameters_Table(),
                        self.HTML_Button()
                ])
            )
        ]
   

    #!
    #! Generate the central curve screen parameters table.
    #!
    
    def Curve_Parameters_Table(self):
        return [
            self.H(4,"Curve Parameters"),
            self.HTML_Table(
                [
                    self.Curve_Parameters_Row()
                ],
                self.Curve_Parameters_Title_Row(),
                [],
                {
                    "frame": 'border',
                    "class": "Parms_Table",
                }
            )
        ]
    
    #!
    #! Returns name of i'th parameter.
    #!
    
    def Curve_Parameter_Name_Get(self,i):      
        names=self.Curve_Parameter_Names()
        
        name=None
        if (len(names)>i):
            name=names[i]
            
        return name
    
    #!
    #! Returns possible values of i'th parameter
    #!
    
    def Curve_Parameter_Values_Get(self,i):      
        valuess=self.Curve_Parameters()
        
        values=None
        if (len(valuess)>i):
            values=valuess[i]
            
        return values

    #!
    #! Generates parameters table title row.
    #!
    
    def Curve_Parameters_Title_Row(self):      
        parameternames=self.Curve_Parameter_Names()
        
        titles=[]
        for i in range ( len(parameternames) ):
            titles.append([
                self.B(parameternames[i])
            ])
        return titles

    #!
    #! Generate parameters row.
    #!
    
    def Curve_Parameters_Row(self):      
        parameters=self.Curve_Parameters()
        parameternames=self.Curve_Parameter_Names()
        
        row=[]
        for i in range ( len(parameternames) ):
           row.append([
                self.Curve_Parameter_Select(i,parameternames[i],parameters[i]),
            ])

        return row
    
    #!
    #! Generate parameter select field.
    #!
    
    def Curve_Parameter_Select(self,i,parametername,values,options={}):
        if (values.__class__.__name__!='list'):
            values=[values]
            
        value=self.Curve_Parameter_CGI_Get(i,parametername,values)
        
        roptions=dict(options)
        roptions[ "multiple" ]=""
        roptions[ "size" ]=10 #len(values)

        return self.HTML_Select(parametername,values,value,[],[],roptions)

    
    #!
    #! Get curve parameterkey from CGI or default.
    #!
    
    def Curve_Parameter_CGI_Get(self,i,parametername,values):
        #Read directly from CGI
        name=self.Curve_Parameter_Name_Get(i)
        value=self.CGI_POST_Get(parametername)

        values=self.Curve_Parameter_Values_Get(i)
        
        if (len(values)>=1 and not value):
            value=values[0]

        return value
     
    #!
    #! Generate parameters row.
    #!
    
    def Curve_Parameters_CGI_Get(self):      
        parameters=self.Curve_Parameters()
        parameternames=self.Curve_Parameter_Names()

        values={}
        for i in range ( len(parameternames) ):
            ivalues=self.Curve_Parameter_Values_Get(i)
            pvalues=self.Curve_Parameter_CGI_Get(i,parameternames[i],ivalues)
            if (pvalues.__class__.__name__!='list'):
                pvalues=[pvalues]
                
            values[ parameternames[i] ]=pvalues
            
        return values
    
    #!
    #! Take curve parameters from CGI.
    #!
    
    def Curve_Parameters_CGI_Set(self):
        for parameterkey in self.Curve_Parameter_Keys():
            
            value=self.CGI_POST_Get(parameterkey)
            if (value):
                try:
                    value=float(value)
                except ValueError:
                    err=1

                setattr(self,parameterkey,value)
                value=getattr(self,parameterkey)
    
    
