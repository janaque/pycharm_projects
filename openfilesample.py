empFile = open("samplefile", "r")


#print(empFile.read())

#print(empFile.readlines()) ## putting in a list

var: int = input("Enter the line you want: ")

var01 = int(var)

print(empFile.readlines()[var01]) ## read 2nd line

empFile.close()
