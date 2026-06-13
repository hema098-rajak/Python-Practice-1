# 1. program to find remainder when a number is divided by z.
a =  int(input("Enter a: "))
b = int(input("Enter b : "))
remainder = a % b
print(remainder)


#2.  check the type of variable assigned using input () function. 
a = input("Enter value of a: ")
print(type(a))
# Note the output of this Questio will always show a string type. 
# Further we can convert it into other types.


#3. use comparison operator to find out whether a given variable a is greater than or not.
a = input("Enter Value of a : ")
b = input("Enter the Value of b : ")
c = a>b
print(c) 
# or another solution
a = input("Enter a: ")
b = input("Enter b: ")
print("a is greater than b is : ", a>b)


#4. Python Program to find an Average of Two Numbers entered by the user.
a = int(input("Enter a : "))
b = int(input("Enter b : "))
average = (a+b)/2
print(average)
#or another solution
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("Average is :",(a+b)/2)



#5. Write a Python Program to calculate the square of a number entered by the user.
a = int(input("Enter the Number : "))
square_of_a = a*a
print(square_of_a)
#or another solution 
a = int(input("Enter the Number : "))
print("Sqare of Number : ",a**2)        #a*a also valid.But a^a is not valid in python. 

