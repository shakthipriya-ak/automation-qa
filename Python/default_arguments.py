def greet(name='Student'):
    print('Welcome',name)
greet()
greet('Rahul')

def student(name, age):
    print(name, age)
student(age=22,name='AK')

def employee(namee,salary):
    print(namee,salary)
employee(salary='10LPA',namee='Shakthipriya AK')

def number(*num):
    print(num)
number(10)
number(10,20,30)
number(1.2,30,204847)

def add(*numbers):
    total=0
    for nums in numbers:
        total+=nums
    print(total)
add(10)
add(20,40,50)
add(1.34,592.93,84848)
    
def largest(*large):
    print(max(large))
largest(2,8,1,10,5,2225)

def largestt(*larg):
    biggest=larg[0]
    for num in larg:
        if num>biggest:
            biggest=num
    print(biggest)
largestt(3,6,8,3553,94854,0,33)

def person(**info):
    for key, value in info.items():
        print(key, value)
person(name='ak',age=22,job='testter')