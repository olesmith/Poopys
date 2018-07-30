from Canvas2 import Canvas2


class Curve_Types():
    
    def Curve_Types_Derivatives(self):
        return [
            #Derivatives
            "dR","d2R","d3R","VN",
        ]
    def Curve_Types_Frenet(self):
        return [
            #Frenet and velocity normal
            "T","N",
        ]
    def Curve_Types_Functions(self):
        return [
            #Scalar quantities
            "v2",
            "Det",
            "S",
            "Phi",
            "Psi",#"dPsi",
            "Kappa",
            "Rho",
        ]
    def Curve_Types_dFunctions(self):
        return [
            #Scalar quantities
            "dv2",
            "dDet",
            "dPhi",
            #"dPsi",
            "dKappa",
            "dRho"
        ]
    def Curve_Types_Vectors(self):
        return [
            #Frenet and velocity normal
            "RhoV",
        ]
       
    def Curve_Types_Evolutes(self):
        return [
            #Evolute and evolute derivative
            "Evolute","dEvolute",
        ]
    
    def Curve_Types_Singulars(self):
        return [
            #Singular points for curve and evolute
            #"Evolute","dEvolute",
        ]
    
    def Curve_Types_Calc(self):
        types=[]
        types=types+self.Curve_Types_Verify()
        types=types+self.Curve_Types_Singulars()
        
        return types

    def Curve_Types_Verify(self):
        types=[]
        types=types+self.Curve_Types_Derivatives()
        types=types+self.Curve_Types_Frenet()
        types=types+self.Curve_Types_Functions()
        types=types+self.Curve_Types_dFunctions()
        types=types+self.Curve_Types_Vectors()
        types=types+self.Curve_Types_Evolutes()
        
        return types

    def Curve_Types_Deviations(self):
        return self.Curve_Types_Verify()

    def Curve_Types_SVG(self):
        types=["R"]
        types=types+self.Curve_Types_Derivatives()
        types=types+self.Curve_Types_Frenet()
        types=types+self.Curve_Types_Evolutes()
        types=types+self.Curve_Types_Vectors()
        types=types+self.Curve_Types_Functions()
        types=types+self.Curve_Types_dFunctions()
        
        return types

    def Curve_Meshes(self):
        types=["R"]
        #types=types+self.Curve_Types_Derivatives()
        types=types+self.Curve_Types_Frenet()
        types=types+self.Curve_Types_Evolutes()
        
        return types

        
    def Curve_Type_Has_Analytical(self,ttype):
        rtype=ttype
        if (ttype=="T"): rtype="t"
        elif (ttype=="N"): rtype="n"

        res=False
        if ( hasattr(self,rtype) ):
            res=True

        return res

    def Curve_Types_Get(self,ttype):
        dtypes=["Num"]
        if (self.Curve_Type_Has_Analytical(ttype)):
            dtypes.append("Ana")
            
        return dtypes

            
    ##!
    ##! Runs method (ex Calc) for ttype and ctype:
    ##!
    ##!    Num(erical)
    ##!    Ana(lytical)
    ##!
    ##! Ie, excutes:
    ##!
    ##!   method+"_Num_"+ttype+"s"
    ##!
    ##! And, if defined: self.Curve_Type_Has_Analytical(ttype):
    ##!   method+"_Ana_"+ttype+"s"
    ##!
    ##!
    
    def Curve_Run_Method_Types(self,method,ttype,tell=False):
        rmethod=method+"_Num_"+ttype+"s"

        if (tell): print "<BR>Curve_Run_Method_Types Num:",rmethod+"<BR>",tell
        self.__Call_Method__(rmethod,[],tell)
        
        if (tell): print "<BR>Curve_Run_Method_Types Num:",rmethod+"<BR>",tell
        
        if (  self.Curve_Type_Has_Analytical(ttype)  ):
            rmethod=method+"_Ana_"+ttype+"s"
            if (tell): print "<BR>Curve_Run_Method_Types Ana:",rmethod+"BR>"
            self.__Call_Method__(rmethod,[],tell)
        
    ##!
    ##! Runs method (ex Verify) for ttype:
    ##! Ie, excutes:
    ##!
    ##!   method+"_"+ttype+"s"
    ##!
    
    def Curve_Run_Method_Type(self,ttype,method,tell=False):
        text=[]
        if (  self.Curve_Type_Has_Analytical(ttype)  ):
            rmethod=method+"_"+ttype+"s"

            if (tell): print "<BR>Curve_Run_Method_Type:",rmethod+"<BR>"
            text=text+[   self.__Call_Method__(rmethod,tell)   ]
            
        return text

            
        
