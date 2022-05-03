# IF else conditions
a=40
b=40
if( a > b ):
    print("a is greater")
elif( b > a ):
    print("b is greater")
else:
    print("None")


#Short hand for the above condition

print("a is greater") if a > b else print("otherwise")

print("a is greater") if a > b else print("equal") if a == b else print("b is greater")


# Loops -while and for loop

timer = 1

while timer <= 10:
    print(timer)
    timer += 1
    if timer == 5:
        print("here")
        continue
else:
    print("Countdown is over")

#For loops
employees = [ "emp1", "emp2", "emp3"]

for index in employees:
    print(index)
    if index == "emp2":
        employees[1]="emp4"
        continue
else:
    print("List is finished")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)