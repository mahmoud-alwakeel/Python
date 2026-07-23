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