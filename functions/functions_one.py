# Def => function keyword
def function_name():
    return "function return"

dataFromFunction = function_name()

print(dataFromFunction)

# Params and Arguments

# say_hello -> function name
# name -> function parameter
def say_hello(name):
    print(f"Hello {name}")

# ahmed here is function argument
say_hello("ahmed")
say_hello("aly")

def addition(n1, n2):
    if not isinstance(n1, (int, float))  or not isinstance(n2, (int, float)):
        print("enter Numbers only")
    else:
        print(n1 + n2)
addition(19, "aaa")
addition(19, 10)
addition(19, 10.5)

def full_name(firstName, middleName, lastName):
    print(f"Hello {firstName.strip().capitalize()} {middleName.upper():.1s} {lastName.capitalize()}")

full_name("   Mahmoud      ", "ahmed", "alwakeel")