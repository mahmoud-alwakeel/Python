myNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Continue -> ignores a specific element
for num in myNums:
    if num == 3:
        continue # in this case won't print the number 3
    print(num)

# Break -> Breaks the loop at a certain condition
print("=" * 50)
print("------------------------Break-----------------------------")
for num in myNums:
    if num == 5: # won't continue past this element
        break
    print(num)

#  Pass -> if we have an empty for loop for example so it will break the code and we don't want to delete it 

print("=" * 50)
print("------------------------Pass-----------------------------")
for num in myNums:
    pass