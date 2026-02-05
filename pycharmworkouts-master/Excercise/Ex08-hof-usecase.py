
def Hdfcbank(p,n):
    r = 10
    interest = p * n * r / 100
    print("Loan Amount to be paid in HDFC Bank",(p + interest))


def Axisbank(p,n):
    r = 12
    interest = p * n * r / 100
    print("Loan Amount to be paid in Axis Bank",(p + interest))

def Citibank(p,n):
    r = 8
    interest = p * n * r / 100
    print("Loan Amount to be paid in Citi Bank",(p + interest))

bank_name = input("Enter Bank Name:")
p_amt = int(input("Enter Principle Amount:"))
tenure = int(input("Enter Period/Tenure:"))

if bank_name == "hdfc":
    b_name = Hdfcbank
elif bank_name == "axis":
    b_name = Axisbank
else:
    b_name = Citibank

def CalcualteInterest(bankname,pamt,period):
    print("Principle Amount:",pamt)
    print("Tenure to Pay:",period)
    bankname(pamt,period)

CalcualteInterest(b_name,p_amt,tenure)


