
class Curve_SVG_Frenet():
    def Mesh_Frenet_SVG(self,dtype):
        attrt="Ts_"+dtype
        attrn="Ns_"+dtype
        
        svg=[]
        svgname=""
        if (hasattr(self,attrt) and hasattr(self,attrn)):
            tmesh=getattr(self,attrt)
            nmesh=getattr(self,attrn)
            if (tmesh and nmesh):
                tell=self.Curve_SVG_Name("Frenet",dtype)
                
                svg=svg+self.Rs.Mesh_SVG_Vectors(
                    [ tmesh,nmesh ],
                    self.Frenet_Every,
                    self.Curve_SVG_Name("Frenet",dtype),
                    self.Curve_Component_Get("R","Color") ,
                    [
                        self.Curve_Component_Get("Frenet","Color",dtype),
                        self.Curve_Component_Get("Frenet","Color",dtype),
                    ],
                    self.Curve_Component_Get("Frenet","Color","Thick"),
                    False, #tell
                    self.Symmetries
                )

                svgname=tell
                
        return svgname
    
    def Mesh_Frenet_SVGs(self):
        return {
            "Num": self.Mesh_Frenet_SVG("Num"),
            "Ana": self.Mesh_Frenet_SVG("Ana"),
        }
 
