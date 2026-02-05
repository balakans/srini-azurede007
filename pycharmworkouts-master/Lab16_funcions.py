"""
built-in functions
user defined functions
lambda functions
"""


# simple function
def func():
    '''This is to learn about simple function in python'''
    print("First user defined function")

# calling the function
func()



# function that takes input as parameters
def addnum(a, b):
    c = a + b
    print(f"sum of {a} + {b} = {c}")


addnum(10, 20)




# function that takes input and return value
def calcsquare(n):
    return n * n


res = calcsquare(10)
print(res)



# function where parameters have default values
# default value parameters should be the last one

def calculatediscount(amt, dispercent=10):
    disamt = amt * dispercent / 100
    return disamt


print(calculatediscount(1000,20))





# variable-length parameters
# Functions that accept flexible numbers of arguments.


# arguments are grouped into a tuple
def add_num(*args):
    print(type(args))
    sum = 0
    for num in args:
        sum += num
    return sum


result = add_num(1,2,3)
print('Sum is', result)




# collects all the keyword arguments passed to the function and stores them in a dictionary.
def CalcualteMarks(**sinfo):
    print(type(sinfo))
    print(sinfo)
    m1 = sinfo["eng"]
    m2 = sinfo["maths"]
    m3 = sinfo["sci"]
    print("Total Marks:", m1 + m2 + m3, "out of 300")


CalcualteMarks(studid=101, studname="Raj", eng=90, maths=98, sci=100)

def studinfo_print(s):
    print("Student Id:",s["studid"])
    print("Student Name:", s["studname"])
    print("English Mark:", s["eng"])
    print("Maths Mark:", s["maths"])
    print("Science Mark:", s["sci"])

studeninfo = {"studid":101,"studname":"Raj","eng":90,"maths":98,"sci":100}

studinfo_print(studeninfo)





# Combining all parameter in one single function
def order_summary(billamt, discount, *items, **details):
    disamt = discount * billamt / 100
    print("Items ordered:", items)
    print("Order details:")
    print("\tCount:",len(items))
    print("\tPayment Type:", details["paymenttype"])
    print("Bill Amount:", billamt)
    print("Discount:", disamt)
    print("Pay Amount:", billamt - disamt)


order_summary(2000,5, "Pizza", "Coke", table=5, take_away=False, no_of_items=2, paymenttype="Card")



#A nested function is a function defined inside another function.
#inner function is only accessible inside the outer function.

def login(username, password):
    def validate():
        return username == "admin" and password == "1234"

    if validate():
        print("Login successful!")
    else:
        print("Login failed.")
        
login("admin","1234")



#closure is a function that remembers and can access variables from its enclosing scope even after that scope has finished executing
def process_payment(amount):
    tax_rate = 0.18  # 18% tax

    def calculate_total():
        return amount + (amount * tax_rate)  # uses outer variables

    return calculate_total  # returning the inner function

# Create a closure instance
payment = process_payment(1000)

# Call the returned inner function
print(payment())  # Output: 1180.0



