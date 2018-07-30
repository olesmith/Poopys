import re,sys

from Circle       import Circle
from Ellipsis     import Ellipsis
from Descartes    import Descartes
from Rose         import Rose
from Parabola     import Parabola
from Hyperbola    import Hyperbola
from Super        import Super
from Cycloid      import Cycloid
from Trochoid     import Trochoid
from Epicycloid   import Epicycloid
from Epitrochoid  import Epitrochoid
from Hypocycloid  import Hypocycloid
from Hypotrochoid import Hypotrochoid


from Parallel     import Parallel
       
class Curves2_Names():
    def Curves2_Curve(self,name=None):
        if (not name): name=self.Curves2_Name()

        self.Calc=True
        if (name=="Circle"):
            self.Curve=Circle()
        elif (name=="Parabola"):
            self.Curve=Parabola()
        elif (name=="Ellipsis"):
            self.Curve=Ellipsis()
        elif (name=="Hyperbola"):
            self.Curve=Hyperbola()
        elif (name=="Descartes"):
            self.Curve=Descartes()
        elif (name=="Rose"):
            self.Curve=Rose()
        elif (name=="Superellipse"):
            self.Curve=Super()
        elif (name=="Cycloid"):
            self.Curve=Cycloid()
        elif (name=="Trochoid"):
            self.Curve=Trochoid()
        elif (name=="Hypocycloid"):
            self.Curve=Hypocycloid()
        elif (name=="Hypotrochoid"):
            self.Curve=Hypotrochoid()
        elif (name=="Epicycloid"):
            self.Curve=Epicycloid()
        elif (name=="Epitrochoid"):
            self.Curve=Epitrochoid()
        elif (name=="Super"):
            self.Curve=Super()

            
        elif (name=="LatexTables"):
            self.Latex_Curves_Table_Generate()
            
        elif (name=="Parallel"):
            self.Curve=Parallel()
            self.Curve.Base_Curve()

            self.Curve.Run()
        else:
            self.Calc=False

        self.Name=name

        if ( self.Curves2_Args() ):
            self.Calc=False

        return self.Curve
        
    def Curves2_Names(self):
        return [
            "Circle",
            "Parabola",
            "Ellipsis",
            "Hyperbola",
            "Superellipse",
            "Cycloid",
            "Trochoid",
            "Hypocycloid",
            "Hypotrochoid",
            "Epicycloid",
            "Epitrochoid",
            "Descartes",
            "Rose",
            "Super",
            "Parallel",
            "LatexTables",
        ]
    
    
    def Curves2_Name(self):
        curve=None
        if (self.CGI_Is()):
            curve=self.CGI_GET_Get("Curve")
        else:
            if (len(sys.argv)>1 and re.search( self.Curves2_Regex()+'$',sys.argv[1])):
                curve=sys.argv[1]
            
        return curve
