xyz = [i for i in range(5)]
print(xyz)



xyz = []
for i in range(5):
    xyz.append(i)

print(xyz)


xyz = (i for i in range(5))

for i in xyz:
    print(i)


