            
class Colors():
    def Colors_Delta(self,n,color1,color2):
        color=[]
        for i in range( len(color1) ):
            col=int(   1.0*(color2[i]-color1[i])/(1.0*(n))  )
            color.append(col)

        return color
    def Colors_Sum(self,color,dcolor):
        rcolor=[]
        for i in range( len(color) ):
            col=int( color[i]+dcolor[i] )
            rcolor.append(col)

        return rcolor
    def Color_2_RGB(self,color):
        rcolor=list(color)
        for i in range( len(color) ):
            rcolor[i]=str(rcolor[i])
                
        return "rgb("+",".join(rcolor)+")"
    
    def Colors_Generate(self,n,color1,color2):
        dcolor=self.Colors_Delta(n,color1,color2)

        colors=[]
        
        color=color1
        for i in range(n):
            colors.append(
                self.Color_2_RGB(color)
            )
            color=self.Colors_Sum(color,dcolor)
            
        colors.append(
            self.Color_2_RGB(color2)
        )
            
        return colors
