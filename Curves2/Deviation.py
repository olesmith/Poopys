from File import *

class Curves2_Deviation():
    #Ressembles the deviations calculated for parameters specified in 
    Deviation_Tables=[]
    
    def Deviation_Tables_Generate(self,deviations):
        tables=[]
        for devtable in self.Curve.Curve_Deviations():
            tables.append( self.Deviation_Table_Generate(deviations,devtable))
            
        latexname=self.Curve.Curve_Latex_Components_Deviations_File()
        File_Write(
            latexname,
            ["\\begin{center}","\n\n".join(tables),"\\end{center}"],
            latexname
        )
        print latexname


    def Matrix_Get(self,r,s,empty=""):
        matrix=[]
        for i in range(r):
            matrix.append([])
            for j in range(s):
                matrix[i].append(empty)
        return matrix
    def Matrix_Transpose(self,m):
        return [[m[j][i]   for j in range(len(m))] for i in range(len(m[0]))  ]
        
    def Deviation_Table_Generate(self,deviations,devtable):
        titles=["Prop."]
        specs=["|c|"]
        for devrow in devtable:
            titles.append( devrow[0] )
            specs.append("r")
        specs.append("|")

        comptypes=self.Curve.Curve_Types_Deviations()
            
        table=[]
        firsts=[]
        for devrow in devtable:
            parameters=devrow[1]
            
            parmkey=self.Run_Parameters2Key(parameters)

            firsts=[]
            row=[]
            if (deviations.has_key(parmkey)):
                parmdeviations=deviations[ parmkey ]
                for comptype in comptypes:
                    if (parmdeviations.has_key(comptype) and self.Curve.Curve_Type_Has_Analytical(comptype)):
                        compvalue=parmdeviations[ comptype ]
                    
                        compname=self.Curve.Curve_Latex_Component_Name(comptype)
                        row.append(compvalue)
                        firsts.append('$'+compname+'$')

                if (len(row)>0):
                    table.append(row)

 
        table=self.Matrix_Transpose(table)
        rtable=[]
        for i in range(   len(table)   ):
            rrow=[firsts[i]]+table[i]
            rtable.append(rrow)

        rtable=["\\hline"]+[titles]+["\\hline"]+rtable+["\\hline"]

        
        return "\n".join(
            self.Latex_Table(
                rtable,
                {
                    "Specs": "".join(specs)
                }
            )
        )

        print "\n".join( self.Latex_Table(table) )



        
    def Deviation_Table_Generate0ld(self,deviations,devtable):
        names=self.Curve.Curve_Parameter_Names()
        
        if (len(devtable)>0):
            listvar=None
            listvarname=None
            listvarvalues=None

            listnonvalues=[]

            parms=[]
            ass=devtable[0]
            if (ass.__class__.__name__=='list'):
                if (len(ass)>1):
                    listvar=0
                    listvarvalues=ass
                    listvarname=names[0]
                else:
                    listnonvalues.append(   names[0]+"="+str(ass[0]) )
            else:
                listnonvalues.append(   names[0]+"="+str(ass)  )
                
            if (len(devtable)>1):
                bss=devtable[1]
                if (bss.__class__.__name__=='list'):
                    if (len(bss)>1):
                        listvar=1
                        listvarvalues=bss
                        listvarname=names[1]
                    else:
                        listnonvalues.append(   names[1]+"="+ str(bss[0])   )
                else:
                    listnonvalues.append(   names[1]+"="+ str(bss)   )
               
            if (len(devtable)>2):
                css=devtable[2]
                if (css.__class__.__name__=='list'):
                    if (len(css)>1):
                        listvar=2
                        listvarvalues=css
                        listvarname=names[2]
                    else:
                        listnonvalues.append(   names[2]+"="+str(css[0])   )
                else:
                    listnonvalues.append(   names[2]+"="+str(css)   )

            
            
            print listvar,listvarname,listvarvalues,listnonvalues
        return []
