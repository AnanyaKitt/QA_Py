"""
# Use if else
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindoor")

elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
"""

# Also can use match name
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")    