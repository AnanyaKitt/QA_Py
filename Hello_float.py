# Round(number[, ndigits])
x = float(input("What's x? "))
y = float(input("What's y? "))

# If digit more than 5, there will round up
#z = round(x + y)

# Round up the ndigit only 2
z = round(x / y, 2)

# Using :, to seperate number
#print(f"{z:,}")
print(z)    #print(f"{z:.2f})
