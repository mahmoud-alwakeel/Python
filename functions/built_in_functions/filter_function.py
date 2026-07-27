myNumbers = [1,2,5,7,10,90,23,45,55]

def check_num(num):
    # if num > 10: or we can do it like this 
        return num > 10


numbersBiggerThanTen = filter(check_num, myNumbers) # filter returns True

for number in numbersBiggerThanTen:
    print(number)

for number in filter(lambda num: num > 10, myNumbers):
      print(f"From lambda: {number}")



# example 2
names = ["weka", "Weka", "ahmed", "Ahmed"]

def check_name(name):
    # if num > 10: or we can do it like this 
        return name.startswith("W")


agreedNames = filter(check_name, names) # filter returns True

for name in agreedNames:
    print(name)
