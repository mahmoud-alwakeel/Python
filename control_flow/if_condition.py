name = "Weka"
age = 25
country = "EG"
# country = "USA"
# country = "Canada"
course = "Python"
coursePrice = 100
isStudent = False

if age < 30 and country == "EG":
    if isStudent:
        print(f"Hello {name}, because you are from {country} the course \"{course}\" price is {coursePrice - 90}")
    else:
        print(f"Hello {name}, because you are from {country} the course \"{course}\" price is {coursePrice - 80}")

elif age < 30 and country == "USA":
    print(f"Hello {name} the course \"{course}\" price is {coursePrice - 50}")
else:
    print(f"Hello {name} the course \"{course}\" price is {coursePrice - 20}")
    
