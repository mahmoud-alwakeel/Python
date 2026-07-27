# sum(iterable, start)
a = [1, 2, 3, 4]

print(sum(a))
print(sum(a, 90)) # start = 90

# round()

b = 99.1234124
print(round(b))
print(round(b, 2))

b = 99.9534124
print(round(b))
print(round(b, 2))

# range(start, end, steps) -> start can be left and it will be equal to 0, also the steps and it will be equal to 1, end is not included
print(list(range(0, 10, 3)))


# print()
print("hello weka how are you")
print("hello", "weka", "how", "are", "you", sep="$") # default separator is space


print("first line", end = "\t") # the default end is "\n"
print("second line")