for i in range(1,6):
    if i==3:
        break
    print(i)

for a in range(7,13):
    if a==9:
        continue
    print(a)

testcases=['login','signup','payment','search']
for test in testcases:
    print('executing',test)

testcase=['login','signup','payment','search']
for testc in testcase:
    if testc=='payment':
        continue
    print('executing',testc)

browsers=['safari','chrome','edge','firefox']
for browser in browsers:
    if browser=='chrome':
        continue
    if browser=='firefox':
        break
    print('testing',browser)

