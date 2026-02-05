"""

#Simple if condition

age = int(input("Enter Age:"))

if age > 18:
    print("You are eligible to vote")


#if else statement
temp = int(input("Enter Temprature:"))

if temp >= 30:
    print("Its a Hot Day")
else:
    print("Its not a Hot Day")

#if..elif..else statement

mark = int(input("Enter Mark:"))

if mark > 90:
    print("Grade A")
elif mark > 70:
    print("Grade B")
elif mark > 50:
    print("Grade C")
else:
    print("Grade D")


#nested if statement
is_member = True
bill_amt = int(input("Enter Bill Amount:"))
disc_amt = 0
payment_type = "Cash"

if is_member:
    if payment_type == "Cash":
        if bill_amt > 5000:
            disc_amt = bill_amt * 10 /100
        else:
            disc_amt = bill_amt * 5 / 100
    elif payment_type == "UPI":
        disc_amt = bill_amt * 3 /100
    else:
        disc_amt = bill_amt * 2 / 100
else:
    print("Become a member to get a discount")

print("Bill Amount:", bill_amt)
print("Discount Amount:", disc_amt)
print("Amount to Pay:", bill_amt - disc_amt)


# if statement using ternary operator

temp = int(input("Enter Temprature:"))

# value_if_true if_condition else value_if_false
print("Its a Hot Day") if temp > 30 else print("Its not a Hot Day")

"""
#find the greatest of 2 numbers using ternary operator

