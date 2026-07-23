myFriends = ["Aly", "Ahmed", "Peter"]
notMyFriends = ["mohammed", "mansour"]
# append
print("Append:")
myFriends.append("Mark")
myFriends.append(1)
myFriends.append(True)
# The whole List will be added as a one element
myFriends.append(notMyFriends)
print("List of myFriends after append():")
print(myFriends)
print(myFriends[0])
print(myFriends[1])
print(myFriends[-1][1])

# extend
print("Extend:")
listA = [1,2,3,4]
listB = ["a","b","c"]
#  Modify the list not Create and return a new list so if we assigned it to a new var c for example it will return None
listA.extend(listB)
print(listA)


listX = [1,2,3,1,1,1,1]
# will remove the first 1 only not all the 1 in the list
listX.remove(1)
print(listX)

# Sort it's only for NUMBERS
listY = [123, 22, 1, -10, -100]
listY.sort()
# This will reverse the sorting
# listY.sort(reverse = True)
print(listY)

# Reverse, reverses the elements in the list, Strings or numbers while Sort is used only with number and sorts them asc or desc
listF = ["one", 1, 1.1]
listF.reverse()
print(listF)