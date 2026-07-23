stringOne = "My name is Weka"

print(stringOne[0])
print(stringOne[1])
print(stringOne[2])
print(stringOne[3])
print(stringOne[4])
print(stringOne[5])
print(stringOne[6])
print(stringOne[7])
# prints the last element
print(stringOne[-1])
# this will result in ERROR!: IndexError: string index out of range
# print(stringOne[100])

print("=" * 50)
string2 = "I love Python"
# IMPORTANT "5" is NOT including so this prints 1 -> 4
# [start:end:steps]
print(string2[0:5])
# from start till the end with a step of 2 
print(string2[0::2])
#  if start is not typed it will automatically start from 0 
print(string2[::2])
#  print full data
print(string2[:])