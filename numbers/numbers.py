# Int
print("Int")
print(type(1))
print(type(100))
print(type(-1))
print(type(-100))

# Float
print("Float")
print(type(-1.5))
print(type(1.5))
print(type(100.5))
print(type(-100.5))

# Complex
print("Complex")
print(type(5+6j))
complexNum = 5+6j
print(f"Real Part is {complexNum.real}")
print(f"Imaginary Part is {complexNum.imag}")


# We can convert from Int to Float and vice versa
# We can convert from Int to Complex 
# We can convert from Float to Complex 
# We cannot covert from Complex to any other type

print(100)
print(float(100))
print(complex(100))
print(11.11)
print(int(11.11))
print(complex(11.11))

#  This will result in an ERROR cann't convert complex to int
# print(int(10+9j))