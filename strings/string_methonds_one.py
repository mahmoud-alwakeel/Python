a = "i am a software engineer"
b = "   i am a software engineer    "
c = "*****i am a software engineer******"

print(len(a))
# spaces before and after also counts
print(len(b))

print(b)
print(b.strip())
print("R strip")
print(b.rstrip())
print("L strip")
print(b.lstrip())

print(c.strip())
print("C strip *")
print(c.strip("*"))

# makes the first letter in every one capital
print(a.title())
# make the first word's Letter capital
print(a.capitalize())

# zfill(3) prints 01, 011, 111
e, d, f = "1", "11", "111"
print(e.zfill(3))
print(d.zfill(3))
print(f.zfill(3))

g = "weka"
print(g.upper())
h = "WEKA"
print(h.lower())