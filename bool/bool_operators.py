age = 25
country = "Eg"

print("And -> all parts must be true in order to evaluate to True")
print( age > 18 and country == "Eg")
print( age > 18 and country == "USA")


print("Or -> any part that is true will evaluate to True")
print( age > 18 or country == "Eg")
print( age > 18 or country == "USA")

print("Not -> if it was supposed to be True Not will make it False")
print(not age > 18)