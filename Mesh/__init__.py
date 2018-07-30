from File import *
from R_n import *
from XML import *
from Canvas2 import Canvas2

from svg import Mesh_SVG

class Mesh(
        list,XML,
        Mesh_SVG
    ):
    Title="Undef"
    Name="Undef"
    Type="Undef"
    
    __Canvas__=None
    
    def __init__(self,n,mname,mtype,args={}):
        self.Name=mname
        self.Type=mtype
        nn=len(self)
        while (nn<n):
            self.append(None)
            nn+=1
            
        self.__Init__(args)
        
        return

    def Map(self,A):
        mesh=Mesh(len(self),self.Name,self.Type)
        mesh.__Canvas__=self.__Canvas__

        for i in range( len(self) ):
            p=self[i]
            pp=None
            if (p!=None):
                pp=p*A
            mesh[i]=pp

        return mesh
    
    def Show(self,other=None):
        for i in range( len(self) ):
            if (other!=None):
                print i,self[i],other[i]
            else:
                print i,self[i]
                
    def __str__(self):
        comps=[
            "Mesh:",
            "Name="+self.Name,
            "Type="+self.Type,
            "len="+str(len(self)),
            "min="+str(self.Min()),
            "max="+str(self.Max()),
        ]
        return " ".join(comps)
        
    
    def __add__(self,mesh):
        rmesh=Mesh( len(self) )
        for n in range( len(self) ):
            p=None
            if (self[n] and mesh[n]):
                print n,self[n],mesh[n]
                p=self[n]+mesh[n]
            rmesh.append(p)
        return rmesh

    def __Init__(self,args):
        for key in args.keys():
            setattr(self,key,args[key])
            
    def Max(self,meshes=[]):
        big=1.0E6
        vmax=Vector([-big,-big])
        for i in range( len(self) ):
            if (self[i]):
                vmax=vmax.Max(self[i])

        for mesh in meshes:
            vmax=vmax.Max( mesh.Max() )
    
        return vmax.Max( Vector([1.0,1.0]) )
                
    def Min(self,meshes=[]):
        big=1.0E6
        vmin=Vector([big,big])
        for i in range( len(self) ):
            if (self[i]):
                vmin=vmin.Min(self[i])

        for mesh in meshes:
            vmin=vmin.Min( mesh.Min() )
            
        return vmin.Min( Vector([-1.0,-1.0]) )
                
    def Mesh_Write(self,fname):
        lines=[]
        for n in range( len(self) ):
            comps=[str(n)]
            if (self[n].__class__.__name__!='Vector'):
                comps.append( "undef" )
                lines.append( "\t".join(comps) )
                continue
            
            for x in self[n]:
                comps.append( "%.6f" % x )
                
            lines.append( "\t".join(comps) )

        res=File_Write(fname,lines)
    
    ##!
    ##! Set canvas by internal values.
    ##!
    
    def Mesh_Canvas_Init(self,resolution):
        if (resolution.__class__.__name__=="Canvas2"):
            self.__Canvas__=resolution
        else:
            self.__Canvas__=Canvas2(self.Min(),self.Max(),resolution)

        
    ##!
    ##! Set canvas by external values.
    ##!

    def Mesh_Canvas(self,canvas=None):
        if (canvas!=None): self.__Canvas__=canvas

        return self.__Canvas__
    
    def Norm(self,p=2.0):
        norm=0.0
        for i in range( len(self) ):
            if (self[i]):
                rnorm=self[i].Norm(p)
                if (rnorm>norm): norm=rnorm
            
        return norm
                
    def Ellipse(self,c=None,axis=None,N=100):
        if (c==None): c=O()
        if (axis==None): axis=Vector([1.0,1.0])
        if (axis.__class__.__name__=='float'): axis=Vector([axis,axis])
        
        ellipse=Mesh(N+1,"Circle","Aux")
        ellipse.__Canvas__=self.__Canvas__

        dt=2*pi/(1.0*N)
        t=0.0
        for n in range(N+1):
            ellipse[n]=c+Vector([ axis[0]*cos(t),axis[1]*sin(t) ])
            t+=dt

        return ellipse
                
    def Circle(self,c=None,r=None,N=100):
        if (r==None): r=1.0

        circle=Mesh(N+1,"Circle","Aux")
        circle.__Canvas__=self.__Canvas__

        dt=2*pi/(1.0*N)
        t=0.0
        for n in range(N+1):
            circle[n]=c+Vector([ cos(t),sin(t) ])*r
            t+=dt

        print circle
        return circle
        

    def Meshes_Compare(mesh1,mesh2,tell=False,showmax=None):
        mesh=Mesh(
            len(mesh1),
            mesh1.Name+"_Diff",
            mesh1.Type+"_Diff"
        )

        maxdev=0.0
        maxx=1.0
        maxv=Vector([0.0,0.0])
        for n in range( len(mesh1) ):
            if (mesh1[n]!=None and mesh2[n]!=None):
                mesh[n]=mesh2[n]-mesh1[n]
                maxdev=max(maxdev,mesh[n].Length())
                maxx=max(maxx,mesh2[n].Length())

                maxv=maxv.Abs_Max(mesh[n])
                if (tell):
                    print n,mesh1[n],mesh2[n],mesh[n],mesh[n].Length()

                elif (showmax!=None and mesh[n].Length()>showmax):
                    print n,mesh1[n],mesh2[n],mesh[n],mesh[n].Length()
                    

        maxx*=1.0*len(mesh1)
        return maxdev/maxx,mesh,maxv
                
