people = {
    "weka": {
        "dart": 90,
        "python": 80,
        "Js": 50,
    },
    "ahmed": {
        "dart": 50,
        "python": 100,
        "Js": 20,
    },
    "aly": {
        "dart": 80,
        "python": 80,
        "Js": 60,
    }
}

# print(people["weka"])
# print(people["ahmed"])
# print(people["aly"])

# print(people["weka"]["Js"])
# print(people["ahmed"]["Js"])
# print(people["aly"]["Js"])

for person in people:
    print(person)  #-> This will print only the Keys.
    # print(f"the skills and pogress for {person} are: {people[person]}") # this will print the key and its value
    for skill in people[person]: # skill here is the key in the inner dictionary and people[person][skill] is it's value
        print(f"{skill} -> {people[person][skill]}")

