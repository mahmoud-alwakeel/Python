# all()

x = [1, 2, 3, 4, []] 

if all(x): # -> False
    print("X: all elements are True")
else:
    print("X: at least one element is False")

y = [1, 2, 3, 4] 

if all(y): # -> True
    print("Y: all elements are True")
else:
    print("Y: at least one element is False")


# any()
z = [1, 2, 3, 4, []] # -> True

if any(z):
    print("Z: at least one element is True")
else:
    print("Z: all elements are False")

a = [0, 0, []] # -> True

if any(a):
    print("Z: at least one element is True")
else:
    print("Z: all elements are False")


# bin()
print(bin(100))

# id()
b = 1
c = 2

print(id(b))
print(id(c))