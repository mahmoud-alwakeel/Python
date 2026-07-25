print(1,2,3,4,5)
myList = [1,2,3,4,5]
print(myList)
print(*myList) # will print each element alone not as a list

# here it takes whatever number of Arguments the user enters 
# this sovles the problem that sometimes we define a fixed number of parameters but we don't remember 
# or we want to add more or less number than the specified parameters
# def say_hello(n1, n2, n3, n4):
def say_hello(*people):
    for name in people:
        print(f"Hello {name}")

say_hello("a", "b", "c", "d", "e")

# * function packing
# * in a DEF   → packing   (gather IN)
def show_skills(name, *skills):
    print(f"hello {name} your skills are")
    for skill in skills:
        print(f"- {skill}")
        print(type(skills))

# function unpacking
# * at a CALL  → unpacking (spread OUT)
show_skills("weka", "python", "dart", "flutter", "data science")