# in & not in

name = "weka"
print("a" in name)
print("w" in name)
print("A" in name) # false -> case sensitive

myFriends = ["ahmed", "aly", "maged"]
print("ahmed" in myFriends)
print("wael" in myFriends)
print("wael" not in myFriends)


countries = ["eg", "usa", "canada"]
myCountry = "eg"

if myCountry in countries:
    print(f"hello")