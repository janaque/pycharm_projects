num1 = float(input("Enter the first number: "))
oper = input("Enter oparation : ")
num2 = float(input("Enter the second number: "))

print("     ")
print("Answer is :")
print("=======")

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
else:
    print("Invalid operator !!!")

print("=======")