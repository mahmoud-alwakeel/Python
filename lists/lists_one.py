myList = [1, 2, 3, 4]
print(myList)
print(type(myList))
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[-1])

listOfEveryThing = [1, True, 11.11, [1, 2, 3], (1, 2, 3), "One", "Two"]
print(listOfEveryThing)
print("Print only from index 0 to 4:")
print(listOfEveryThing[0:5])
#  all List elements with step = 1 
print(listOfEveryThing[::1])
#  all List elements with step = 2
print(listOfEveryThing[::2])
#  will result in a Range error
# print(listOfEveryThing[150])

# Len of List
print("Length of List:")
print(len(listOfEveryThing))


# we can edit list items as it's mutable
list2 = [1, 2, 3]
print(list2)

list2[1] = 44

print("list2 after editing index 1 and changed it from 2 to 44:")
print(list2)


list3 = [1, 2, 3, 4, 5, 6]
list3[0:2] = []
print(list3) 


list4 = [1, 2, 3, 4, 5, 6]
#  here we don't replace so we can remove multiple elements and put one new element 
list4[0:3] = [99]
print(list4) 