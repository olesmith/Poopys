
class Curve_Screen_Caroussel():
    
    #!
    #! Permute 2
    #!
    
    def Curve_Parameters_Permute(self,list1,list2):
        perms=[]
        for item1 in list1:
            if (item1.__class__.__name__!='list'):
                item1=[item1]
                
            for item2 in list2:
                if (item2.__class__.__name__!='list'):
                    item2=[item2]
                    
                perms.append( item1+item2 )
                
        return perms
    
                
        
    #!
    #! Generate the central curve animation screen.
    #!
    
    def Curve_Parameters_Caroussel(self):
        parms=self.Curve_Parameters_CGI_Get()
        print parms,"Parms<BR>"

        pkeys=self.Curve_Parameter_Names()
        
        parms0=parms[ pkeys[0] ]
        parms1=parms[ pkeys[1] ]

        perms=self.Curve_Parameters_Permute(parms0,parms1)
        for i in range(2,len(pkeys)):
            perms=self.Curve_Parameters_Permute(perms,parms[ pkeys[i] ] )


        images=[]
        for perm in perms:
            paths=[
                self.Curve_BasePath,
                self.Name,
            ]
            
            for parm in perm:
                parm=float(parm)
                parm="%.6f" % parm
                paths.append( parm )

            paths.append( str(self.N) )
            name="/".join(paths)
            print name,"<BR>"
        print perms,"perms2<BR>"

        
        return perms
