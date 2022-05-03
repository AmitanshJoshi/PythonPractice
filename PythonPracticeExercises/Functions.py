
def tvMode(power = False):
    if bool(power) == True:
        print("Switched on")
    else:
        print("Switched Off")

tvMode(True)

def aLot(*args):
    print(args[1],args[0])

aLot(1,2,4,5,6)


#Recursion using function

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result




#Lambda
x= lambda a,b : a+b
print(x(2,5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))