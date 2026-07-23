# Tuples with one element and how differentiate between it and a String for a tuple with a single item

# these will be of Type String
tuple1 = "Weka"
tuple2 = ("Weka")

#  But if we added a comma after it we will make it's type tuple
tuple3 = "Weka",
tuple4 = ("Weka",)

# strings
print(type(tuple1))
print(type(tuple2))

# tuples
print(type(tuple4))
print(type(tuple3))


tupleA = (1,2,3)
tupleB = (4, 5, 6, 6, 6, 6)
tupleC = tupleA + tupleB
print(tupleC)

# Count, we want to know how many times is this element is in a tuple
print(tupleB.count(6))

#  to find the index of this element
print(f"The position of element '5' is: {tupleB.index(5)}")

# This will result in an error we cannot concatenate a string with a number
# print("The position of element '5' is: " + tupleB.index(5))


# Destruct
#  if tuple len is bigger than the var we assign the tuple to we will get an error, instead we can place an "_" for this variable
tuple9 = ("A", "b", "c")
x, y, z = tuple9
print(x)
print(y)
print(z)

print("="*50)
print("tuple 10:")
tuple10 = ("A", "b", 4, "c")
h, i, _, j = tuple10
print(h)
print(i)
print(j)

tupleOne = ([1,2,3], 1, 2, 4)
print(tupleOne)
