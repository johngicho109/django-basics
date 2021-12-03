from math import *
from functions import *

#print function
print("Hello world!")
print("Welcome")

#variables
name = "Joe"
age = 25
country = "Kenya"
print(name,"aged",age,"is from",country)
print(type(name),type(age))
#\n = newline character
#\' = printing a quote on a string of character

#inbuilt python strings functions
"""
.upper() - converts strings to uppercase
.lower() - converts strings to lowercase
.isupper() - returns true if string is uppercase or false if string is lower
.lower()
.index("character in a variable string") - returns interger value of the character
.replace("char. being replaced","char. to replace into")
"""
print(20%6) #returns the remainder
print(str(44) + "44")
print(44 + int("44"))
print(bin(3)) #binary function
print(sqrt(100))



#Getting user input
"""
name = input("What is your name?\n")
age = input("What is your age?\n")
print("Welcome",name,"You are",int(age),"years old")
"""

#Exercise 1
"""
sentence = input("Enter a sentense\n")
print("Your sentense is",sentence)
word1 = input("Enter the word to replace\n")
word2 = input("Enter the word to replace it with\n")
print(sentence.replace(word1,word2))
"""

#lists
countries = ["Kenya","UK","USA","Canada","Australia"]
print(countries)
print(countries[0][0])
print(countries[1:])
print(countries[:])
print(countries[:3])
print(countries[1:4])
countries[0] = "China"
print(countries)
print(countries[-1])
print(countries[-2])
print(type(countries[0]))

myList = list(("Joe","Lizz","Abby","Mary"))

#list methods
list1 = list(("1","2","3","4","5","6"))
list2 = ["Banana","Mangoes","Oranges","Apple","Ovacadoes"]
list1.extend(list2)
print(list1)
print(list2)
list2.append("Cherry")
print(list2)
list2.insert(1,"cherry")
print(list2)
list2.remove("cherry")
list1.clear()
print(list1)
print(list2.index("Mangoes"))
print(list2.count("Mangoes"))
list1 = list((1,4,6,0,7,8))
(list1.sort())
print(list1)
list2.reverse()
print(list2)
list3 = list2.copy()
print(list3)
list2.pop()
print(list2)
print(list3)
list3.remove("Apple")
list3.pop(0) #del list2[1] del list2
print(list3)

#Tupples
myTup = 1,
myTup2 = 1,"Home",True
print(myTup)
print(myTup2)
print(type(myTup))
myTup3 = tuple((1,2,3,4,5,6,7))
print(myTup3)

#function
def greetings(name,age):
    print("Hello",name)
    print("You are",age,"years old")
    print("WElcome Home")

greetings("joe",26)

def greetings2(*names):
    print("Welcome",names[1])

greetings2("Joe","Lizz","Abby")

def square(x):
    return x*x

print(square(2))

def add(num1,num2):
    return num1+num2

print(add(1,2))


#if statements
x = 3
if x%2==0:
    print("Number is Even")
else:
    print("Number is Odd")

dt = input("Enter a value")
if type(dt) == str:
    print("Data type is a string")
elif type(dt) == int:
    print("data type is an integer")
elif type(dt) == list:
    print("Data type is a list")
else:
    print("Unknown data type")

st = "This is a sentence"
if len(st) > 10:
    print("Good")
else:
    print("Bad")

#Dictionaries
#Duplicates of keys are not allowed
myDict = {
    1:"Lizz",
    2:"Mary",
    3:"Cinthia"
}
print(myDict)
print(type(myDict))
print(myDict[1])
myDict2 = dict()
print(myDict2)

#while loop
i = 1
while i < 6:
    print(i)
    i += 1

#for loops
lst1 = [1,2,3,4,5]
for i in lst1:
    print(i)

for letter in "Hello":
    print(letter)

print("==============================")
print(myDict)
for keys in myDict:
    print(keys)

for i in range(4):
    print("Hello",i)

for i in range(2,5):
    print("Hae",i)

#2D list and Nested loops
myList2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(myList2)
print(myList2[0][0])
print(myList2[1][1])

for i in myList2:
    for j in i:
        print(j)

#calculator
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
except ValueError: #ValueError,NameError
    print("Value not an interger")
else:
    op = input("Enter an operator: ")

    if op == "+":
        print(num1,"+",num2,"=",num1 + num2)
    elif op == "-":
        print(num1,"-",num2,"=",num1 - num2)
    elif op == "*":
        print(num1,"*",num2,"=",num1 * num2)
    elif op == "/":
        print(num1,"/",num2,"=",num1/num2)
    else:
        print("Invalid operator")
finally:
    print("Finished")

#try/except

#reading files
"""
r - read
w - write
a - append
r+ - read and writing or either read or write
"""
countryFile = open("countries.txt","r")
print(countryFile.readable())
# print(countryFile.readline())
# print(countryFile.readlines()[-1])
for country in countryFile.readlines():
    print(country)
countryFile.close()

#writing files
countFile = open("countries.txt","w")
countFile.write("Kenya,Canada,USA,China,Austaralia ,blablabla")
countFile.close()

#append
countFile2 = open("countries.txt","a")
countFile2.write("\nNew zeland")
countFile2.close()

