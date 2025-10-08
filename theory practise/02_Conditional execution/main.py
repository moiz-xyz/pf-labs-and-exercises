 
#  basics
print("hello")

a = "Moiz"

if (a == "Moiz") :
    print(a)
else :
    print("hadin")

#  Boolean expressions
a = 10
b = 20 

if (a == b):
    print(True)
else :
    print (False)
print(type(True))


# Logical operators
a = 10
b = 20

x = 90
y = 60
if(a  > b and x == y) :
    print(True) 
else:
    print(False)

# Chained conditionals
marks = 78
if ( marks >= 80) :
    print("Grade is A")
elif (marks >= 70) :
    print("Grade is B")
else : 
    print("You are fail")

# Nested condtionals 
age = 22 
has_ID = False
if age > 19:
    if has_ID:
        print("You can enter")
    else :
        print("You need ID to enter")
else :
    print("You are under 18")

marks = 90

if (marks < 100) :
    if(marks > 80) :
        print("Grade is A")
    # if(marks > 70) :
    elif(marks > 70) :
        print("Youa are fai")

else :
    print("Ivalid marks")
    

# Catching exceptions using try and except
try:
    number = int(input("What is your age"))
    print("Your umber is" , input)
except:
    print("enter a valid number")

#  a code to test
a = 10 + 12
print(a) 
