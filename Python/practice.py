for i in range(1,4):
    for j in range(i):
        print('*',end='')
    print()

print()

for row in range(3):
    for star in range(3):
        print('*',end='')
    print()

print()

for rows in range(3,0,-1):
    for stars in range(rows):
        print('*',end='')
    print()

print()

for c in range(1,5):
    for d in range(1, c+1):
        print(d,end='')
    print()