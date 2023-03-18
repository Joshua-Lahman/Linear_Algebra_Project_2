#Part 4
#Joshua Lahman
#Programming Assignment 2

import math

def quadf(a,b,c):
    square = math.sqrt((b*b) - (4*a*c))
    x1 = ((-1*b) + square) / 2*a
    x2 = ((-1*b) - square) / 2*a
    return[x1,x2]

def eigenv(b11,b21):

    w11 = 1
    w21 = ((-1*b21)/b11)
    w12 = 0
    w22 = 1

    #compute dot product (what we need of it)
    c11 = w11*b11 + w12*b21
    c21 = w21*b11 + w22*b21

    #find vector r
    r1 = 1 #let r1 = 1
    r2 = -1*(c21/c11)

    return [r1,r2]

#display sample matrix
print("Please enter a 2x2 matrix: ")
print("[a11 a12]")
print("[a21 a22]")

#recieve matrix input
a11=float(input("a11 = "))
a21=float(input("a21 = "))
a12=float(input("a12 = "))
a22=float(input("a22 = "))

#display entered matrix
print("Your matrix: ")
print("[" + str(a11) + " " + str(a12) + "]")
print("[" + str(a21) + " " + str(a22) + "]")


#find eigen values----------------
#characteristic equation
a = 1.0
b = (-1*(a11+a22))
c = (a11*a22 - a21*a12)

#use quadratic formula to find lamba values
[x1,x2] = quadf(a,b,c)
if (abs(x1)>abs(x2)):
    domLam = x1
    lam2 = x2
else :
    domLam = x2
    lam2 = x1

print("Characteristic Equation: ")
print(str(a) + "Lambda^2 - " + str(b) + "Lambda + " + str(c))

print("Lambda 1: ")
print(str(domLam))

print("Lambda 2: ")
print(str(lam2))

print("Dominant Eigenvalue: ")
print(str(domLam))

#Find Eigen Vectors---------------
#create new matrix using Lambda1
b11 = a11 - domLam
b21 = a21
b12 = a12
b22 = a22 - domLam

#print new Lambda1 matrix
print("Matrix minus Lambda1: ")
print("[" + str(b11) + " " + str(b12) + "]")
print("[" + str(b21) + " " + str(b22) + "]")



#create new matrix using Lambda2
d11 = a11 - lam2
d21 = a21
d12 = a12
d22 = a22 - lam2

#print new Lambda2 matrix
print("Matrix minus Lambda2: ")
print("[" + str(d11) + " " + str(d12) + "]")
print("[" + str(d21) + " " + str(d22) + "]")

#find dominent eigen vector
[r1,r2] = eigenv(b11,b21)
#find second eigen vector
[s1,s2] = eigenv(d11,d21)

#display vectors
print("Dominate Eigen Vector: ")
print("r1 = c[" + str(r1) + " , " + str(r2) + "]")
print("Second Eigen Vector: ")
print("r2 = c[" + str(s1) + " , " + str(s2) + "]")