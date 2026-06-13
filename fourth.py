#program to store fruits in a list entered by the user.
fruits = []

f1 = input("enter fruit name : ")
fruits.append(f1)
f2 = input("enter fruit name : ")
fruits.append(f2)
f3 = input("enter fruit name : ")
fruits.append(f3)
f4 = input("enter fruit name : ")
fruits.append(f4)
f5 = input("enter fruit name : ")
fruits.append(f5)
f6 = input("enter fruit name : ")
fruits.append(f6)
f7 = input("enter fruit name : ")
fruits.append(f7)
print(fruits)


#Program to accept marks of 6 students and display them in a sorted manner. 
marks = []
m1 = int(input("enter marks : "))
marks.append(m1)
m2 = int(input("enter marks : "))
marks.append(m2)
m3 = int(input("enter marks : "))
marks.append(m3)
m4 = int(input("enter marks : "))
marks.append(m4)
m5 = int(input("enter marks : "))
marks.append(m5)
m6 = int(input("enter marks : "))
marks.append(m6)
marks.sort()
print(marks)

# Check that tuple type cannot be changed.
a = ["hema", 2, 'a']
a[2] = "Hema" # Assidgnment cannot be done as tuples are immutable.


# Program to sum a list with 4 numbers.
list = (1,2,3,4)
print(sum(list))

#Program to count the number of zeros in the tuple.
a = (0, 10, 22,33,00)
n = a.count(0)
print(n)

