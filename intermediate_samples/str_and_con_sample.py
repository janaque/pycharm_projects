import os

var1 = input("Enter you first name: ")
var2 = input("Enter you second name: ")
var3 = input("Enter you third name: ")
var4 = input("Enter you fourth name: ")


names = [var1,
         var2,
         var3,
         var4,
         ]

print('=================================')

for var in names:
    print('Hello there, ' + var)

print('=================================')

print(', '.join(names))