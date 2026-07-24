dictOne = {
    "name": "Mahmoud Alwakeel",
    "age": 25,
    "programming_languages": ["Dart", "Python"],
    "rating": 9.5
}
# If i typed the key "name" again, the last key will be used and the ones before will be ignored
print(dictOne)
print(dictOne['programming_languages'])
print(dictOne.get('programming_languages'))
print(dictOne.keys())
print(dictOne.values())
# This prints an error
# print(dictOne[2])

twoDimensionalDictionary = {
    "one": {
        "language": "Dart",
        "progress": "90%",
    },
    "two": {
            "language": "Python",
            "progress": "80%",
    },
    "three": {
                "language": "Js",
                "progress": "50%",
    }
}
print(twoDimensionalDictionary)
print(twoDimensionalDictionary['two'])
print(twoDimensionalDictionary['two']['language'])
print(f"The length of this dictionary is {len(twoDimensionalDictionary)}")