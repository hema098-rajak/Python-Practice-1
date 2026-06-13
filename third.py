# 1. Python Program to Display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name: ")
print("Good Afternoon " + name + "!")
#or Another Solution
name = input("Enter your name: ")
print(f"Good Afternoon {name}")


#2. Write a program to fill in a letter template given below with name and date. 
#   letter = '''
#   Dear <|Name|>,
#   You are Selected. 
#   <|Date|>
#   '''

letter = '''Dear <|Name|>,
You are Selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Hema").replace("<|Date|>","2026"))  #chaining of .replace


#3. Program to detect double space in a string.
a = "Hema is a good  girl  "
print(a.find("  "))

#4. replace the Double Space from single spaces.
a = "Hema is a good  girl  "
print(a.replace("  "," "))

#5. Program to format the following letter using escape sequence characters.
letter = "Dear Riku, this python course is nice. Thanks!"
letter = "Dear Riku,\n\t This python course is nice. \n Thanks!"
print(letter)
