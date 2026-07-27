myList = ["weka", "ahmed", "aly"]

def format_text(name):
    return f"-  {name.strip().capitalize()}  -"

formatedData = map(format_text, myList)

for name in formatedData:
    print(name)

# or if we don't want to store it in a variable we can do the following:

for name in map(format_text, myList):
    print(name)

#  Or using lambda function:
print("using Lamda:")
for name in map((lambda name: f"-  {name.strip().capitalize()}  -"), myList):
    print(name)