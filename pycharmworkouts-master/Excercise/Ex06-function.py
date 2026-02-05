

int_rate = 0.1

print("Before Calling function..Interest Rate:", int_rate)
def calculate_loan_amount(pr,tenure):
    global int_rate
    int_rate = 0.2
    print("Inside Interest Rate:", int_rate)
    return pr * tenure * int_rate / 100


calculate_loan_amount(1000,2)
print("After Calling function..Interest Rate:", int_rate)