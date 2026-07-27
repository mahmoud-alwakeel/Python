mySkills = ["dart", "flutter", "python", "data science"]

mySkillsEnumerated = enumerate(mySkills, 1) # the second argument is the start for the counter

# for skill in mySkillsEnumerated:
#     print(skill)

for counter, skill in mySkillsEnumerated:
    print(f"{counter} - {skill}")


#  reversed
name = "wekaaa"
nameReversed = reversed(name)

for letter in nameReversed:
    print(letter)