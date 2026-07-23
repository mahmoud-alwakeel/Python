# This is the new way for String formatting
name = "Weka"
age = 25
country = "Egy"
level = 100
print(f"my name is: {name} i'm {age} and i am from {country}, i have {level:.2f}")

#  {:s} -> String
#  {:d} -> digit
#  {:f} -> Float
#  {:.wf} -> Float with 2 decimal places

#  Formatting money
myMoney = 100000000
print(f"My money is {myMoney:,d}")
print(f"My money is {myMoney:_d}")
# print(f"My money is {myMoney:&d}") # invalid format specifier