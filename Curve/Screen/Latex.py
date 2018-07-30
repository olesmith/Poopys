

class Curve_Screen_Latex():
    #!
    #! Generate the central curve screen Latex formulas.
    #!
    
    def Curve_Latex(self):
        htmltex=[]
        for tex in self.__Tex__(False):
            htmltex.append(self.Center(self.HTML_Latex(tex)))

        return "<BR>\n".join(htmltex)
