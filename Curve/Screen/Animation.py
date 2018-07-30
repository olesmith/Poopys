from Canvas2 import Canvas2

class Curve_Screen_Animation():
    
    #!
    #! Generate the central curve animation screen.
    #!
    
    def Curve_Animation(self):
        self.Curve_Parameters_CGI_Set()
        self.__Init__()
        self.__Calc__()

        n=50
        html=[
            self.Curve_Parameters_Form(),
            self.Curve_Animation_SVG(n)
        ]

        return html
    
    #!
    #! Generate the central curve carousel part
    #!
    
    def Curve_Animation_Carousel(self):
        html=[
            #self.Curve_Parameters_Form()
        ]

        return html
        
    #!
    #! Creates the curve animation in svg.
    #!
    
    def Curve_Animation_SVG(self,n):
        svg=self.Rs.SVG_Pre_Amble(self.Rs.__Canvas__)
        meshes=self.Curve_Animation_Meshes(n)

        color="orange"
        for mesh in meshes:
            svg=svg+mesh.Mesh_SVG_Draw_Curve(color)

        svg=svg+self.Rs.SVG_Post_Amble(self.Rs.__Canvas__)
        return svg
    
    #!
    #! Creates the curve animation in svg.
    #!
    
    def Curve_Animation_Meshes(self,n):
        meshes=[
            self.Rs,
            self.dRs_Num,self.d2Rs_Num,self.Ts_Num,self.Ns_Num,
            self.VNs_Num,self.RhoVs_Num,
            self.Evolutes_Num,self.dEvolutes_Num,
        ]

        pmin=self.Rs.Min(meshes)
        pmax=self.Rs.Max(meshes)
        
        self.Rs.__Canvas__=Canvas2(pmin,pmax,self.Resolution)
        return meshes
