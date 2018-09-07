with open('samplefile', 'r') as f:

    for line in f:
        print(line)


print('====================')

with open('samplefile', 'r') as f:

    f_contents = f.read(50)
    print(f_contents, end='')

    f_contents = f.read(50)
    print(f_contents)

print('====================')

with open('samplefile', 'r') as f:


    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='**********')
        f_contents =f.read(size_to_read)


