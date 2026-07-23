tuple1 = (1, 2, 3)
print(tuple1)

# we can remove thetuple parantheses
tuple2 = 1, 2, 3
print(tuple2)
print(type(tuple2))


tuple3 = (1, 2, 3, 4, 5)

print(tuple3)
print(tuple3[1])
print(tuple3[0])
print(tuple3[-1])
print(tuple3[1:3])

# Tuples are immutable we can't edit it
#  we will get: TypeError: 'tuple' object does not support item assignment
# tuple3[1] = 99

#  ERROR: AttributeError: 'tuple' object has no attribute 'clear'
# tuple3.clear()
# print(tuple3)

tuple4 = (1, "one", True, -100)
print(tuple4)
