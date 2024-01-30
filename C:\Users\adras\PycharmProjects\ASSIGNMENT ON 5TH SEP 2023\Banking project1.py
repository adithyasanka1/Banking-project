class BankAccount:
    def __init__(self):
        self.balance=0
        print("Hello welcome to Lakshmi Bank")
    def login(self):
        account_login=int(input("Enter your account number:"))
    def password(self):
        account_password=int(input("Enter your password:"))
        print("Login successful")
    def deposit(self):
        amount=float(input("Enter the amount you wish to deposit:"))
        self.balance+=amount
        print("\n Amount Deposited:",amount)
    def withdrawal(self):
        amount=float(input("Enter the amount you wish to withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n Amount you have withdrawn:")
        else:
            print("\nSorry insufficient account balance")
    def display(self):
        print("\n Net available balance",self.balance)

ba1=BankAccount()
ba1.login()
ba1.password()
ba1.deposit()
ba1.withdrawal()
ba1.display()

