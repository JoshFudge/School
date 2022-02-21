

import csv



FILENAME = "customers.csv"






class Customer():
    customer_list = []

    def __init__(self,id,firstName,lastName,company,address,city,state,zip):
        self.id = id
        self.firstName = firstName
        self.last_Name = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        Customer.customer_list.append(self)



    def read_file():
        # When it starts set it to true as the csv file starts with the line with the attributes(Id,names,address,...) 
        # and we dont want that one in the list
        top_line = True


        with open(FILENAME,"r",newline="") as f:
                reader = csv.reader(f)


                for line in reader:

                    # if its the first line
                    if top_line == True:
                        #only change this variable to false for this lines turn and not add to the list
                        top_line = False

                        # and continue to the second line
                        continue
                    else:
                        
                        #           Id     FName    LName  Company  Address City   State   Zip
                            Customer(line[0], line[1], line[2],line[3],line[4],line[5],line[6],line[7])




             

    def find_cust(customer_id):
        Customer.read_file()
        for customer in Customer.customer_list:
            if customer.id == customer_id:
                return customer
        else:
                return "Nah, No customer with that ID"
            




def main():
    print('Customer Viewer')
    print()
    again = "y"

    while again == "y":

        customer_id = input("Enter a Customer ID (101-600):      ")

        answer = Customer.find_cust(customer_id)
        print()

        if answer == "Nah, No customer with that ID":
            print()
            print(answer)
        else:
            
                if answer.company != "":
                    print(f"{answer.firstName} {answer.last_Name}\n{answer.company}\n{answer.address}\n{answer.city} {answer.state} {answer.zip}")
                else:
                    print(f"{answer.firstName} {answer.last_Name}\n{answer.address}\n{answer.city} {answer.state} {answer.zip}")
        print()
        again = input("Find another customer? (y/n)     ")
    print()
    print("Adios!")
    









if __name__ == "__main__":
    main()