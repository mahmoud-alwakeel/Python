# Clear
setOne = {1,2,3}
setOne.clear()
print(setOne)

# Union
setTwo = {"A", "B", "c"}
setThree = {"1","2","3"}
setX = {"cool", "Great"}
print(setTwo.union(setThree, setX))
print(setTwo | setThree)

setExample = {1, True, "one", (1,2,3)}
print(setExample)


# add
setD = { "one", "two"}
setD.add("Three")
setD.add("Four")
print(setD)


# Remove
# if we entered a value in the remove that it's not in the set it will result in an ERROR
g = {7,8,9}
g.remove(7)
print(g)

# Discard will not cause an error if the element is not in the Set
h = {7,8,9}
h.discard(100)
print(h)
# pop() doesn't take an element
# h.pop(9)
h.pop()
print(h)


# Update like union, Union don't duplicate the likely elements from both sets
setK = {5,6,7}
setX = {7,8,9}
setK.update(["Dart", "Python"])
setK.update({"html", "css"})
setK.update(("AI", "Machine learning"))
setK.update(setX)
print(setK)