import main

import datetime as dt

class Human():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def humanAgePrint(self):
        print("Hi! My name is "+self.firstName+" "+self.lastName)

human1 = Human("Sam","Jonas")
print(human1.firstName)
human1.humanAgePrint()

#Inheritance Human is the base class and Student is the child class

class Student(Human):
    def __init__(self, firstName, lastName, standard):
        super(Student, self).__init__(firstName, lastName)
        self.standard = standard

student1 = Student("James","Anderson","8th")
print(student1.firstName)
print(student1.firstName, student1.lastName, student1.standard)


#Iterator
#List set tuple are iterable object and iterator form can be retrieved from the list set or tuple
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#Creating owns iterator

class Increment():
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        self.number = self.number+1
        return self.number


numbersInc = Increment()

series = iter(numbersInc)

print(next(series))
print(next(series))
print(next(series))
print(next(series))
print(next(series))
print(next(series))
print(next(series))

#Import modules
main.NameFunc()

#date time functions and methods
print(dt.date.today())
print(dt.datetime.now())
x = dt.datetime(2018, 6, 1)

print(x.strftime("%c"))


#Exception Handling

try:
    x = 2/1
    print(int(x))
except NameError:
    print("variable not named")
except:
    print("cannot divide by zero")
else:
    print("Nothing went wrong")
finally:
    print("end the solution")


age = 25.0

if type(age) is not int:
    raise Exception("Age cannot be an integer, supposed to be a whole number")
