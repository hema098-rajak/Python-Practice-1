# Create an empty dictionary dictionary. Allow 4 friends to enter their favorite languages as value and use key as their names.Assume that names are uniue. 
s = {}
name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})

print(s)

