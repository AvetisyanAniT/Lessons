class bank_program:
    def __init__(self, account_type, percent, max_sum, balance = 0):
        self.account_type = account_type
        self.percent = percent
        self.max_sum = max_sum
        self.balance = balance

    def print_account_type(self):
        print(f'Account type: {self.account_type}')

    def print_percent(self):
        print(f'Account percentage: {self.percent}')

    def print_max_sum(self):
        print(f'Maximum amount: {self.max_sum}')

current_account = bank_program('current','2%', 1000000, 0)
deposit_account = bank_program('deposit','10%', 5000000, 50000)

class pension_program(bank_program):
    def __init__(self, account_type, percent, max_sum, balance, pension_amount):
        bank_program.__init__(self, account_type, percent, max_sum, balance)
        self.pension_amount = pension_amount
    
    def print_pension_amount(self):
        print(f'Pension amount: {self.pension_amount}')

pension_account = pension_program('pension','1%', 500000, 0, 40000)

print('The current account')
current_account.print_account_type()
current_account.print_percent()
current_account.print_max_sum()
print('\nThe deposit account')
deposit_account.print_account_type()
deposit_account.print_percent()
deposit_account.print_max_sum()
print('\nThe pension account')
pension_account.print_account_type()
pension_account.print_percent()
pension_account.print_max_sum()
pension_account.print_pension_amount()


# Exactly what I need. Very Good Ani jan!!! Only remember,
#  By convention, user-defined Python class names start with a capital letter
# example- class Bank_program  class Pension_program
