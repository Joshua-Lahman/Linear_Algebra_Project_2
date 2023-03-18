#Part 2
#Joshua Lahman
#Programming Assignment 2

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

#find det, if == 0 then no inverse exists
det = (a11*a22) - (a21*a12)

if (det == 0) :
    print("Inverse does not exist")

else :
    #calculate inverse
    i11 = a22/((a11*a22)-(a21*a12))
    i21 = (1/(((-1*a21*a12) / a11) + a22)) * (-1*a21) / a11
    i12 = -1*a12/((a11*a22)-(a21*a12))
    i22 = 1/(((-1*a21*a12)/a11) + a22)

    #print the inverse    
    print("Your inverse matrix: ")
    print("[" + str(float(i11)) + " " + str(float(i12)) + "]")
    print("[" + str(float(i21)) + " " + str(float(i22)) + "]")