try:
    num=int(input('emter number:'))
    print(10/num)
except ZeroDivisionError:
    print('Cannot divide by zero')
except:
    print('Invalid input')
finally:
    print('Program ended')