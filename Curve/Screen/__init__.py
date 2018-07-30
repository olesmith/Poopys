
from Menu import Curve_Screen_Menu
from Parameters import Curve_Screen_Parameters
from Components import Curve_Screen_Components
from Caroussel import Curve_Screen_Caroussel
from Latex import Curve_Screen_Latex
from Animation import Curve_Screen_Animation

class Curve_Screen(
        Curve_Screen_Menu,
        Curve_Screen_Parameters,
        Curve_Screen_Components,
        Curve_Screen_Caroussel,
        Curve_Screen_Latex,
        Curve_Screen_Animation
    ):

    #!
    #! Generate the central curve screen: Menu.
    #! Branch for Latex=1, Animation=1 and Carousel=1
    #!
    
    def Curve_Screen(self):
        html=[
            self.H(3,self.Name),
            self.Curve_Menu(),
        ]

        if (self.CGI_GET_Get("Latex")=="1"):
            html.append(  self.Curve_Latex()  )

        if (self.CGI_GET_Get("Animation")=="1"):
            html.append(  self.Curve_Animation()  )

        
        return html
