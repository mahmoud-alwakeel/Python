# default parameter must be the last parameter 
def say_hello(name, age, country = "unKnown"):
    print(f"Hello {name}, your age is: {age} and your country is: {country}")

say_hello("weka", 25, "Eg")
say_hello("ahmed", 30)