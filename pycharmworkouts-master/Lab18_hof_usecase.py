

def silver(salesamt):
    disperct = 5
    print("Customer Type:Silver")
    print("Discount %:",disperct)
    return salesamt * disperct / 100

def gold(salesamt):
    disperct = 8
    print("Customer Type:Gold")
    print("Discount %:",disperct)
    return salesamt * disperct /100

def platinum(salesamt):
    disperct = 10
    print("Customer Type:Platinum")
    print("Discount %:",disperct)
    return salesamt * disperct /100


def premium(salesamt):
    disperct = 12
    print("Customer Type:Premium")
    print("Discount %:",disperct)
    return salesamt * disperct /100

def elite(salesamt):
    disperct = 15
    print("Customer Type:Elite")
    print("Discount %:",disperct)
    return salesamt * disperct /100


#Higher order function
def finalamount(customertype, salesamt):
    discount = customertype(salesamt)
    print("Purchase Amount: {}".format(salesamt))
    print("Discount Amount: {}".format(discount))
    print("Amount to be Paid: {}".format(salesamt - discount))

cust_type = input("Enter Customer Type:")
sales_amt = float(input("Enter Sales Amount:"))

if cust_type == "silver":
    cust_type_fun = silver
elif cust_type == "gold":
    cust_type_fun = gold
elif  cust_type == "platinum":
    cust_type_fun = platinum
elif  cust_type == "elite":
    cust_type_fun = elite
else:
    cust_type_fun = premium

print(type(cust_type_fun))

finalamount(cust_type_fun,sales_amt)


"""
print("=======================")



#higher order function
def calcualtetotalloan(banktype,p,n):
    banktype(p,n)


calcualtetotalloan(Hdfcbank,1000,1)

"""