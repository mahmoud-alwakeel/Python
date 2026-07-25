# Has no Name
# we can call it inline without defining it anywhere
# we can use it in returning data from another function
# used for simple functions and normal function is the one responsible for handling lare tasks
# lambda function is one single expression not a block of code
# Lambda function is of type function

# normal function
def say_hello(name):
    return f"Hello {name}"

# lambda function
hello = lambda name, age = "unknown": f"Hello {name}, your age is: {age}"

print(say_hello("Weka"))
print(hello("Weka from lambda function"))
print(hello("Weka from lambda function", 25))
print(say_hello.__name__)
print(hello.__name__)