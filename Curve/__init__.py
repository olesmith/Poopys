from math import *
import re

from File   import *

from Vector import Vector
from Latex  import Latex
from XML    import XML



from t   import Curve_t
from R   import Curve_R
from dR  import Curve_dR
from d2R import Curve_d2R
from d3R import Curve_d3R
    
from v2  import Curve_v2
from dv2 import Curve_dv2
from T   import Curve_T
from N   import Curve_N
from VN  import Curve_VN

from Det   import Curve_Det
from dDet  import Curve_dDet

from Phi   import Curve_Phi
from dPhi  import Curve_dPhi
from Psi   import Curve_Psi
from dPsi  import Curve_dPsi

from Kappa  import Curve_Kappa
from dKappa import Curve_dKappa
from Rho    import Curve_Rho
from dRho   import Curve_dRho

from RhoV  import Curve_RhoV


from Evolute  import Curve_Evolute
from dEvolute import Curve_dEvolute

from Singular  import Curve_Singular
from Evolute_Singular  import Curve_Evolute_Singular

from s import Curve_S

from Types   import Curve_Types
from Canvas  import Curve_Canvas
from Calc    import Curve_Calc
from Verify  import Curve_Verify
from latex   import Curve_Latex
from Write   import Curve_Write
from SVG     import Curve_SVG
from PDF     import Curve_PDF

from Screen    import Curve_Screen

from Parameters    import Curve_Parameters
from Python    import Curve_Python



