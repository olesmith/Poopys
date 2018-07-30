from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve

class Hyperbola(Curve):
    Name="Hyperbola"

    a=1.0
    b=2.0
    rho=2.0
    N=400
    
    xmax=10.0
    ymax=10.0

    t1=-10.0
    t2= 10.0

    Symmetries=[]
    tmp=[
        Matrix([
            [-1.0,0.0],
            [ 0.0,1.0],
        ]),
    ]
    
    Show_Point_Size=10
    #Show_Point_Nos=[190,200,210]
    Show_Point_Nos=[]
    Latex_Figs=[
            [
                [
                    "Hyperbola/Hyperbola_Ana_2_000000-1_000000-400.pdf",
                ],
                [ "$a=2$", ],
            ],
            [
                [
                    "Hyperbola/Hyperbola_Ana_0_500000-1_000000-400.pdf",
                ],
                [ "$a=0.5$", ],
            ],
    ]
    
    def PMax(self):
        return Vector([self.xmax,self.ymax])
    
    def PMin(self):
        return Vector([-self.xmax,-self.ymax])
    
        
    ##!
    ##! Size of coordinate system (1) - override!
    ##!

    def Curve_Coordinate_System_Get(self):
        return 5.0
    
    def Curve_Parameters(self):
        b=1.0
        ass=[
            2.0,1.75,sqrt(2),
            1.25,1.0,1.0/1.25,
            1.0/sqrt(2),1.0/1.75,1.0/2.0,
        ]
        return [
            ass,
            [
                1.0,
            ],
        ]
    
    def Run_Curves_Post0000(self):
        self.Run_Curves_Post_Type("Evolute","Evolute")
        self.Run_Curves_Post_Type("dEvolute","dEvolute")
        
    def Run_Curves_Post_Type(self,type,texfile):
        b=1.0
        ass=[
            [
                2.0,1.75,sqrt(2),
            ],
            [
                1.25,1.0,1.0/1.25,
            ],
            [
                1.0/sqrt(2),1.0/1.75,1.0/2.0,
            ],
        ]
        
        
        pdffiles=[]
        titles=[]
        no=1
        for rass in ass:
            rpdffiles=[]
            rtitles=[]
            for a in rass:
                paths=self.Curve_Parameters_2_Path(
                    type,"Ana",
                    self.Curve_Parameters_Values_Format([a,b,self.N])
                )

                pdffile="/".join(paths)+".pdf"
                
                paths.pop(0)
                paths.pop(0)
                paths.pop(0)

                svgfile="/".join(paths)+".svg"
                print self.SVG_2_PDF(svgfile,pdffile)

                rpdffiles.append(pdffile)
                rtitles.append("$a="+str(a)+"$")

            pdffiles.append(rpdffiles)
            titles.append(rtitles)


            self.Latex_Figures_Table(
                self.Curve_Base_Name(self.Name)+"/"+texfile+"."+str(no)+".tex",
                pdffiles,
                titles
            )
            pdffiles=[]
            titles=[]
            no+=1
            
        
    
    def Curve_Init_Parameters(self):
        return
    
    
    def Curve_Parameter_Values(self):
        return [
            self.a,self.b,self.N
        ]
    
    def Curve_Parameter_Keys(self):
        return [ "a","b"]
    def Curve_Parameter_Names(self):
        return [ "a","b"]

    
    def R(self,t):
        return Vector([
            sqrt(  self.a**2*(1.0+t**2)  ),
            self.b*t,
        ])
    
    def Equation_Tex(self):
        return "\\frac{ (x-x_0)^2 }{a^2}-\\frac{ (y-y_0)^2 }{b^2}=1"
    
    
    def R_Tex(self):
        return self.Latex_vect(["a\\sqrt{1+t^2}","bt"])
        
    def dR(self,t):
        return Vector([
            self.a*t/(  sqrt(1.0+t**2)  ),
            self.b,
        ])

    def dR_Tex(self):
        return self.Latex_vect(["\\frac{at}{\\sqrt{1+t^2}}","b"])
        
    def dRN_Tex(self):
        return self.Latex_vect(["-b","\\frac{at}{\\sqrt{1+t^2}}"])
        
    def d2R(self,t):
        return Vector([
            self.a/(  sqrt(1.0+t**2)**3  ),
            0.0,
        ])

    def d2R_Tex(self):
        return self.Latex_vect(["a(1+t^2)^{-3/2}","0"])
        
    def d3R(self,t):
        return Vector([
            -3.0*self.a*t/(  sqrt(1.0+t**2)**5  ),
            0.0,
        ])

    def d3R_Tex00(self):
        return self.Latex_vect(["-3at (1+t^2)^{-5/2}","0"])
        
    def v2(self,t):
        return (  (self.a**2+self.b**2)*t**2+self.b**2   )/(1+t**2)
    
    def v2_Tex(self):
        return "\\frac{  (a^2+b^2) t^2+b^2  }{ 1+t^2 }"
       
    def v2_inv_Tex(self):
        return "\\frac{ 1+t^2 }{  (a^2+b^2) t^2+b^2  }"
       

    def t(self,t):
        v=sqrt(  self.v2(t)  )
        
        return Vector([
            self.a*t/(  sqrt(1.0+t**2)  ),
            self.b,
        ])*(1.0/v)

    def t_Tex(self):
        return "\\sqrt{"+self.v2_inv_Tex()+"}"+self.dR_Tex()
        
    def n(self,t):
        v=sqrt(  self.v2(t)  )
        
        return Vector([
            -self.b,
            self.a*t/(  sqrt(1.0+t**2)  ),
        ])*(1.0/v)

    def n_Tex(self):
        return "\\sqrt{"+self.v2_inv_Tex()+"}"+self.dRN_Tex()
        
    def VN(self,t):
        return Vector([
            -self.b,
            self.a*t/(  sqrt(1.0+t**2)  )
        ])

    def VN_Tex(self):
        return "-"+self.Latex_vect(["-b","\\frac{at}{\\sqrt{1+t^2}}"])
        
    def Det(self,t):
        return -self.a*self.b*(1.0+t**2)**(-1.5)
    
    def Det_Tex(self):
        return "-ab (1+t^2)^{-3/2}"
        
    def Phi(self,t):
        return -(  (self.a**2+self.b**2)*t**2+self.b**2 )*sqrt(1+t**2)/(self.a*self.b)

    def Phi_Tex(self):
        return "-\\frac{ (a^2+b^2) t^2+b^2 }{ab} \\sqrt{1+t^2}"
        
    def Kappa(self,t):
        return (self.a*self.b)/(  (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )**1.5  )
    
    def Kappa_Tex(self):
        return "-ab\\left(\\frac{ab}{  (a^2+b^2) t^2+b^2}\\right)^{3/2}(1+t^2)^{-3}"

    def Rho(self,t):
        return (  (  (self.a*sin(t))**2.0  +  (self.b*cos(t))**2.0  )**1.5  )/(self.a*self.b)

    def Rho_Tex00(self):
        return "\\frac{   ("+self.v2_Tex()+")^{3/2}   }{ab}"
        
    def Evolute(self,t):

        t12=1.0+t**2
        ab2=self.a**2+self.b**2
        
        return Vector([
            self.b*(  t12**1.5  ),
            -self.a*t**3,
        ])*(ab2/self.a*self.b)
    
    def Evolute_Tex(self):
        return "\\frac{a^2+b^2}{ab}"+self.Latex_vect([
            "b(1+t^2)^{3/2}",
            "-at^3"
        ])
    
    def dEvolute(self,t):
        t12=1.0+t**2
        ab2=self.a**2+self.b**2
        
        return Vector([
            self.b*t*(  t12**0.5  ),
            -self.a*t**2,
        ])*(3.0*ab2/self.a*self.b)

        
    def dEvolute_Tex(self):
        return "-3\\frac{a^2+b^2}{ab}"+self.Latex_vect(["bt\\sqrt{1+t^2}","-at^2"])
        
if (re.search('Hyperbola.py$',sys.argv[0])):
    curve=Hyperbola({
    })

    curve.Run()
