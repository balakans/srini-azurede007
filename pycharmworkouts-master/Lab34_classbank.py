class Bankaccount:
    #member
    customercount = 0

    #methods
    def __init__(self, accountid, balance):
        self.accid = accountid
        self.accbalance = balance
        Bankaccount.customercount += 1

    def deposit(self, amount):
        print("Current Balance:", self.accbalance)
        print("Deposit Amount:", amount)
        self.accbalance = self.accbalance + amount
        print("After Deposit, Balance Amount:", self.accbalance)

    def withdrawl(self, amount):
        print("Current Balance:", self.accbalance)
        print("Withdraw Amount:", amount)
        if self.accbalance >= amount:
            print("Amount withdrawn:", amount)
            self.accbalance = self.accbalance - amount
            print("After Withdrawn, Balance Amount:", self.accbalance)
        else:
            print("There is no sufficient amount to withdraw")

# Access Class member by class name
print("Current Customer Count:",Bankaccount.customercount)

#Creating Object
b1 = Bankaccount("SBI001",10000)
b1.withdrawl(5000)
b1.deposit(50000)
b2 = Bankaccount("SBI002",10000)
b3 = Bankaccount("SBI003",10000)
b4 = Bankaccount("SBI004",10000)

print("Current Customer Count:",Bankaccount.customercount)
