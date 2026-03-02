from networkx.generators.classic import balanced_tree


class InvalidAmountError(ValueError):
    def __init__(self,name, amount, code):
        self.data = (name, amount, code)

class InsufficientFundsError(Exception):
    def __init__(self, name, code, balance, amount):
        self.data = (name, code, balance, amount)
        super().__init__(f"Balance is {balance} and attempted withdrawal is {amount}")
class BankAccount:
    def __init__(self, holder,balance):
        self.holder = holder
        self.balance = balance
    def withdraw(self, amount):
        if amount<=0:
            raise InvalidAmountError("Invalid Amount", amount, "001")
        if amount > self.balance:
            raise InsufficientFundsError("You don't have that much money", "002" , self.balance, amount)
        self.balance -= amount
        return f"Withdraw sucessful you have {self.balance} left"
def process_transaction(account, amount):
    print(f"Processing withdrawal of {amount, account.holder}")
    try:
       value = account.withdraw(amount)
    except InvalidAmountError as a:
        print("Invalid Transaction as amount is invalid", a.args)
    except InsufficientFundsError as b:
        print("Insufficent Funds. Transction was not complete", b.args)
    except Exception as e:
        print("Unexpected Error occured")
    else:
        print("Successful Transaction!")
        print(value)
    finally:
        print("Session Closed")
account = BankAccount("Alice", 1000)
process_transaction(account, 200)
process_transaction(account, -50)
process_transaction(account, 2000)