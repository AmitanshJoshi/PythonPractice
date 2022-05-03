import random

print(random.randrange(1,10)) #random number to print from range 1 to 10

print(list(range(1,11)))

multiLineString = """
This is the data
assigned to the multiline 
string.
"""
print(multiLineString)

name = "Derek, Jones"

print(name[0])

for x in name:
    print(x)


#Checking string withing a string

subscriptionStatus = "The course is completely free"
print("free" in subscriptionStatus)
print("expensive" not in subscriptionStatus)