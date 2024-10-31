class BankingApp:
    total_balance = 0.0
    transaction_type = ['add','withdraw']

    def __init__(self):
        pass

    def transaction(self, transaction_type, amount):
        if transaction_type not in BankingApp.transaction_type:
            raise ValueError(f"You choose an unvalid transaction type amount the {BankingApp.transaction_type[0]} or {BankingApp.transaction_type[1]} ")
        
        if transaction_type == 'add':
            BankingApp.total_balance += amount

        elif transaction_type == 'withdraw':
            if amount > BankingApp.total_balance:
                return "Insufficient balance for this transaction"
            BankingApp.total_balance -= amount

    def get_balance(self):
        return BankingApp.total_balance

bank_app = BankingApp()


bank_app.transaction('add',50)
print(bank_app.get_balance())

res = bank_app.transaction('withdraw',67)
print(res)

