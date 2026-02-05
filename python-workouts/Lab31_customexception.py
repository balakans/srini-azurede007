
#--Custom Exception

class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot take square root of negative number.")
    return n ** 0.5

try:
    res = square_root(9)
    print(res)
except NegativeNumberError as e:
    print("Error:", e)


class InsufficientFundsError(Exception):
   pass


def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Transaction failed: Tried to withdraw ₹{amount} with only ₹{balance} in account.")
    balance -= amount
    return balance

try:
    current_balance = 1000
    withdraw_amount = 1500
    new_balance = withdraw_money(current_balance, withdraw_amount)
    print(f"New balance: ₹{new_balance}")
except InsufficientFundsError as e:
    print(e)