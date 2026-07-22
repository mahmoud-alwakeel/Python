msg = "First Part"
msg2 = "second part"

print (msg + " " + msg2)

#  or we can make space in the first String
msgSpace = "First Part "
msg3 = "second part"

print (msgSpace + msg3)

a = "First \
Second \
Third"

b = "A \
B \
C"

# this will print First second ThridA B C as the backslash \ escapes the new line so they are 
#  a = "First Second Third", b = "A B C"
print(a + b)

#  we will get TypeError: can only concatenate str (not "int") to str
# print ("Hello "+ 1)