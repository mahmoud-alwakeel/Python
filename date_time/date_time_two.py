import datetime

birthday = datetime.datetime(2001, 9, 21)

print(birthday)
print(birthday.strftime("%B"))
print(birthday.strftime("%b"))
print(birthday.strftime("%a"))
print(birthday.strftime("%A"))
print(birthday.strftime("%d %B %Y"))
print(birthday.strftime("%d, %B, %Y"))
print(birthday.strftime("%d/%b/%Y"))