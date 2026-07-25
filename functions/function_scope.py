# Global scope
x = 1

def one():
    x = 2
    print(f"from function 'Local' scope {x} ")


def two():
    global x
    x = 99
    print(f"from function 'Local' scope {x} ")

# this function has no x defined inside it so it will get the value for x from the global scope
def three():

    print(f"from function 'Local' scope {x} ")

print(f"from global scope {x} ")

one()
two()
three()
print(f"from global scope after function two is called and it have global x: {x} ")