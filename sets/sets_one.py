# sets are not ordered, so we cannot perform indexing or slicing
setOne = {1, "weka", -100, 55}
print(setOne)

# set has only immutable data types "number, Strings, tuples" But List and Dict are not
# ERROR: TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# setTwo = {1,2,3, [1,2,3]} # (unhashable type: 'list')
setTwo = {1,2,3, (1,2,3)} 
print(setTwo)

#  Items are Unique
setThree = {1,1,1, 2, 3}
print(setThree) # print one 1 only