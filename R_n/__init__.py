from math import *

from Scalar import Scalar
from Vector import Vector
from Matrix import Matrix
from Mesh import Mesh
from Function import Function


def O(n=2):
    return Vector(n)

def I(n=2):
    i=Vector(n)
    i[0]=1.0
    
    return i

def J(n=2):
    j=Vector(n)
    j[1]=1.0
    
    return j

def K(n=3):
    k=Vector(n)
    k[2]=1.0
    
    return k


def E(t,omega=1.0,gamma=0.0):
    tt=omega*t+gamma
    return Vector([ cos(tt),sin(tt) ])

def F(t,omega=1.0,gamma=0.0):
    tt=omega*t+gamma
    return Vector([ -sin(tt),cos(tt) ])

def P(t,omega=1.0,gamma=0.0):
    tt=omega*t+gamma
    return Vector([ -cos(tt),sin(tt) ])

def Q(t,omega=1.0,gamma=0.0):
    tt=omega*t+gamma
    return Vector([ -sin(tt),-cos(tt) ])

##
## Identity matrix or n'th order
##
    
def Matrix_Identity(n):
    I=Matrix(n,n)
    for i in range(n): I[i][i]=1.0

    return I

##
## Matrix print: print as libnes of Vector.
##
    
def Matrix_Rotation(n,theta):
    I=Matrix(n,n)
    if (n==2):
        return Matrix([
            [ cos(theta),-sin(theta)],
            [ sin(theta), cos(theta)],
        ])
    return I
