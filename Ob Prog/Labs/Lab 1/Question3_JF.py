
sales = [[1540.0, 2010.0, 2450.0, 1845.0], # Region 1
         [1130.0, 1168.0, 1847.0, 1491.0], # Region 2
         [1580.0, 2305.0, 2710.0, 1284.0], # Region 3
         [1105.0, 4102.0, 2391.0, 1576.0]] # Region 4
region1 = sales[0]
region2 = sales[1]
region3 = sales[2]
region4 = sales[3]
print("Sales Report")
print()
print(f"{'Region':15} {'Q1':15} {'Q2':15} {'Q3':15} {'Q4':15}")
print(f"{'1':15} {'$'}{region1[0]:5,.2f} {'$':>7}{region1[1]:5,.2f} {'$':>7}{region1[2]:5,.2f} {'$':>7}{region1[3]:5,.2f}")
print(f"{'2':15} {'$'}{region2[0]:5,.2f} {'$':>7}{region2[1]:5,.2f} {'$':>7}{region2[2]:5,.2f} {'$':>7}{region2[3]:5,.2f}")
print(f"{'3':15} {'$'}{region3[0]:5,.2f} {'$':>7}{region3[1]:5,.2f} {'$':>7}{region3[2]:5,.2f} {'$':>7}{region3[3]:5,.2f}")
print(f"{'4':15} {'$'}{region4[0]:5,.2f} {'$':>7}{region4[1]:5,.2f} {'$':>7}{region4[2]:5,.2f} {'$':>7}{region4[3]:5,.2f}")
print()



r1_sum = sum(region1)
r2_sum = sum(region2)
r3_sum = sum(region3)
r4_sum = sum(region4)
total_money = (r1_sum+r2_sum+r3_sum+r4_sum)
print("Sales by region:")
print(f"{'Region 1: ':15} ${r1_sum:,.2f}")
print(f"{'Region 2: ':15} ${r2_sum:,.2f}")
print(f"{'Region 3: ':15} ${r3_sum:,.2f}")
print(f"{'Region 4: ':15} ${r4_sum:,.2f}")
print()

quarter1 = [region1[0],region2[0],region3[0],region4[0]]
quarter2 = [region1[1],region2[1],region3[1],region4[1]]
quarter3 = [region1[2],region2[2],region3[2],region4[2]]
quarter4 = [region1[3],region2[3],region3[3],region4[3]]


q1_sum = sum(quarter1)
q2_sum = sum(quarter2)
q3_sum = sum(quarter3)
q4_sum = sum(quarter4)


print("Sales by quarter:")
print(f"{'Q1: ':15} ${q1_sum:,.2f}")
print(f"{'Q2: ':15} ${q2_sum:,.2f}")
print(f"{'Q3: ':15} ${q3_sum:,.2f}")
print(f"{'Q4: ':15} ${q4_sum:,.2f}")

total = (total_money)
print()
print(f"Total annual sales, all regions:    ${total:,.2f}")