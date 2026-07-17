pin='1425'
attempts=0
balance=1000
transactions=[]
def check_balance():
    print(f'Current balance: ${balance}')

def deposit(amount):
    global balance
    if amount <=0:
        print('Enter a valid amount to deposit')
    else:
        balance+=amount
        transactions.append(f'Deposited ${amount}')
        print(f'${amount} deposited successfully')
        print(f'Available balance: ${balance}')

def withdraw(amount):
    global balance
    if amount<=0:
        print('Enter a valid amount to withdraw')
    elif amount>balance:
        print('Insufficient balance')
    else:
        balance-=amount
        transactions.append(f'Withdrawn ${amount}')
        print(f'${amount} withdrawn successfully')
        print(f'Available balance: ${balance}')

while attempts<3:
    entered_pin=input('Enter the 4 digit Pin: ')
    if entered_pin==pin:
        print('Welcome')
        break
    else: 
        attempts+=1
        print('Incorrect Pin, Try again')
if attempts==3:
    print('Too many attempts')
    print('CARD BLOCKED')
    exit()

while True:
    print('-------- ATM MENU --------')
    print('1. Check balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transaction History')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice=='1':
        check_balance()
    elif choice=='2':
        try:
            amount=float(input('Enter amount to deposity: '))
            deposit(amount)
        except ValueError:
            print('Enter a valid number')
    elif choice=='3':
        try:
            amount=float(input('Enter amount to withdraw: '))
            withdraw(amount)
        except ValueError:
            print('Enter a valid number')
    elif choice=='4':
        if len(transactions)==0:
            print('No transactions yet')
        else:
            print('Transaction history:')
            for transaction in transactions:
                print(transaction)
    elif choice=='5':
        print('Thank you for using ATM')
        break
    else:
        print('Invalid entry')