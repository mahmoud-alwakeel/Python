# set Default

dictOne= {
    "name": "weka"
}
print(dictOne)
print(dictOne.setdefault("name", "Not weka")) # this won't change the name as it's already their
print(dictOne.setdefault("age", 25)) # this will add a new key age with a new val 25
print(dictOne.setdefault("languages")) # This will make the Value "None"
print(dictOne)

dictTwo= {
    "name": "weka"
}

dictTwo.update({"age": 25})
dictTwo.update({"country": "Eg"})
print(dictTwo)
# popitem takes no arguments!!
# dictTwo.popitem("age") this is wrong
#  it removes the last added item which is here in this case the country
dictTwo.popitem()
print(dictTwo)

# From keys
a = ('one', 'two', 'three')
b = "X"
print(dict.fromkeys(a, b))