text = " Python is fun"

randomNumbers = "1 2 3 4 5 6 7 8 9"

print(text[0:6])
print(text[-3:])

#string functions

print(text.upper())
print(text.lower())
print(text.strip()) #removes whitespace
print(text.replace("P","H"))
print(randomNumbers.split(" "))


#Format string

name="Joshi"
age="25"
favProgLang="Python"

sentence = " Hello! My name is {} and I am {} years old. My fav prog lang is {}"
print(sentence.format(name,age,favProgLang))

#Escape Characters
print("My name is \"Joshi\"")

#Other string functions
sentence1 = "this is a new sentence.this seems cool, isn't it?"
print(sentence1.capitalize())
print(sentence1.startswith("this not"))


#Operators in Python
var= 21
print(var)
print(var//3)
print(var%3)
print(var**2)
print(24>26 or 25>24)