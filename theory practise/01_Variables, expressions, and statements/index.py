# 1.1 Values and types
print(2)     

print(type("Hello world"))
print(type(19))
print(type(12.3))
# print(type(1000,0000,000))

# 1.2 variables

message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931

print(n)
print(message)
print(pi)

print(type(n))


# 1.3 Statements
print(122)
x = 100
print(x)

# 1.4 Operators and operands
add =  3 + 5
print(add)

sub = 10-3
print(sub)

multi = 10*2
print(multi)

divide = 10 /5
print(divide)

floor = 10 // 3
print(floor)

# 1.5 expression 

5
x = 5
x + 1
print(x)


# 1.6 Order of operations  (PEMDAS)
# 1) Parentheses
# 2) Exponentiation
# 3) Multiplication 
# 4) Division
# 5) Addition
# 6) Subtraction


#  Exercises

# Write a program that uses input to prompt a user for their
# name and then welcomes them.

name = str(input("Enter your name"))
print("Hello" , name)

# Write a program to prompt the user for hours and rate per
# hour to compute gross pay
rate = int(input("What is your rate per hour"))
hours = int(input("How many hours did you worked"))

gross_pay = float(rate * hours)
print(gross_pay)


# Assume that we execute the following assignment statements:
width = 17
height = 12.0

# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).

# 1. width//2
x = width//2
print(x)
print(type(x))

# 2. width/2.0
y = width/2.0
print(y)
print(type(y))

# 3. height/3
b = height/3
print(b)
print(type(b))

# 4. 1 + 2 * 5
a = 4.1 + 2 * 5
print(a)
print(type(a))

# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
# converted temperature.

celsius_temp = int(input("Enter the temperature in Celsius"))
fahrenheit_temp = (celsius_temp * 1.8) + 32
print( celsius_temp,"°C is" , float(fahrenheit_temp) ,"in °F.")