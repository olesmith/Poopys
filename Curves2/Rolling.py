from math import *
import re,sys
sys.path.insert(0,'/root/python')

from System import *
from File import *

from R_n import *
from Curve import Curve

#Implements rolling part.

class Rolling():
    __Curve_Base__=None

    r=1.0
    Lambda=1.0

    __R__={}
    
    ##!
    ##! Reset storage for the Rs.
    ##!
    def Curve_Init_Parameters(self):

        self.__R__={}
        return
    ##!
    ##! Initialize base curve: the x-axis
    ##!

    def Curve_Base(self):
        if (self.__Curve_Base__==None):
            print "Base"
            self.__Curve_Base__=self.Curve_Base_Get()

        return self.__Curve_Base__
    
    ##!
    ##! Calculate Rotation angle
    ##!

    def Rotation_Angle(self,t):
        return -self.Curve_Base().S(t)/self.r
    
    ##!
    ##! Calculate I matrix
    ##!

    def Rotation_I(self):
        return Matrix([
            [ 1.0,0.0 ],
            [ 0.0,1.0 ],
        ])
    
    ##!
    ##! Calculate Rotation matrix
    ##!

    def Rotation_Matrix(self,theta):
        return Matrix([
            [ cos(theta),-sin(theta) ],
            [ sin(theta),cos(theta) ],
        ])
    
    ##!
    ##! Calculate R
    ##!

    def R(self,t):
        tt=str(t)
        if (not self.__R__.has_key(tt)):
            n=self.Curve_Base().n(t)
            r=self.Curve_Base().R(t)
            theta=self.Rotation_Angle(t)

            rolling_center=r+n*self.r
            M=Matrix_Rotation(2,theta)

            rotated_vector=M*(  n*(  self.r*self.Lambda  )  )

            self.__R__[ tt ]=rolling_center-rotated_vector
            
        return self.__R__[ tt ]
        
    ##!
    ##! Override Rolling_Center(t):
    ##!
    ##! Calculate Rolling Center
    ##!

    def Rolling_Center(self,t):
        return self.R(t)
        rolling_center=I()*self.rolling_t+J()

        return rolling_center*self.r

    
