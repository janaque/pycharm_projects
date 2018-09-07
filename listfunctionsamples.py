

lucky_numbers = [5,8,15,16,19]
friends = ["Robbin", "Elton", "Allan", "Bob", "Paul"]

#print lucky numbers
print(lucky_numbers)
print(friends)

friends1 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]

#concat lucky numbers and friends
friends1.extend(lucky_numbers)

friends2 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]

#append Creed on friends
friends2.append("Creed")

friends3 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]

friends4 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]
friends4.insert(2, "Baron")

friends5 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]
friends5.remove("Elton")

friends6 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]
friends6.clear()

friends7 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]
friends7.pop()

friends8 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]

friends9 = ["Robbin", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]

friends10 = ["Robbin", "Elton", "Elton", "Allan", "Bob", "Paul"]
lucky_numbers = [5,8,15,16,19]

friends11 = ["Tome", "Jerry", "Bruce", "Wayne", "Paul"]
lucky_numbers2 = [42,4,11,5,8,15,16,19]
lucky_numbers3 = [42,4,11,5,8,15,16,19]

friends11.sort()
lucky_numbers2.sort()
lucky_numbers3.reverse()

friends12 = friends11.copy()

#print friends + append and extend
print(friends1)

#print friends + append
print(friends2)

#print friends + append and extend
print(friends3)

#print friends + insert "Baron"
print(friends4)

#print friends + remove "Baron"
print(friends5)

#clear the list
print(friends6)

#pop remove the last element on the list
print(friends7)

#looks for Baron on the list and exit with 0 if successful
print(friends8.index("Elton"))

#looks for Baron on the list and exit with 1 if failed
#print(friends9.index("Jay"))

#looks for Elton and count the instance
print(friends10.count("Elton"))


#sort list on ascending order
print(friends11)
print(lucky_numbers2)

#sort in reverse order
print(lucky_numbers3)

#prints copy of friends 11

print(friends12)
