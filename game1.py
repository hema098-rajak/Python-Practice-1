# Lucky Letter Game
print("✨ Welcome to Lucky Letter Game ✨")

name = input("Enter your name: ")

name = name.lower()

a_count = name.count("a")
e_count = name.count("e")

print("\n🔍 Checking your lucky letters...")

print("Count of letter a:", a_count)
print("Count of letter e:", e_count)

if a_count > e_count:
    print("\n🌟 You are very lucky!")
else:
    print("\n🔥 You have strong energy!")

print("\n🎮 Thanks for playing!")