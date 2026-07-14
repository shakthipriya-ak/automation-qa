def findpassorfail():
    if (mark>=35 and mark<=100):
        print(mark,' is a pass mark')
    elif(mark<35 and mark>=0):
        print(mark,' is a fail mark')
    else:
        print(mark,' is a Invalid mark')
mark=int(input('marks:'))
findpassorfail()