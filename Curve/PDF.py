from Vector import Vector

from System import *
from File import *


class Curve_PDF():
    
    Svg2Pdf="/var/www/cgi-bin/PDF"

    
    ##!
    ##! Generates PDFs for a list of parameter lists,
    ##! for curve type. Returns list of pdffiles created.
    ##! Type should be mtype_Num or mtype_Ana
    ##!
    
    def Curve_Types_PDFs000(self,meshtype,parameterlist,texfile=None,i=None):
        pdffiles=[]
        for ctype in ["Num","Ana"]:
            pdffiles.append(
                self.Curve_Type_PDFs(meshtype,ctype,parameterlist,texfile,i)
            )

        return pdffiles
    
    ##!
    ##! Generates PDFs for a list of parameter lists,
    ##! for curve type. Returns list of pdffiles created.
    ##! Type should be mtype_Num or mtype_Ana
    ##!
    
    def Curve_Type_PDFs(self,meshtype,ctype,parameterlist,texfile=None,i=None):
        titles=[]
        pdffiles=[]
        for parameters in parameterlist:
            pdffiles.append( self.Curve_Type_PDF(meshtype,ctype,parameters) )
            titles.append( self.Curve_Type_PDF_Title(parameters,i) )


        if (texfile!=None):
            self.Latex_Figures_Table(
                "/".join([
                    self.Latex_Out_Path(),
                    texfile
                ]),
                [ pdffiles ],
                [ titles ]
            )
        return pdffiles
    
    ##!
    ##! Generates PDF for parameters,for curve type. 
    ##! Returns name of pdffile created.
    ##!
    
    def Curve_Type_PDF(self,meshtype,ctype,parameters):
        parameters.append(self.N)
        paths=self.Curve_Parameters_2_Path(
            meshtype,ctype,
            self.Curve_Parameters_Values_Format(parameters)
        )


        pdffile="/".join(paths)+".pdf"

        if (not File_Exists(pdffile)):
            paths.pop(0)
            paths.pop(0)
            paths.pop(0)

            svgfile="/".join(paths)+".svg"
            self.SVG_2_PDF(svgfile,pdffile)

        return pdffile
    
    ##!
    ##! Generates title for parameters,for curve type. 
    ##! Returns name of pdffile created.
    ##!
    
    def Curve_Type_PDF_Title(self,parameters,i=None):
        names=self.Curve_Parameter_Names()

        if (i!=None):
            return "$"+names[i]+"="+str(parameters[i])+"$"

        comps=[]
        for i in range(names):
            comps.append( "$"+names[i]+"="+str(parameters[i])+"$" )
        
        return ", ".append(comps)
