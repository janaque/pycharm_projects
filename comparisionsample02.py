def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>= num1 and num2 >= num3:
        return num2
    else:
        return num3

var1 = input("Enter the first number: ")
var2 = input("Enter the second number: ")
var3 = input("Enter the last  number: ")

print("=======================")
print("The biggest no. is: ")

biggest_num = print(max_num(var1, var2, var3))

print("=======================")

# !=  not equal
# == equal to