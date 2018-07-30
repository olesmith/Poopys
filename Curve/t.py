from Vector import Vector

class Curve_t():
    ##!
    ##! Calculate parameter values.
    ##! Store in self.ts.
    ##!

    ts=[]
    
    def Calc_ts(self):
        dt=(self.t2-self.t1)/(1.0*(self.N-1))
        self.ts=list([])

        t=self.t1
        for n in range(self.N):
            self.ts.append(t)
            t+=dt
