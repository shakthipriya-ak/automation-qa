for i in range(1,11):
    print(i)

for a in range(1,21):
    if a%2==0:
        print(a)

testcase=['login','signup','payment','safari']
for test in testcase:
    if test=='payment':
        continue
    print('Executing',test)

tests=['login','signup','payment','safari']
for test1 in tests:
    if test1=='payment':
        print('Executing',test1)

browsers = ["Chrome", "Firefox", "Edge", "Safari"]
for browser in browsers:
    if browser=='Edge':
        continue
    if browser=='Safari':
        break
    print('Test',browser)

for r in range(10,0,-1):
    print(r)

employees = ["AK", "John", "David", "Sara", "Emma"]
for emp in employees:
    if emp=='John':
        continue
    if emp=='Sara':
        break
    print('Processing',emp)