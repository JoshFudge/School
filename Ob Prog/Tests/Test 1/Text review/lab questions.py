# import locale as lc
# from decimal import Decimal
# lc.setlocale(lc.LC_ALL,"en_us")



# print("Monthly Payment Calculator")
# print()
# print("DATA ENTRY")
# loan_amount = int(input(f"Loan Amount:      "))
# yearly_rate= float(input(f"Yearly intrest rate:     "))
# years= int(input("Years:            "))



# yearly_rate = yearly_rate/100
# monthly_interest_rate = yearly_rate /12
# months = (years * 12)


# monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** months)

# monthly_payment = lc.currency(monthly_payment,grouping=True)
# loan_amount = lc.currency(loan_amount,grouping=True)


# # monthly_payment= lc.currency(monthly_payment)

# print()
# print('FORMATTED RESULTS')
# print(f"Loan amount:{loan_amount:>41}")
# print(f"Yearly intrest rate:{yearly_rate:>33,.1%}")
# print(f"Number of years:{years:37}")
# print(f"Monthly payment:{monthly_payment:>37}")


# sales = [[1540.0, 2010.0, 2450.0, 1845.0], # Region 1
#          [1130.0, 1168.0, 1847.0, 1491.0], # Region 2
#          [1580.0, 2305.0, 2710.0, 1284.0], # Region 3
#          [1105.0, 4102.0, 2391.0, 1576.0]] # Region 4

# print("Sales report")
# print()
# print(f"{'Region':20}{'Q1':13}{'Q2':13} {'Q3':13} {'Q4':13}")


# # org_sales=[]
# # for row in sales:
# #     for item in row:
# #         item=lc.currency(item,grouping=True)
# #         org_sales.append(item)
# # print(org_sales)





# R1=[]
# for item in sales[0]:
#     item=lc.currency(item,grouping=True)
#     R1.append(item)
# print(R1)

# R2=[]
# for item in sales[1]:
#     item=lc.currency(item,grouping=True)
#     R2.append(item)
# print(R2)

# R3=[]
# for item in sales[2]:
#     item=lc.currency(item,grouping=True)
#     R3.append(item)
# print(R3)

# R4=[]
# for item in sales[3]:
#     item=lc.currency(item,grouping=True)
#     R4.append(item)
# print(R4)















































