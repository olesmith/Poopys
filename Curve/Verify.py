from Canvas2 import Canvas2


class Curve_Verify():
    def __Verify__(self,tell=False):
        print "Verify:",", ".join(   self.Curve_Types_Verify()   )
        
        deviations={}
        for ttype in self.Curve_Types_Verify():
            if (self.Curve_Type_Has_Analytical(ttype)):
                if (tell): print "__Verify__:",ttype,tell
                line=self.Curve_Run_Method_Type(ttype,"Verify",tell)
                line=line[0]
                res=line[1]
                deviations[ ttype ]=res

        return deviations
    
    def Verify_Mesh_Type(self,type,tell=False):
        attr_num=type+"s_Num"
        attr_ana=type+"s_Ana"
        
        mesh_num=getattr(self,attr_num)
        mesh_ana=getattr(self,attr_ana)
        if (mesh_ana==None):
            return 0.0,0.0,[0.0,0.0]

        return mesh_num.Meshes_Compare(mesh_ana,tell)
