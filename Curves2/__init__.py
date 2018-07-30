import re,sys

from XML import XML
#from CGI import CGI

from Curve        import Curve
from Colors import Colors

from Names        import Curves2_Names
from Parms        import Curves2_Parms
from Menu_Left    import Curves2_Menu_Left
from Screen       import Curves2_Screen
from Latex_Tables import Curves2_Latex
from Deviation    import Curves2_Deviation

            
class Curves2(
        Curves2_Names,
        Curves2_Latex,
        Curves2_Parms,
        #Curves2_CGI,
        Curves2_Menu_Left,
        Curves2_Screen,
        Curves2_Deviation,
        XML,
        Colors
    ):
    Curve=None
    Name=None
    Calc=True
    
    def __init__(self,init=True,name=None):
        if (init):
            #We need a copy to retrieve curve types parameters
            self.Curves2_Curve(name)
        
        return

    def Curves2_Args_CLI(self):
        ckeys=self.Curve.Curve_Parameter_Keys()

        keys=[]
        if ( len(sys.argv)>1 ):
            for i in range(2,len(sys.argv)):
                if (i-2<len(ckeys)):
                    keys.append(sys.argv[i])

        for i in range( len(keys) ):
            setattr(self.Curve,ckeys[i],keys[i])

        return keys
    
    def Curves2_Args_CGI(self):
        return []

    
    def Curves2_Args(self):
        if (not self.Curve): return []
        
        ckeys=self.Curve.Curve_Parameter_Keys()

        keys=[]
        if (self.CGI_Is()):
            keys=self.Curves2_Args_CGI()
        else:
            keys=self.Curves2_Args_CLI()

        return keys

    def Run_Parameters2Key(self,parms):
        key=""
        for parm in parms:
            key+= "%.6e" % parm

        return key
    
    def Run_Curves_Calc(self):
        parms=self.Parms()
        
        color2=[255,0,0]
        color1=[0,0,255]
        palette=self.Colors_Generate(len(parms),color1,color2)
        curve=None
        
        svg=[]
        colorno=0
        first=True

        deviations={}
        for cparms in parms:
            curve=self.Curves2_Curve()
            
            curve.Set_Curve_Parameters(cparms)

            key=self.Run_Parameters2Key(cparms)
            
            deviations[ key ]=curve.Run()
            if ( first ):
                #Just to see changes in pdfs and latex first time through
                curve.__Tex__()
                first=False

            colorno+=1
            if (colorno>=len(palette)): colorno=0
            cparms.append(curve.N)

        #Last curve
        if (curve):
            curve.Curve_SVG_Accumulateds(parms)
            
            curve.Run_Curves_Post()
            curve.Curve_Python_Analytical_Codes()
            self.Deviation_Tables_Generate(deviations)
            #Run again
            curve.__Tex__()
        

    def Run(self):
        if (self.CGI_Is()):
            self.Curves2_Screen()
        elif (self.Name):
            self.Run_Curves_Calc()
