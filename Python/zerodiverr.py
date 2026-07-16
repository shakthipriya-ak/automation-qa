try:
    a=10
    b=0
    print(a/b)
except:
    print('cannot divide by zero')

print()

try:
    x='hello'
    print(x)
except:
    print('invalid number')
print('program finished')
print()
try:
    y=int('hello')
    print(y)
except:
    print('invalid number')
print('program finished')