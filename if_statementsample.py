print("======================")

is_male = True

if is_male:
    print("You are a male bro !!!")
print("======================")

is_male = False

if is_male:
    print("You are a male bro !!!")

print("======================")

is_male = False

if is_male:
    print("You are a male bro !!!")
else:
    print("You are not a bro bruh ...")

print("======================")

is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall bro !!!")

else:
    print("You are not a  bruh ...")

print("======================")

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male bro !!!")

else:
    print("You are not a  bruh ...")

print("======================")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male bro !!!")

elif is_male and not (is_tall):
    print("You are a short male")

elif not(is_male) and is_tall:

    print("You are not a male but is tall")

else:
    print("You are not a  bruh ...")

print("======================")




