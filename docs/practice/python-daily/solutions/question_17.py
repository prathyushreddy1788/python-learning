import datetime

class Account:
    def __init__(self, name: str, account_number: int, balance: float):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transaction_history: list[Transaction] = []

    def add_amount(self, amount: float):
        self.balance += amount
        current_transaction_obj = Transaction(f"{datetime.datetime.now()}", "credit", amount)
        curret_transaction = {"transaction_time": f"{datetime.datetime.now()}", "transaction_type": "credit","amount": amount}

        self.transaction_history.append(curret_transaction)

    def withdraw_amount(self, amount: float):

        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            current_transaction_obj = Transaction(f"{datetime.datetime.now()}", "debit", amount)
            curret_transaction = {"transaction_time": f"{datetime.datetime.now()}", "transaction_type": "debit", "amount": amount}
            self.transaction_history.append(curret_transaction)

    def display_transactions(self):
        for transaction in self.transaction_history:
            #print(f"transaction_time: {transaction.transaction_time} transaction_type : {transaction.transaction_type} amount: {transaction.amount}")
            print(transaction)








class Transaction:

    def __init__(self, transaction_time: str, transaction_type: str, amount: float):

        self.transaction_time = transaction_time
        self.transaction_type = transaction_type
        self.amount = amount




account1 = Account("prathyush", 123456, 0)
account1.add_amount(1000)
account1.withdraw_amount(1001)
account1.display_transactions()
print(account1.balance)

#no transactions
#date time
#negative_balance


