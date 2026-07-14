def add(a, b):
    print(a+b)
def sub(a, b):
    print(a-b)
def mul(a, b):
    print(a*b)
def div(a, b):
    print(a/b)
def pow(a, b):
    print(a**b)
a=int(input('a:'))
b=int(input('b:'))
add(a,b)
mul(a,b)
pow(a,b)
sub(a,b)

def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
div(a,b)