subject=['Python','SQL','Java','Testing']
for index, sub in enumerate(subject,start=1):
    if sub=='Java':
        continue
    print(index, sub)
print()

marks=[95, 82, 48, 76, 39]
for num, sc in enumerate(marks, start=1):
    if sc>= 50 and sc <=100:
        print('Student',num,':','Pass')
    elif sc<50 and sc>=0:
        print('Student',num,':','Fail')
    else:
        print('Invalid')
    