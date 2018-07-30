from Args import *
from File import *



from Latex import *

def Grep(regex,glist):
    rlist=[]
    for line in glist:
        if (re.search(regex,line)):
            rlist.append(rlist)
            
    return rlist

class Curves2_Latex(Latex):
    
    def Latex_Curve_Paths(self):
        return [
            "","usr","local","Curves",
        ]
    
    def Latex_Curve_Component_Files(self):
        return [
            "Equation",
            "Parameters",
            "Parametrization",
            #"Vectors",
            #"dVectors",
            #"VectorsN",
            "R",
            "dR",
            "VN",
            "d2R",
            "d3R",
            "v2",
            "Det",
            "t",
            "n",
            "v",
            "Psi",
            "Phi",
            "Kappa",
            "Rho",
            "Evolute",
            "dEvolute"
        ]
    
    def Latex_Curve_Components(self):
        return {
            "Equation":        "",
            "Parameters":      "",
            "Parametrization": "\\Vector{r}",
            "R":               "\\Vector{r}",
            "Vectors":         "",
            "dVectors":        "",
            "VectorsN":        "",
            "dR":              "\\Vector{r}'",
            "d2R":             "\\Vector{r}''",
            "d3R":             "\\Vector{r}'''",
            "VN":              "\\Vector{\\widehat r}'",
            "t":               "\\Vector{t}",
            "n":               "\\Vector{n}",
            "v":               "v",
            "v2":              "v^2",
            "Det":             "D",
            "Psi":             "\\psi",
            "Phi":             "\\varphi",
            "Kappa":           "\\kappa",
            "Rho":             "\\rho",
            "Evolute":         "\\Vector{c}",
            "dEvolute":        "\\Vector{c}'",
        }
    def Latex_Curves_Table_Generate(self):
        args=Args_Get()
        args.pop(0)

        curves=[]
        titles=[]
        for n in range(0,len(args),2):
            curves.append(   args[n]  )
            
            title=args[n]
            if ( n+1<len(args) ): title=args[n+1]
            titles.append(title)

        table=[
            "   \\hline",
            self.Latex_Curves_Table_Titles(titles),
            "   \\hline",
        ]
        
        for texfile in self.Latex_Curve_Component_Files():
            table=table+self.Latex_Curves_Rows(texfile,curves)

        table=table+[
            "   \\hline",
        ]
        
        print "\n".join(
            self.Latex_Table(
                table,
                {
                    "Specs": self.Latex_Curves_Table_Specs(curves)
                }
            )
        )

    
    def Latex_Curves_Table_Specs(self,curves):
        specs=["|l"]
        for curve in curves:
            specs.append("|c")
            
        return "".join(specs)+"|"
    
    def Latex_Curves_Table_Titles(self,titles):
        if (len(titles)==0): return []

        
        rtitles=[""]
        for title in titles:
            rtitles.append( "\\textbf{"+title+"}" )
            
        return rtitles
    
    def Latex_Curves_Rows(self,texfile,curves):
        parms=self.Latex_Curve_Components()
        start=parms[ texfile ]
        
        row=[ "$"+start+"$" ]
        for curve in curves:
            row=row+[
                self.Latex_Curve_Row_File_Cell(
                    texfile,
                    curve
                )
            ]

        rows=[]
        
        if (Grep('input',row)):
            rows=[row]

        return rows
    
    def Latex_Curve_File(self,texfile,curve):
        return "/".join(
            self.Latex_Curve_Paths()+[
                curve,texfile
            ]
        )+".tex"
    
    def Phi_Tex(self):
        return "1/\\psi(t)"
    
    def Latex_Curve_Row_File_Cell(self,texfile,curve):
        cell="---"
        rtexfile=self.Latex_Curve_File(texfile,curve)
        if (  File_Exists(rtexfile)  ):
            lines=File_Read(rtexfile)
            cell="$"+"\\displaystyle \\input{"+rtexfile+"}$"

        return cell
