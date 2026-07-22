# Python is a dynamically typed language, which means that we do not have to declare the type of a variable when we create it. 
# The type of a variable is determined by the value that is assigned to it.
x = 10
print(x)

# We can change the type of a variable by assigning a value of a different type to it.
x = "Hello"
print(x)


a, b, c = 1, 2, 3
print(a, b, c)
# reserved keywords are words that have a special meaning in Python and cannot be used as variable names.
# help("keywords")

# this will result in ValueError: not enough values to unpack (expected 3, got 2)
# e, f, g = 4, 5
# print(e, f, g)

# this will result in ValueError: too many values to unpack (expected 3, got 4)
e, f, g = 4, 5, 6, 7
print(e, f, g)
