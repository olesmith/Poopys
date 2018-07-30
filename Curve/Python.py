from File import *
import re

##Class for locating and latex'ing code fragments. 
class Curve_Python():
    def Curve_Python_Analyticals(self):
        rcomps=[]
        for comps in self.Curve_Latex_Components_Get():
            rcomps=rcomps+comps
        return comps
                
    def Curve_Python_Analytical_Codes(self):
        for comp in self.Curve_Python_Analyticals():
            self.Curve_Python_Def_Code(comp)
            
    def Curve_Python_Analytical_Function(self,comp):
        return comp
    
    def Curve_Python_Analytical_File(self,comp):
        return "/usr/local/python/Curves2/"+self.Name+".py"
    
    def Curve_Python_Def_Code(self,comp):
        filename=self.Curve_Python_Analytical_File(comp)
        funcname=self.Curve_Python_Analytical_Function(comp)

        python=File_Read_Lines(filename)

        regex_def='^\s*def\s+'

        for n in range( len(python) ):
            if (re.search(regex_def+funcname,python[n])):
                rpython=["\\begin{lstlisting}"]
                nn=n
                while (nn+1<len(python) and not re.search(regex_def,python[nn+1])):
                    rpython.append(python[nn])
                    nn+=1
                rpython.append("\\end{lstlisting}")

                pyfile=self.Curve_Base_Name(self.Name+"/"+comp+".py")
                res=File_Write(
                    pyfile,
                    rpython,
                    pyfile
                )
                return rpython

        print "Warning!",funcname,"not found in file:",filename
        return []
