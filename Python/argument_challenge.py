def total(*marks):
    total=sum(marks)
    print('Total: ',total)
def average(*marks):
    total=sum(marks)
    avg=total/len(marks)
    print('Average: ',avg)
def highest(*marks):
    high=max(marks)
    print('Highest: ',high)
def lowest(*marks):
    low=min(marks)
    print('Lowest:',low)
total(85, 90, 78, 92, 88)
average(85, 90, 78, 92, 88)
highest(85, 90, 78, 92, 88)
lowest(85, 90, 78, 92, 88)
print()

def report(*marks):
    print("Total:", sum(marks))
    print("Average:", sum(marks) / len(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

report(85, 90, 78, 92, 88)