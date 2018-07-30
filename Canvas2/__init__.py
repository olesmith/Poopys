from R_n import *

class Canvas2():
    Resolution=[800,800]
    A=None
    B=None
    PMin=None
    PMax=None

    Eps=0.05 #pixel margin %
    
    def __init__(self,pmin,pmax,resolution=[]):
        if (resolution): self.Resolution=resolution
        
        self.__Canvas_Init__(pmin,pmax)
        

        return
    
    def __str__(self):
        comps=[
            "Canvas2:",
            "Resolution="+
            str(self.Resolution[0])+"x"+str(self.Resolution[1]),
            "Pmin=("+
            str(self.PMin[0])+","+str(self.PMin[1])+
            ")",
            "Pmax=("+
            str(self.PMax[0])+","+str(self.PMax[1])+
            ")",
            "A=("+
            str(self.A[0])+","+str(self.A[1])+
            ")",
            "B=("+
            str(self.B[0])+","+str(self.B[1])+
            ")",
        ]
        return " ".join(comps)
    
    def __Canvas_Init__(self,pmin,pmax):
        self.PMin=pmin
        self.PMax=pmax
        self.Thickness_Factor=10.0/sqrt( self.Resolution[0]**2+self.Resolution[1]**2 )

        #Invert y-axis
        self.A=Matrix([
            [1.0, 0.0],
            [0.0,-1.0],
        ])

        #Translate up
        self.B=Vector([   0.0,self.PMax[1]+self.PMin[1]   ])
        
        return
            
    def Point2Pixels(self,p):
        if (not p or p==None): return None

        #Make sure e have a Vector, not a list
        if (p.__class__.__name__=='list'): p=Vector(p)
        
        return self.A*p+self.B

    def Points2Pixels(self,ps):
        pxs=[]
        for p in ps:
            px=None
            if (p):
                px=self.Point2Pixels(p)
                
            pxs.append(px)
        
        return pxs
    
