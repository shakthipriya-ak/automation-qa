def average(*numbers):
    total=0
    for num in numbers:
        total+=num
    avg=total/len(numbers)
    print(avg)
average(4,6,7,45,24,74,2)