
class Curve_SVG_Legends():
    ##! 
    ##! Generate curve legends insertion point.
    ##!

    def Curve_Legend_Inserts(self,functions):
        return [100,50],[100,0]

    ##! 
    ##! Generate curve legends insertion point.
    ##!

    def Curve_Legend_Title(self):
        return "&#8226;"

    ##! 
    ##! Generate curve legends insertion point.
    ##!

    def Curve_Legend_Text(self,function):
        return self.Curve_Component_Get(function,"SVG")

    ##! 
    ##! Generate curve legends for mesh functions.
    ##!

    def Curve_Legend_SVG(self,functions,colors):
        px,dx=self.Curve_Legend_Inserts(functions)
        
        svg=[self.SVG_Comment("Curves Legend")]
        for n in range( len(functions) ):
            svg=svg+[
                self.SVG_Text(
                    px,
                    self.Curve_Legend_Title(),
                    colors[n],
                    "20pt"
                )
            ]

            px[0]+=15
            
            svg=svg+[
                self.SVG_Text(
                    px,
                    self.Curve_Legend_Text(functions[n]),
                    colors[n],
                    "20pt"
                )
            ]
            
            for i in range( len(px) ): px[i]+=dx[i]

        return svg


    
