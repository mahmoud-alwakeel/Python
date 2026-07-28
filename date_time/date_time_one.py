import datetime

print(datetime.datetime.now())

print("=" * 50)
print(datetime.datetime.now().year)

print(datetime.datetime.now().month)

print(datetime.datetime.now().day)

# start and end datetime
print("=" * 50)
print(datetime.datetime.min)
print(datetime.datetime.max)

print("=" * 50)
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().date())

# start and end time
print("=" * 50)
print(datetime.time.min)
print(datetime.time.max)

# print specific date: 
print(datetime.datetime(2001, 9, 21))

myBirthdate = datetime.datetime(2001, 9, 21)
howManydays = (datetime.datetime.now() - datetime.datetime(2001, 9, 21)).days
print(f"You lived for {howManydays} days")