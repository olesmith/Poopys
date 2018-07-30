from File import *

class Curve_Write():
    def __Write__(self):
        self.Rs_Write()
        self.dRs_Write()
        self.d2Rs_Write()
        self.d3Rs_Write()
        
        self.v2s_Write()
        self.Ts_Write()
        self.Ns_Write()
        
        self.VNs_Write()
        self.Dets_Write()
        self.Phis_Write()
        self.Kappas_Write()
        self.Rhos_Write()
        
        self.RhoVs_Write()
        self.Evolutes_Write()
        self.dEvolutes_Write()
        
        self.Evolute_Singulars_Write()

    def Rs_Write(self):
        self.Rs.Mesh_Write(   self.Curve_File_Name("d0R.txt")   )
        
       
    def d2Rs_Write(self):
        if (self.d2Rs_Num):
            self.d2Rs_Num.Mesh_Write(   self.Curve_File_Name("d2R.N.txt")   )
            
        if (self.d2Rs_Ana):
            self.d2Rs_Ana.Mesh_Write(   self.Curve_File_Name("d2R.A.txt")   )
        
    def d3Rs_Write(self):
        if (self.d3Rs_Num):
            self.d3Rs_Num.Mesh_Write(   self.Curve_File_Name("d3R.N.txt")   )

        if (self.d3Rs_Ana):
            self.d3Rs_Ana.Mesh_Write(   self.Curve_File_Name("d3R.A.txt")   )
        
    def v2s_Write(self):
        if (self.v2s_Num):
            self.v2s_Num.Mesh_Write(   self.Curve_File_Name("v2.N.txt")   )
        
        if (self.v2s_Ana):
            self.v2s_Ana.Mesh_Write(   self.Curve_File_Name("v2.A.txt")   )

    def Ts_Write(self):
        if (self.Ts_Num):
            self.Ts_Num.Mesh_Write(   self.Curve_File_Name("T.N.txt")   )

        if (self.Ts_Ana):
            self.Ts_Ana.Mesh_Write(   self.Curve_File_Name("T.A.txt")   )

    def Ns_Write(self):
        if (self.Ns_Num):
            self.Ns_Num.Mesh_Write(   self.Curve_File_Name("N.N.txt")   )

        if (self.Ns_Ana):
            self.Ns_Ana.Mesh_Write(   self.Curve_File_Name("N.A.txt")   )

    def VNs_Write(self):
        if (self.VNs_Num):
            self.VNs_Num.Mesh_Write(   self.Curve_File_Name("VN.N.txt")   )

        if (self.VNs_Ana):
            self.VNs_Ana.Mesh_Write(   self.Curve_File_Name("VN.A.txt")   )

    def Dets_Write(self):
        if (self.Dets_Num):
            self.Dets_Num.Mesh_Write(   self.Curve_File_Name("Det.N.txt")   )

        if (self.Dets_Ana):
            self.Dets_Ana.Mesh_Write(   self.Curve_File_Name("Det.A.txt")   )

    def Phis_Write(self):
        if (self.Phis_Num):
            self.Phis_Num.Mesh_Write(   self.Curve_File_Name("Phi.N.txt")   )

        if (self.Phis_Ana):
            self.Phis_Ana.Mesh_Write(   self.Curve_File_Name("Phi.A.txt")   )

    def Kappas_Write(self):
        if (self.Kappas_Num):
            self.Kappas_Num.Mesh_Write(   self.Curve_File_Name("Kappa.N.txt")   )

        if (self.Kappas_Ana):
            self.Kappas_Ana.Mesh_Write(   self.Curve_File_Name("Kappa.A.txt")   )

    def Rhos_Write(self):
        if (self.Rhos_Num):
            self.Rhos_Num.Mesh_Write(   self.Curve_File_Name("Rho.N.txt")   )

        if (self.Rhos_Ana):
            self.Rhos_Ana.Mesh_Write(   self.Curve_File_Name("Rho.A.txt")   )

    def RhoVs_Write(self):
        if (self.RhoVs_Num):
            self.RhoVs_Num.Mesh_Write(   self.Curve_File_Name("RhoV.N.txt")   )

        if (self.RhoVs_Ana):
            self.RhoVs_Ana.Mesh_Write(   self.Curve_File_Name("RhoV.A.txt")   )

    def Evolutes_Write(self):
        if (self.Evolutes_Num):
            self.Evolutes_Num.Mesh_Write(   self.Curve_File_Name("Evolute.N.txt")   )

        if (self.Evolutes_Ana):
            self.Evolutes_Ana.Mesh_Write(   self.Curve_File_Name("Evolute.A.txt")   )

    def dEvolutes_Write(self):
        if (self.dEvolutes_Num):
            self.dEvolutes_Num.Mesh_Write(   self.Curve_File_Name("dEvolute.N.txt")   )

        if (self.dEvolutes_Ana):
            self.dEvolutes_Ana.Mesh_Write(   self.Curve_File_Name("dEvolute.A.txt")   )

