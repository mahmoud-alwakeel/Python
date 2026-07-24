# Clear
dictOne = {
    'one': 'example'
}
print(dictOne)
dictOne.clear()
print(dictOne)

# Update
dictTwo = {
    'two': 'example2'
}
dictTwo['age'] = 19
print(dictTwo)
dictTwo.update({"money": "100", "country": "Egy"})
print(dictTwo)

main = {
    "name": "Weka"
}

notMainDict = main.copy()
print(f"Main Dict: {main}")
print(f"not main Dict: {notMainDict}")
main["age"] = 25

print(f"Main Dict after adding: {main}")
print(f"not main Dict after adding to the main: {notMainDict}")
