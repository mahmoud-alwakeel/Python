# difference

setOne = {1,2,3,4}
setTwo = {1,2,"hola", "hello"}
print(setOne)
print(setOne.difference(setTwo)) # setOne - SetTwo
print(setOne)

# difference_update
#  updates SetThree with the elements not in the other set
print("=" * 50)
setThree = {1,2,3,4}
setFour = {1,2,"hola", "hello"}
print(setThree)
setThree.difference_update(setFour) # setThree - setFour
print(setThree)


# Intersection
print("=" * 50)
print("Intersection")
setFive = {1,2,3,4}
setSix = {1,2,"hola", "hello"}
print(setFive.intersection(setSix))
print(setFive & setSix) # & here represents intersection
print(setFive)

# Intersection_update
print("=" * 50)
print("Intersection Update")
setSeven = {1,2,3,4}
setEight = {1,2,"hola", "hello"}
print(setSeven)
setSeven.intersection_update(setEight)
print(f"Set Seven after Intersection Update {setSeven}")
print(setSeven & setEight) # & here represents intersection

# Symmetric Difference
print("=" * 50)
print("Symmetric Difference")
setNine = {1,2,3,4}
setTen = {1,2,"hola", "hello"}
print(f"This prints the symmetric difference between the 2 Sets: {setNine.symmetric_difference(setTen)}")

