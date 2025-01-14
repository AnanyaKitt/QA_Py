# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str and capitalize user's name
name = name.strip().title()
 
# Capitalize user's name
#name = name.capitalize()    #title()

# Say Hello to user
print("Hello, ")
print(name) 
print(f"hello, {name}")
