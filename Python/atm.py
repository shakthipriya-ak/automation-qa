balance=1000
def check_balance():
    print(f'Current balance: ${balance}')
def deposit(amount):
    global balance
    balance+=amount
    print(f'${balance} deposited successfully')
    print(f'Available balance: ${balance}')
def withdraw(amount):
    global balance
    if amount>balance:
        print('Insufficient balance')
    else:
        balance-=amount
        print(f'${amount} withdrawn successfully')
        print(f'Available balance: ${balance}')
while True:
    print('-------- ATM MENU --------')
    print('1. Check balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    choice = input('Enter your choice: ')
    if choice=='1':
        check_balance()
    elif choice=='2':
        amount=float(input('Enter amount to deposity: '))
        deposit(amount)
    elif choice=='3':
        amount=float(input('Enter amount to withdraw: '))
        withdraw(amount)
    elif choice=='4':
        print('Thank you for using ATM')
        break
    else:
        print('Invalid entry')