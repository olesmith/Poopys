from File import *
import re


class Curve_Latex():
    Curve_Latex_Equations=[
        "Equation","Parameters","Parametrization",
        "Vectors", "dVectors", "VectorsN",
    ]

    Curve_Latex_Components=[
        #[ "Vectors",],# "dVectors", "VectorsN", ],
        [
            "R","dR",
        ],
        ["d2R","VN", ],
        ["v2","Det", ],
        ["dv2","dDet", ],
        ["t","n", ],
        [ "Psi","Phi" ],
        [ "Kappa","Rho" ],
        [ "dPhi","dPsi" ],
        [ "dKappa","dRho" ],
        #[ "RhoV", ],
        ["Evolute","dEvolute"],
        ["SPs","Evolute_SPs"],
        ["S", ],
    ]
      
    def HTML_Latex(self,latex):
        if (latex.__class__.__name__!="list"):
            latex=[latex]
            for i in range( len(latex) ):
                latex[i]=re.sub(r'\\\[','[;',latex[i])
                latex[i]=re.sub(r'\\\]',';]',latex[i])

        return "".join(latex)
    
    def Curve_Latex(self):
        return [
            self.Latex_Eq("Parametrization:","Parametrization"),
            self.Latex_Eq("Parameters:","Parameters"),
            self.Latex_Eq("Canonical:","R"),
            self.Latex_Eq("1st Derivative:","dR"),
            self.Latex_Eq("Singular Points:","SPs"),
            self.Latex_Eq("2nd Derivative:","d2R"),
            #self.Latex_Eq("3rd Derivative:","d3R"),
            self.Latex_Eq("Squared Velocity:","v2"),
            self.Latex_Eq("Arc Length:","S"),
            self.Latex_Eq("Unit Tanget:","T"),
            self.Latex_Eq("Unit Normal:","N"),
            self.Latex_Eq("Velocity Normal:","VN"),
            self.Latex_Eq("Curve Determinant:","Det"),
            self.Latex_Eq("Curvature Factor:","Phi"),
            self.Latex_Eq("Curvature:","Kappa"),
            self.Latex_Eq("Curvature Radius:","Rho"),
            self.Latex_Eq("Evolute:","Evolute"),
            self.Latex_Eq("Evolute Singular Points:","Evolute_SPs"),
            self.Latex_Eq("Evolute Derivative:","dEvolute"),
        ]

    #Path to Tex output files
    def Latex_Out_Path(self):
        return "/".join([  "/usr/local/Curves/Latex"   ])

    
    def Curve_Latex_Components_Table_File(self):
        return self.Latex_Out_Path()+"/"+self.Name+".Table.tex"
            
    def Curve_Latex_Components_Figures_File(self):
        return self.Latex_Out_Path()+"/"+self.Name+".Figures.tex"
            
    def Curve_Latex_Components_Deviations_File(self):
        return self.Latex_Out_Path()+"/"+self.Name+".Deviations.tex"
            
    def Curve_Latex_File(self):
        return self.Latex_Out_Path()+"/"+self.Name+".tex"
        
    def __Tex__(self,write=True):
        latex=self.Curve_Latex_Components_Title()

        latex=latex+self.Curve_Latex_Components_Equations()
        latex=latex+["\n\n"]
        
        table_tex=self.Curve_Latex_Components_Table("$")
        figures_tex=self.Curve_Latex_Figures()
        deviations_tex=self.Curve_Latex_Deviations()
        
        if (write):
            head=File_Read("Curve/Head.tex")
            tail=File_Read("Curve/Tail.tex")
            
            texpath=self.Latex_Out_Path()
            texfile=texpath+"/"+self.Name+".tex"
            texdoc=texpath+"/"+self.Name+".tex"
            texfile=texpath+"/"+self.Name+".Table.tex"
 
            latex=head+latex+table_tex+deviations_tex+figures_tex
            latex=latex+tail
            
            res=File_Write(
                self.Curve_Latex_File(),
                latex,
                texdoc
            )

            
            print Command_Exec(
                [
                    "/usr/bin/pdflatex",
                    "-output-directory",
                    texpath,
                    texdoc,
                    ">> ouput.log;",
                    "rm "+texpath+"/*.log;"
                    "rm "+texpath+"/*.aux;"
                ],
                texpath
            )

        return latex
    
    def Curve_Latex_Components_Get(self):
        return self.Curve_Latex_Components
          
    
    
    def Curve_Latex_Components_Equations(self):
        latex=[]
        for equation in self.Curve_Latex_Equations:
            if (hasattr(self,equation+"_Tex")):
                method=getattr(self,equation+"_Tex")
            
                tex=method()
                self.Curve_Latex_Component_Formula_Write(equation,tex)
                latex.append("\\[\n"+re.sub('\n',"\n   ",tex)+"\n\\]\n\n")

        return latex
    
    def Curve_Latex_Components_Title(self):
        return [
            "\\subsection{"+self.Title+"}",
        ]

    def Curve_Latex_Figures(self):
        texfigfile=self.Curve_Latex_Components_Figures_File()

        latex=[]
        if ( File_Exists(texfigfile) ):
            latex=[
                "\\input{"+re.sub('.tex$',"",texfigfile)+"}\n",
            ]

        return latex
    
    def Curve_Latex_Deviations(self):
        texdevfile=self.Curve_Latex_Components_Deviations_File()

        latex=[]
        if ( File_Exists(texdevfile) ):
            latex=[
                "\\input{"+re.sub('.tex$',"",texdevfile,)+"}\n",
            ]

        return latex
    
    def Curve_Latex_Components_Table(self,formula=None):
        table=[
            "\\toprule",
            [
                "\\textbf{Property}","","\\textbf{Expression}",
                "\\textbf{Property}","","\\textbf{Expression}",
            ],
            "\\midrule",
        ]
        
        for comps in self.Curve_Latex_Components_Get():
            row=self.Curve_Latex_Components_Row(comps,formula)

            if (len(row)>0):
                table.append(row)
                table.append("\\\\")

        
        table=table+[
            "\\bottomrule",
        ]

        latex=self.Latex_Table(table)

        texfile=self.Curve_Latex_Components_Table_File()
        res=File_Write(texfile,latex,False)
        

        print "Latex written to ",texfile
        return [
            "\\Table{\\scalebox{0.75}{",
            "\\input{"+re.sub('.tex$',"",texfile)+"}\n",
            "}}",
            "{Geometrical Properties, "+self.Name+".}",
            "{\\linewidth}",
            "{table:"+self.Name+"}",
        ]

        return ["\\input{"+re.sub('.tex$',"",texfile)+"}\n"]

    
    def Curve_Latex_Component_Tex_Method(self,comp):
        return comp+"_Tex_Name"
    
    def Curve_Latex_Component_Tex_Name(self,comp):
        namemethod=self.Curve_Latex_Component_Tex_Method(comp)
        
        texname=comp
        if (hasattr(self,namemethod)):
            namemethod=getattr(self,namemethod)
            texname='$'+namemethod()+'$'
            
        return texname
         
    def Curve_Latex_Components_Row(self,comps,formula=None):
        row=[]
        hascomps=False
        for comp in comps:
            method=comp+"_Tex"

            cells=[]
            if (hasattr(self,method)):
                namemethod=comp+"_Tex_Name"
                namemethod=getattr(self,namemethod)
                cells=[
                    "$"+namemethod()+"$",
                    "$=$",
                    self.Curve_Latex_Component_Cell(comp,formula),
                ]
                hascomps=True
            row=row+cells


        if (len(row)==3):
            row=[" \\quad ".join(row)]

        #if (not hascomps): return []
        
        return row

    def Curve_Latex_Component_Name(self,comp,formula=None):
        if (comp=="N"): comp="n"
        if (comp=="T"): comp="t"
        
        namemethod=comp+"_Tex_Name"
        namemethod=getattr(self,namemethod)
        
        return namemethod()
        
    #Posible formulas: $, \[,
    def Curve_Latex_Component_Cell(self,comp,formula=None):
        method=comp+"_Tex"

        latex=""
        if (hasattr(self,method)):
            method=getattr(self,method)
            latex=method()
            self.Curve_Latex_Component_Formula_Write(comp,latex)

            if (formula=="$"):
                latex="$\\displaystyle "+latex+"$"
            elif (formula=="["):
                latex="\[\n"+re.sub('\n',"\n   ",latex)+"\n]"

                
        latex=re.sub('\n',"\n      ",latex)
        return "   %%"+comp+"_Tex\n      "+latex
        
    def Curve_Latex_Component_Formula_Write(self,comp,tex):
        texfile=self.Curve_Base_Name(self.Name+"/"+comp+".tex")
        return File_Write(texfile,[tex],False)
       
    def Latex_Figures_Table(self,texfile,filelists,titlelists,specsep="",spec="c",hline="",colsep="&",rowsep="\\\\"):
        if (len(filelists)==0):
            print "No graphic filelists given, ",filelists
            return []

        if (filelists[0].__class__.__name__!='list'):
            filelists2=[filelists]
            titlelists2=[titlelists]
            
        nfigsperrow=self.Latex_Table_Width(filelists)
        width="%.2f" % (1.0/nfigsperrow)

        prefig="\\includegraphics[width="+width+"\\linewidth]{"
        postfig="}"

        pretitle=""
        posttitle=""
        
        figures=[]
        names=[]

        latex=[]
        for i in range( len(filelists) ):
            table=[]
            table.append(hline)
            for j in range( len(filelists[i]) ):
                if (not re.search('^\/',filelists[i][j])):
                    filelists[i][j]="/".join([
                        self.Curve_BasePath,
                        filelists[i][j]
                    ])
                    
                filelists[i][j]=prefig+filelists[i][j]+postfig
                titlelists[i][j]=pretitle+titlelists[i][j]+posttitle
                

            table.append(filelists[i])
            table.append(titlelists[i])
            table.append(hline)

            latex=latex+self.Latex_Table(
                table,
                {
                    "SpecSep": specsep,
                    "Spec": spec,
                    "ColSep": colsep,
                    "RowSep": rowsep,
                }
            )

            latex=latex+[""]

        if (texfile): 
            res=File_Write(texfile,latex,True)
        
        return latex
        
        
    def Interval_Tex(self):
        return "["+str(self.t1)+","+str(self.t2)+"]"
        
    def Latex_Has(self,comp):
        namer=comp+"_Tex"

        res=False
        if ( hasattr(self,namer) ):
            res=True

        return res

    def Latex_Has_Name(self,comp):
        namer=comp+"_Tex_Name"

        res=False
        if ( hasattr(self,namer) ):
            res=True

        return res

    def Latex_Name(self,comp):
        if (comp=="N"): comp="n"
        if (comp=="T"): comp="t"

        namer=comp+"_Tex_Name"
        if ( hasattr(self,namer) ):
            method=getattr(self,namer)
            namer=method()

        return namer

    def Latex_Tex(self,comp):
        namer=comp+"_Tex"
        if ( hasattr(self,namer) ):
            method=getattr(self,namer)
            namer=method()
        
        return namer

    def Latex_Eq(self,title,comp):
        if (not self.Latex_Has(comp)): return ""

        latex=[]
        if (self.Latex_Has_Name(comp)):
            latex.append(self.Latex_Name(comp))
        
        if (self.Latex_Has(comp)):
            latex.append(self.Latex_Tex(comp))
        
        return "".join([
            title+
            "<P ALIGN='center'>[; ",
            " = ".join(latex),
            " ;]",
            "</P>",
        ])
        
    
    def Parametrization_Tex_Name(self):
        return self.Latex_Vector("r")+"(t)"
    
    def S_Tex_Name(self):
        return "s(t)-s(t_0)"
    
    def R_Tex_Name(self):
        return self.Latex_Vector("r")+"(t)"
    
    def dR_Tex(self):
        return "-"
    
    def dR_Tex_Name(self):
        return self.Latex_Vector("r")+"'(t)"
    
    def SPs_Tex_Name(self):
        return "\\mathcal{S}"
    
    def v2_Tex(self):
        return self.Latex_Vector("r")+"'(t)"+" \\cdot "+self.Latex_Vector("r")+"'(t)"
    
    def v2_Tex_Name(self):
        return "v(t)^2"
    
    def dv2_Tex_Name(self):
        return "\\frac{d}{dt} v(t)^2"
    
    def v_Tex_Name(self):
        return "v(t)"
    
    def d2R_Tex(self):
        return "-"
    
    def d2R_Tex_Name(self):
        return self.Latex_Vector("r")+"''(t)"
    
    def d3R_Tex(self):
        return "-"
    
    def d3R_Tex_Name(self):
        return self.Latex_Vector("r")+"'''(t)"
    
    def t_Tex(self):
        return "-"
    
     
    def t_Tex_Name(self):
        return self.Latex_Vector("t")+"(t)"
    
    def t_Tex(self):
        return "\\frac{"+self.dR_Tex()+"}{\\sqrt{"+self.v2_Tex()+"}} \\cdot "
    
    def n_Tex(self):
        return "-"
    
    def n_Tex_Name(self):
        return self.Latex_Vector("n")+"(t)"
    
    def n_Tex(self):
        return "\\frac{"+self.VN_Tex()+"}{\\sqrt{"+self.v2_Tex()+"}} \\cdot "
    
    def Det_Tex(self):
        return self.Latex_Vector("r")+"''(t) \\cdot "+self.Latex_Vector("\\widehat r")+"'(t)"
    
    def Det_Tex_Name(self):
        return "D(t)"
    
    def dDet_Tex_Name(self):
        return "D'(t)"
    
    def dDet_Tex00000000(self):
        return "-"

    def VN_Tex(self):
        return "-"
    
    def VN_Tex_Name(self):
        return "\\widehat{"+self.Latex_Vector("r")+"}'(t)"

    def Phi_Tex(self):
        return "\\frac{D(t)}{v(t)^2}"
    
    def Phi_Tex_Name(self):
        return "\\varphi(t)"
    
    def dPhi_Tex0000(self):
        return "\\frac{D(t)}{v(t)^2}"
    
    def dPhi_Tex_Name(self):
        return "\\varphi'(t)"
    
    def Psi_Tex(self):
        return "\\frac{v(t)^2}{D(t)}"
    
    def Psi_Tex_Name(self):
        return "\\psi(t)"
    
    def dPsi_Tex_Name(self):
        return "\\psi'(t)"
    
    def Kappa_Tex(self):
        return "\\frac{D(t)}{v(t)^3}"
    
    def Kappa_Tex_Name(self):
        return "\\kappa(t)"
    
    def dKappa_Tex_Name(self):
        return "\\kappa'(t)"
    
    def Kappa_Tex(self):
        return "\\frac{"+self.Det_Tex()+"}{ ("+self.v2_Tex()+")^{3/2}}"
    
    def Rho_Tex(self):
        return "\\frac{v(t)^3}{D(t)}"
    
    def Rho_Tex_Name(self):
        return "\\rho(t)"
    
    def dRho_Tex_Name(self):
        return "\\rho'(t)"
    
    def Rho_Tex(self):
        return "\\frac{("+self.v2_Tex()+")^{3/2}}{ ("+self.Det_Tex()+"}"
    
    def RhoV_Tex_Name(self):
        return "{\\underline \\rho}(t)"
    
    def Evolute_Tex(self):
        return "-"

    def Evolute_Tex_Name(self):
        return self.Latex_Vector("c")+"(t)"

    def Evolute_SPs_Tex000(self):
        return "-"

    def Evolute_SPs_Tex_Name(self):
        return "\\mathcal{E}"
    
    
    def dEvolute_Tex(self):
        return "-"

    def dEvolute_Tex_Name(self):
        return self.Latex_Vector("c")+"'(t)"


    #Unit vectors latex versions
    
    def EF_Vectors(self,omega=""):
        if (omega): omega=omega+" "
        
        return [
            self.Latex_Vector("e")+"("+omega+"t)="+self.Latex_vect([ "\\cos{"+omega+"t}" ,"\\sin{"+omega+"t}" ]),
            self.Latex_Vector("f")+"("+omega+"t)="+self.Latex_vect([ "-\\sin{"+omega+"t}","\\cos{"+omega+"t}" ]),
        ]

    def EF_dVectors(self,omega=""):
        if (omega): omega=omega+" "
        
        return [
            self.Latex_Vector("e")+"'("+omega+"t)= "+ omega+self.Latex_Vector("f")+"("+omega+"t)",
            self.Latex_Vector("f")+"'("+omega+"t)=-"+omega+self.Latex_Vector("e")+"("+omega+"t)",
        ]

    def EF_VectorsN(self,omega=""):
        if (omega): omega=omega+" "
        
        return [
            self.Latex_Vector("\\widehat e")+"("+omega+"t)="+ self.Latex_Vector("f")+"("+omega+"t)",
            self.Latex_Vector("\\widehat f")+"("+omega+"t)=-"+self.Latex_Vector("e")+"("+omega+"t)",
        ]

    def PQ_Vectors(self,omega=""):
        if (omega): omega=omega+" "
        
        return [
            self.Latex_Vector("p")+"("+omega+"t)="+self.Latex_vect([ "-\\cos{"+omega+"t}","\\sin{"+omega+"t}" ]),
            self.Latex_Vector("q")+"("+omega+"t)="+self.Latex_vect([ "-\\sin{"+omega+"t}","-\\cos{"+omega+"t}" ]),
        ]

    def PQ_dVectors(self,omega=""):
        if (omega): omega=omega+" "
        
        return [
            self.Latex_Vector("p")+"'("+omega+"t)=-"+self.Latex_Vector("q")+"("+omega+"t)",
            self.Latex_Vector("q")+"'("+omega+"t)="+self.Latex_Vector("p")+"("+omega+"t)",
        ]

    def PQ_VectorsN(self,omega=""):
        if (omega): omega=omega+" "
        
        return [
            "\\widehat{"+self.Latex_Vector("p")+"}("+omega+"t)="+self.Latex_Vector("q")+"("+omega+"t)",
            "\\widehat{"+self.Latex_Vector("q")+"}("+omega+"t)=-"+self.Latex_Vector("p")+"("+omega+"t)",
        ]

