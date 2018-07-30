from Vector import Vector

from Mesh import Mesh

class Curve_R():

    ##!
    ##! Calculate Curve values.
    ##! Store in self.Rs
    ##!

    Rs=None
    Canvas=None
    
    def Calc_Rs(self):
        self.Rs=Mesh(self.N,"R","")

        err=0
        for n in range( self.N ):
            try:
                self.Rs[n]=self.R(  self.ts[n]  )
            except ValueError:
                err=1
                
        return err
                
    ##!
    ##! Draw curve as SVG polyline.
    ##!
    
    def Rs_SVG(self,tell=False):
        self.Rs.Mesh_SVG(
            self.Curve_SVG_Name("d0R",""),
            self.Curve_Component_Get("R","Color","Ana"),
            tell,
            self.Show_Points,
            self.Show_Point_Size,
            self.Curve_Component_Get("R","Color","Ana"),
            True, #text
            self.Curve_Coordinate_System_Get(),
            [],[],
            self.Symmetries
        )
        
