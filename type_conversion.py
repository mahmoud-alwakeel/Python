# str()
a= 10
print(type(a))
print(type(str(a)))
print(f"a + {a}")
print("=" * 50)

# tuple -> variable must be iterable
b = "weka"
c = [1, 2, 3]
d = {"A", "B", "C"}
e = {"one": "A", "two": "B"}
print("type conversionTo Tuple")
print(type(tuple(b)))
print(type(tuple(c)))
print(type(tuple(d)))
print(type(tuple(e)))
print("=" * 50)

# List -> variable must be iterable
f = "weka"
g = (1, 2, 3)
h = {"A", "B", "C"}
i = {"one": "A", "two": "B"}
print("type conversionTo List")
print(type(list(f)))
print(type(list(g)))
print(type(list(h)))
print(type(list(i)))
print(list(f))
print(list(g))
print(list(h))
# Takes only the keys
print(list(i))
print("=" * 50)

# Set -> variable must be iterable
j = "weka"
k = [1, 2, 3]
l = ("A", "B", "C")
m = {"one": "A", "two": "B"}
print("type conversionTo Set")
print(type(set(j)))
print(type(set(k)))
print(type(set(l)))
print(type(set(m)))
print(set(j))
print(set(k))
print(set(l))
# Takes only the keys
print(set(m))
print("=" * 50)


# j = "weka" -> String can't be converted to a dict
k = (("A", 1), ("B", 2), ("C", 3)) # tuple can be converted but it needs nested tuples each with 2 elements to act as a Dict
l = [["A", 1], ["B", 2], ["C", 3]] # List same as tuple
# m = {"one": "A", "two": "B"} Set is unhashable
print("type conversionTo Dict")
print(type(dict(k)))
print(type(dict(l)))
print(dict(k))
print(dict(l))
# Takes only the keys
print("=" * 50)

