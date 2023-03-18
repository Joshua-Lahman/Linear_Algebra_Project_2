#Part 1
#Joshua Lahman
#Programming Assignment 2

#delare variables
p1 = 0 
p2 = 0
v1 = 0
v2 = 0
a = 0
b = 0
c = 0
loop = True

#ask user for implicit or parametic
while (loop):
    eqForm = input("Enter i to convert from implicit and p to convert from implicit: ")


    #get input from user
    if (eqForm == "p"): #parametric -> implicit
        print("l(t) = p + tv")
        p1 = int(input("please enter p1: "))
        p2 = int(input("please enter p2: "))
        v1 = int(input("please enter v1: "))
        v2 = int(input("please enter v2: "))
        loop = False

    elif (eqForm == "i"): #implicit -> parametric
        print("ax1 + bx2 + c = 0")
        a = int(input("please enter a: "))
        b = int(input("please enter b: "))
        c = int(input("please enter c: "))
        loop = False
    else :
        continue

#parametric -> implicit
if (eqForm == "p"):
    if (v2 == 0):
        a1 = v2
        a2 = -1*v1
    else :
        a1 = -1*v2
        a2 = v1
    c = -1*((a1*p1) + (a2*p2))

    #find signs for implicit equation
    #x1 sign will be inclcuded/excluded automatically
    if (a2>=0):
        x2Sign = "+"
    else:
        x2Sign = ""
    if (c>=0):
        x3Sign = "+"
    else:
        x3Sign = ""
    #display implicit    
    print(str(a1) + "x1 " + x2Sign + " " + str(a2) + "x2 " + x3Sign + " " + str(c) + " = 0")

#implicit -> parametric
else :
    if (abs(a) >= abs(b)) :
        p1 = (-1*c)/a
        p2 = 0
    else :
        p1 = 0
        p2 = (-1*c)/b

    #check for zero value
    if (v1==0) :
        v1 = b
        v2 = -1*a
    else :
        v1 = -1*b
        v2 = a

    #display parametric        
    print("L(t) = [" + str(p1) + " " + str(p2) +"] + t[" + str(v1) + " " + str(v2) +"] = 0")