username='ak'
password='shakthi'
def validate():
    if(username==uname and password==pword):
        return True
    else:
        return False
uname=input('username:')
pword=input('password:')
a=validate()
print(a)