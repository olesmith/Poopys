from Scalar import Scalar
from Vector import Vector

class Matrix(list):
    ##
    ## Matrix creator: allocates and/or initializes
    ##
    
    def __init__(self,A=None,j=None):
        if (A):
            if (A.__class__.__name__=='int'):
                #Just allocate
                if (not j): j=A
                for i in range(A):
                    self.append( Vector(j) )
                    
            elif (A.__class__.__name__ in [ 'list','Matrix' ] ):
                #Copy content!
                for i in range( len(A) ):
                    self.append(Vector([]))
                    for j in range( len(A[i]) ):
                        self[i].append( Scalar(A[i][j]) )
            else:
                print "Matrix.init: Invalid second argument type",A
                exit()
                
    ##
    ## Vector add: per coordinate
    ##
    
    def __add__(A,B):
        if ( len(A)!=len(B) ):
            print "Matrix.add: Incompatible dimensions",len(A),len(B)
            exit()

        C=Matrix()
        for i in range( len(A) ):
            C.append([])
            if ( len(A[i])!=len(B[i]) ):
                print "Matrix.add, row",i,": Incompatible dimensions",len(A[i]),len(B[i])
                exit()
            for j in range( len(A[i]) ):
                C[i].append( Scalar( A[i][j]+B[i][j] ) )

        return C
            
    def __iadd__(A,B):
        return A+B
    
    ##
    ## Matrix sub: per element
    ##
    
    def __sub__(A,B):
        return A+(B*(-1.0))
            
    def __isub__(A,B):
        return u-v
            
    ##
    ## Vector mul: per element
    ##
    
    def __mul__(A,B):
        #Cast int to float
        if (B.__class__.__name__ in [ 'int' ]):
            B=Scalar(B)

        if (B.__class__.__name__ in [ 'float' ]):
            #Multiply by constant
            C=Matrix(A)
            for i in range( len(A) ):
                for j in range( len(A[i]) ):
                    C[i][j]=A[i][j]*B

            return C

        if (B.__class__.__name__ in [ 'Vector' ]):
            v=Vector( len(A) )
            for i in range( len(A) ):
                v[i]=0.0
                for j in range( len(B) ):
                    v[i]+=A[i][j]*B[j]

            return v
        
        if (B.__class__.__name__ in [ 'Matrix' ]):
            C=Matrix( len(A) )
            for i in range( len(A) ):
                for j in range( len(A[i]) ):
                    cij=0.0
                    for k in range( len(B) ):
                        cij+=A[i][k]*B[k][j]
                    C[i].append( cij )

            return C
        
        print "Matrix.mul: Invalid second argument type",B,B.__class__.__name__
        exit()
        
            
    def __imul__(A,B):
        return A*B
     
    ##
    ## Vector neg: opposed Matrix
    ##
    
    def __neg__(A):
        return A*(-1.0)
    
    ##
    ## Matrix print: print as libnes of Vector.
    ##
    
    def __str__(A):
        text=[]
        for i in range( len(A) ):
            text.append( A[i].__str__() )

        return "[\n   "+",\n   ".join(text)+"\n]"
    
