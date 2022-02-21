import locale as lc
print("Monthly Payment Calculator")
print()
choice = "y"
while choice == "y":
    print("DATA ENTRY")

    loan_amount = int(input("Loan Amount:         "))
    loan_amount = round(loan_amount,2)
    yearly_intrest = float(input("Yearly Intrest Rate: ")) #i couldnt get decimal to work, kept getting module error

    yearly_intrest = yearly_intrest / 100
    monthly_intrest= yearly_intrest/ 12
    years = int(input("Years:               "))
   
    lc.setlocale(lc.LC_ALL, "us")
    spacing = "25"
    
    months = years * 12
    monthly_payment = loan_amount * monthly_intrest /  (1 - 1 / (1 + monthly_intrest) ** months)
    monthly_payment = lc.currency(monthly_payment,grouping=True)
    loan_amount = lc.currency(loan_amount,grouping=True)
    
    
    print()
    print("FORMATTED RESULTS")
    print(f"{'Loan amount':24}{loan_amount:>11}")
    print(f"{'Yearly Intrest Rate:':25}{yearly_intrest:>10.1%}")
    print(f"{'Number Of Years:':{spacing}}{years:>10}")
    print(f"{'Monthly Payment:':24}{monthly_payment:>11}")
    print()
    choice= input("Continue? (y/n): ")
    print()
print("Cya!")
print()