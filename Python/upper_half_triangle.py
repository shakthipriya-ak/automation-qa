n=5
for i in range(1,n+1):
    #spaces
    for j in range(i-1):
        print(' ',end='')
    # stars
    for k in range((n-i)+1):
        print('*',end='')
    print()
