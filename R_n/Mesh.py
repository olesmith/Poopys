from Scalar import Scalar
from Vector import Vector

class Mesh(list):
    ##
    ## Mesh creator: allocates and/or initializes
    ##
    
    def __init__(self,ps=None):
        if (ps):
            if (ps.__class__.__name__=='int'):
                for n in range(  ps ):
                    self.append( Vector(2) )
            
            elif (ps.__class__.__name__=='int'):
                for n in range(  len(ps) ):
                    self.append( Vector(p) )
        return
    
    ##
    ## Mesh add: add as points
    ##
    
    def __add__(ps1,ps2):
        ps=Mesh()
        for n in range(  len(ps1) ):
            self.append( Vector(ps1+ps2) )
            
        return ps
    
    ##
    ## Mesh print
    ##
    
    def __str__(self):
        text=[]
        for i in range( len(self) ):
            text.append( str(i+1)+"\t"+self[i].__str__() )
        return "\n".join(text)
    
        
 
