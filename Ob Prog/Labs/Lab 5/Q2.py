


class Person:
    def __init__(self,FName,LName,Email):
        self.Fname = FName
        self.LName = LName
        self.Email = Email
    
    def __str__(self):
        return f"Name: {self.Fname} {self.LName}\nEmail: {self.Email}"
        
    
class Customer(Person):
    def __init__(self, FName, LName, Email, CustNum):
        super().__init__(FName, LName, Email)
        self.CustNum = CustNum

class Employee(Person):
    def __init__(self, FName, LName, Email,SSN):
        super().__init__(FName, LName, Email)
        self.SSN = SSN

def main():
    print("Customer/Employee Data Center")
    print()

    again = "y"
    while again == "y":

        CorE = input("Customer or employee? (c/e)   ")
        print()

        if CorE == "c":
            print("DATA ENTRY")
            f_name=input("First Name:   ")
            l_name = input("Last Name:  ")
            e_mail = input("Email:  ")
            c_num = input("Number:  ")
            cust = Customer(f_name, l_name, e_mail, c_num)
            if isinstance(cust, Customer) == True:
                print()
                print("CUSTOMER")
                print(cust)
                print(f"Number: {cust.CustNum}")
                print()
                again = input("Continue? (y/n) ")
                print()
            
            else:
                print("Not a valid Customer")
                continue


        if CorE == "e":
            
            print("DATA ENTRY")
            f_name=input("First Name:   ")
            l_name = input("Last Name:  ")
            e_mail = input("Email:  ")
            ssn = input("SSN:  ")
            Emp = Employee(f_name, l_name, e_mail, ssn)
            if isinstance(Emp, Employee) == True:
                print()
                print("EMPLOYEE")
                print(Emp)
                print(f"SSN: {Emp.SSN}")
                print()
                again = input("Continue? (y/n) ")
                print()
            
            else:
                print("Not a valid Employee")
                continue


        

        if CorE != "c" and CorE != "e":
            print()
            print("Pls choose valid option")
            print()
            continue

    
    print("Adios!")
    print()

if __name__ == "__main__":
    main()