# Is Super set & subset
setOne = {1,2,3,4}
setTwo = {1,2,3, 4, "hola", "hello"}
print(f"Checking if setTwo is superset: {setTwo.issuperset(setOne)}") 
print(f"Checking if setOne is subset of set Two: {setOne.issubset(setTwo)}") 

# Disjoint
setThree = {1,2,3,4}
setFour = {1,2,3, 4, 5}
setFive = {10, 11, 12}
print(f"Checking if the two sets are disjoint: {setThree.isdisjoint(setFour)}") 
print(f"Checking if the two sets are disjoint: {setThree.isdisjoint(setFive)}") 