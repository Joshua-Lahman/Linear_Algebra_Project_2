#Part 3
#Joshua Lahman
#Programming Assignment 2

#Write a program to determine the linear map used
#to map a source triangle to a target triangle given the 
#vertices of both triangles. 

#display sample triangle
print("Please enter 3 verticies: ")
print("[b1,1] [b2,1] [b3,1]")
print("[b1,2] [b2,2] [b3,2]")

#recieve triangle input
b11=float(input("b1,1 = "))
b12=float(input("b1,2 = "))
b21=float(input("b2,1 = "))
b22=float(input("b2,2 = "))
b31=float(input("b3,1 = "))
b32=float(input("b3,2 = "))

print("Triangle B: ")
print("[" + str(b11) +"] [" + str(b21) + "] [" + str(b31) + "]")
print("[" + str(b12) +"] [" + str(b22) + "] [" + str(b32) + "]")


#display sample triangle again
print("Please enter 3 verticies: ")
print("[c1,1] [c2,1] [c3,1]")
print("[c1,2] [c2,2] [c3,2]")

#recieve second triangle input
c11=float(input("c1,1 = "))
c12=float(input("c1,2 = "))
c21=float(input("c2,1 = "))
c22=float(input("c2,2 = "))
c31=float(input("c3,1 = "))
c32=float(input("c3,2 = "))

#display second triangle
print("Triangle C: ")
print("[" + str(c11) +"] [" + str(c21) + "] [" + str(c31) + "]")
print("[" + str(c12) +"] [" + str(c22) + "] [" + str(c32) + "]")

#calculate first triangle matrix
v11 = b21 - b11
v21 = b22 - b12
v12 = b31 - b11
v22 = b32 - b12

#display first triangle matrix V
print("First Triangel Matrix V: ")
print("[" + str(v11) + " " + str(v12) + "]")
print("[" + str(v21) + " " + str(v22) + "]")

#calculate second triangle matrix
w11 = c21 - c11
w21 = c22 - c12
w12 = c31 - c11
w22 = c32 - c12

#display second triangle matrix w
print("Second Triangle Matrix W: ")
print("[" + str(w11) + " " + str(w12) + "]")
print("[" + str(w21) + " " + str(w22) + "]")
     
#find det of 1st triangle matrix, if == 0 then no inverse exists
det = (v11*v22) - (v21*v12)

if (det == 0) :
    print("Inverse does not exist")

else :
    #calculate inverse
    i11 = v22/((v11*v22)-(v21*v12))
    i21 = (1/(((-1*v21*v12) / v11) + v22)) * (-1*v21) / v11
    i12 = -1*v12/((v11*v22)-(v21*v12))
    i22 = 1/(((-1*v21*v12)/v11) + v22)

    #print the inverse    
    print("Your inverse matrix: ")
    print("[" + str(float(i11)) + " " + str(float(i12)) + "]")
    print("[" + str(float(i21)) + " " + str(float(i22)) + "]")

#calculate Affine Map using dot product
a11 = w11*i11 + w12*i21
a21 = w21*i11 + w22*i21
a12 = w11*i12 + w12*i22
a22 = w21*i12 + w22*i22

#display affine map
print("Affine Map: ")
print("[" + str(a11) + " " + str(a12) + "]")
print("[" + str(a21) + " " + str(a22) + "]")