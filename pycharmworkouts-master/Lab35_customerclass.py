from pandas.core.config_init import colheader_justify_doc


class customer():
    def __init__(self,custid,fname,lname,age,prof):
        self.cusid = custid
        self.fname = fname
        self.lname = lname
        self.age = age
        self.prof = prof

    def display_custinfo(s):
        print("Customer Id:",s.cusid)
        print("FirstName:",s.fname)
        print("LastName:", s.lname)
        print("Age:", s.age)
        print("Profession:",s.prof)

    #static method
    def about_customer(msg):
        print(msg)


#Create Object for the class customer
c1 = customer(1001,"Ramesh","Kumar",25,"Teacher")
c2 = customer(1002,"Vimal","Raj",30,"Lawyer")
c2.display_custinfo()
print("===================")
c1.display_custinfo()

print("===================")

#c1.about_customer("its about class through object")
customer.about_customer("Its about the class")
c1.about_customer()




"""
writing java code for the same customer class

class customer
{
    public customer(int custid,string fname,string lname,int age,string prod)
    {
        cid = custid;
        fname = fname;
        lname = lname;
        age = age;
        prof = prof
    }
    public void display_custinfo()
    {
        System.out.print("CustId" + cid)
    }
    public static void about_customer()
    {
    
    }
}

customer c1 = new customer(1001,"karthik","raj",25,"Teacher");
c1.display_custinfo();
customer.about_customer();
c1 = new customer(1002,"karthik","raj",25,"Teacher");
"""


