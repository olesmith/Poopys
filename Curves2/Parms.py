            
class Curves2_Parms():
    def Parms1(self,parms):
        rparms=[]
        for parms0 in parms[0]:
            rparms.append( [parms0] )
        return rparms
    
    def Parms2(self,parms):
        rparms=[]
        for parms0 in parms[0]:
            for parms1 in parms[1]:
                rparms.append( [parms0,parms1] )
        return rparms
    
    def Parms3(self,parms):
        rparms=[]
        for parms0 in parms[0]:
            for parms1 in parms[1]:
                for parms2 in parms[2]:
                    rparms.append( [parms0,parms1,parms2] )
        return rparms
    
    def Parms4(self,parms):
        rparms=[]
        for parms0 in parms[0]:
            for parms1 in parms[1]:
                for parms2 in parms[2]:
                    for parms3 in parms[3]:
                        rparms.append( [parms0,parms1,parms2,parms3] )
        return rparms
    
    def Parms(self):
        parms=self.Curve.Curve_Parameters()
        if ( len(parms)==1):
            parms=self.Parms1(parms)
        elif ( len(parms)==2):
            parms=self.Parms2(parms)
        elif ( len(parms)==3):
            parms=self.Parms3(parms)
        elif ( len(parms)==4):
            parms=self.Parms4(parms)
             
        return parms
    
    def Curve_Parms_HTML(self):
        parms=self.Curve.Curve_Parameters()
        parmnames=self.Curve.Curve_Parameter_Names()

        
        html=[]
        for n in range( len(parms) ):
            row=[  self.B(parmnames[n])  ]
            
            rparms=[]
            rrparms=[]
            for parm in parms[n]:
                rrparms.append(str(parm))
                if ( len(rrparms)>5 ):
                    rparms.append( ", ".join(rrparms) )
                    rrparms=[]


            if ( len(rrparms)>0 ):
                rparms.append( ", ".join(rrparms) )
                        
            row.append( ",<BR>".join(rparms) )
            html.append(row)

        return self.Center(
            self.HTML_Table(
                html,
                [
                    "Parameter","Values",
                ],
                [],
                {
                    "border": "1px",
                    "align": "center",
                }
            )
        )
