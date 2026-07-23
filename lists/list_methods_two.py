# Clear

list1 = [1, 2, 3, 4]
print(list1)
list1.clear()
print(list1)

list2 = [5, 6, 7, 8]
# Return a shallow copy of the list.
list3 = list2.copy()

print(list2) # Main list
print(list3) # Copied list

list2.append(9)
print(list2) # Main list
#  doesn't have the element we added using append as it's a shallow copy
print(list3) # Copied list

list4 = [5, 6, 7, 8, 9, 9, 9, 9]
print(".count: counts How many times this element is in the list:")
print(list4.count(9))

list5 = ["one", "two", "three", "four"]
print(list5.index("three"))
# if the element is not in the list it will return an error:
# print(list5.index("thre"))
# print(list5.find("three"))

# Insert in a specific index
list5.insert(0, "zerooooooo")
# Insert before the LAST INDEX 
list5.insert(-1, "-11111")
print(list5)

# if it didn't take an index it will remove the last element if it took an index it will remove the element in that index
list5.pop(1)
print(list5)