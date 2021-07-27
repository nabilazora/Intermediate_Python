# Adding a placeholder
# number = 25
# newmsg = "The number is {} for you!"
# print(newmsg.format(number))

# Displayed as a number with two decimals
# number = 25
# newmsg = "The number is {:.2f} for you!"
# print(newmsg.format(number))

# Adding Multiple Placeholders
# quantity = 5
# itemNumber = 50
# price = 24
# firstOder = "We want {} pieces of item number {} for {:.2f} dollars."

# print(firstOder.format(quantity, itemNumber, price))

# Using index numbers
quantity = 5
itemNumber = 50
price = 24
firstOder = "We want {0} pieces of item number {1} for {2:.2f} dollars."

print(firstOder.format(quantity, itemNumber, price))

age = 45
name = "Jack"
newTxt = "The name is {1}. {1} is {0} years old."

print(newTxt.format(age, name))

# Using named indexes by entering a name inside the curly brackets
newOrder = "I have a {car}, it is a {model}"
print(newOrder.format(car = "Volvo", model = "S60"))