class Curve(
        File,
        Latex,
        XML,
        Curve_t,
        Curve_R,
        Curve_dR,
        Curve_d2R,
        Curve_d3R,
        Curve_v2,
        Curve_dv2,
        Curve_T,
        Curve_N,
        Curve_VN,
        Curve_Det,
        Curve_dDet,
        
        Curve_Phi,
        Curve_dPhi,
        Curve_Psi,
        Curve_dPsi,
        
        Curve_Kappa,
        Curve_dKappa,
        Curve_Rho,
        Curve_dRho,
        
        Curve_RhoV,
        Curve_Evolute,
        Curve_dEvolute,
        Curve_S,
        Curve_Singular,
        Curve_Evolute_Singular,
        Curve_Calc,
        Curve_Canvas,
        Curve_Types,
        Curve_Verify,
        Curve_Latex,
        Curve_Write,
        Curve_SVG,
        Curve_PDF,
        Curve_Screen,
        Curve_Parameters,
        Curve_Python
    ):

    Resolution=[800,800]
    
    Name="Curve"
    Title="Curve"
    Curve_BasePaths=["","usr","local","Curves" ]
    Curve_BasePath="/usr/local/Curves"

    Parms=None
    
    N=100
    t1=0.0
    t2=2.0*pi

    eps=1.0E-3
    eps2=None

    __Canvas__=None
    
    Singular_Eps=0.014
    Singular=[]
    Curve_Thickness=3
    Curve_Point_Size=5

    #PDFs and figures tables to generate
    PDFs=[]
    Latex_Figs=[]

    def __init__(self,args={}):
        self.Title="The "+self.Name
        self.__Init__(args)

        return

    
    def __Call_Method__(self,method,args=[],tell=False):
        res=False
        if (tell): print "<BR>__Calc_Method__:",method,args,tell

        if (hasattr(self,method)):
            rmethod=getattr(self,method)
            try:
                res=rmethod()
            except ValueError:
                print "No can do,",rmethod
                
        else:
            print "No such attribute:",method

        if (tell): print "<BR>__Calc_Method__:",method,args
        return res
    
    def __Init__(self,args={}):
        #Default number of points minus 1
        self.N1=self.N-1
        
        self.Show_Points=list()
        
        self.Parms={}
        for key in args.keys():
            setattr(self,key,args[key])

        self.eps2=1.0/(2.0*self.eps)
        
        self.Curve_Init_Parameters()

    #Curve_Deviations: List of parameter values for which to write deviations between
    #analytical and numerical values.
    def Curve_Deviations(self):
        return []
    
        
    def Set_Curve_Parameters(self,parms=[]):
        parmkeys=self.Curve_Parameter_Keys()
        for n in range(  len(parmkeys) ):
            setattr(self,parmkeys[n],parms[n])

        self.Curve_Init_Parameters()
            
    ##! 
    ##! Do nothing function Run_Curves_Post.
    ##! Overridden in actual Curve class.
    ##! 

    def Run_Curves_Post(self):
        for pddefs in self.PDFs:
            meshtype=pddefs[0]
            ctype=pddefs[1]
            parms=pddefs[2]

            texfile=i=None
            if (len(pddefs)>3):
                texfile=pddefs[3]
                if (len(pddefs)>4):
                    i=pddefs[4]
                    
            self.Curve_Type_PDFs(meshtype,ctype,parms,texfile,i)       


        latex=[]
        for figures in self.Latex_Figs:
            latex=latex+self.Latex_Figures_Table(False,[figures[0]],[figures[1]])
            
        texfile="/".join([
            self.Latex_Out_Path(),
            self.Name+".Figures.tex"
        ])
        
        self.File_Write(texfile,latex,True)
        return latex


    
    def Run(self):
        verify=self.__Calc__()
        print "Running",len(self.ts),"/".join(self.Curve_Paths())+":"
        #self.__Tex2__()

        self.__Write__()
        self.__SVG__()
        return verify

    def __str__(self):
        return "Curve: "+self.Name+" "+str(self.N)+" "+"["+str(self.t1)+","+str(self.t2)+"] "+"/".join(self.Curve_Paths())
        
    def Curve_Paths(self):
        return self.Curve_BasePaths+[
            self.Name,
        ]+self.Curve_Parameters_Values_Format(self.Curve_Parameter_Values())
        
    def Curve_File_Name(self,name):
        fnames=self.Curve_Paths()
        fnames.append(name)
        return "/".join(fnames)
        
    def Curve_Base_Name(self,name):
        fnames=[
            self.Curve_BasePath,
            name
        ]
        return "/".join(fnames)
        
    def Curve_Parameters_Values_Format(self,parms):
        values=[]
        for parm in parms:
            value=parm
            if (parm.__class__.__name__=='int'):
                value="%d"  % parm
            elif (parm.__class__.__name__=='float'):
                value="%.6f"  % parm
            elif (parm.__class__.__name__=='list'):
                value="-".join(parm)

            value=re.sub('\.',"_",value)
            values.append(value)
            
        return values
    
    def Curve_Parameters_2_Paths(self,parms=[]):
        if (parms.__class__.__name__!='list' or  len(parms)==0 ):
            parms=self.Curve_Parameter_Values()

        parms=self.Curve_Parameters_Values_Format(parms)
        
        return "-".join(parms)
    
    def Curve_SVG_Paths_Base(self,name):
        paths=self.Curve_BasePaths+[
            self.Name,
        ]
        if (name): paths.append(name)
        
        return paths
        
    def Curve_Init_Parameters(self):            
        return
    
    def Curve_Parameters_2_Path(self,name,ctype,parms=[]):
        paths=self.Curve_SVG_Paths_Base(name)
        
        if (parms):
            path=self.Curve_Parameters_2_Paths(parms)
            if (ctype):
                path=ctype+"_"+path
                
            paths.append(path)

        return paths
    
    def Curve_SVG_Paths(self,name,ctype,parms=True):
        paths=self.Curve_SVG_Paths_Base(name)
        
        if (parms):
            path=self.Curve_Parameters_2_Paths(parms)
            if (ctype):
                path=ctype+"_"+path
                
            paths.append(path)

        paths[ len(paths)-1 ]=paths[ len(paths)-1 ]+".svg"
        return paths
        
    def Curve_SVG_Name(self,name,ctype,parms=True):
        fnames=self.Curve_SVG_Paths(name,ctype,parms)
        return "/".join(fnames)
        
    def Max(self):
        pmax=self.Rs.Max()
        if ( hasattr(self,"PMax") ):
            pmax=self.PMax()

        return pmax

    def Min(self):
        pmin=self.Rs.Min()
        if ( hasattr(self,"PMin") ):
            pmin=self.PMin()

        return pmin

    
    def Point_Draw(self,p,color="black",thickness=2):
        return [ self.Rs.Mesh_SVG_Point(p,color,thickness) ]
    
    def Circle_Draw(self,c,r,color="black",thickness=2,drawcenter=False):
        circle=self.Rs.Circle(c,r)

        svg=[]
        svg=svg+circle.Mesh_SVG_Curve(color,thickness)
        if (drawcenter):
            svg=svg+self.Point_Draw(c,color,2*thickness)
            
        return svg
