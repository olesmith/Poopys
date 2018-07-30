

class Curve_Screen_Menu():
    #!
    #! Generate the central curve screen horisontal menu.
    #!
    
    def Curve_Menu(self):
        hrefs=["|"]
        for screen in [ "Latex","Carousel","Animation" ]:
            url="?Curve="+self.Name+"&"+screen+"="+str(1)
            hrefs.append(  self.A(url,screen)+"|"  )
            
        return self.Center([hrefs])
