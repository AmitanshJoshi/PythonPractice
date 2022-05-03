# Basics of python programming language

print("Hello World")
# print(7+int("4")) Will throw an error as the string and integer cannot be added or concatenated,
# conversion is required
print(int("7")+int("4"))

"""
This is how you comment 
Multiline in python and for single line # is used
"""

#Python Variables

name = "Joshi"
age = 25
points = 10
print(name)
print(age)
print(type(points)) # its an int type
print(float(points)) #converting in float
a=4
A=10
print(a)
print(A)

#Multiple assignment

person1, person2, person3 = "Emp1","Emp2","Emp3"
print(person1+" "+person2+" "+person3)

# Single value to multiple variable
student1 = student2 = 10
print(student1)
print(student2)

#Collection assignment
x = y =z =['n1','n2','n3']
print(x+y+z)

#O/P multiple variable
x=1
y=2
z=3
print(x,y,z)

# Global and local variable

name="Joshi"

def NameFunc():
    global name
    name="Joshi1"
    print(name)


NameFunc()
print(name)

