import random

def dice_roll():
    roll = random.randint(1,6)
    return roll




def main():
    counter1=0
    counter2=0
    counter3=0
    counter4=0
    counter5=0
    counter6=0


    print()

    amount = int(input("Enter total amount of dice rolls:   "))

    print()

    for i in range(1,amount + 1):
        num_rolled = dice_roll()
        if num_rolled == 1:
            counter1 += 1

        if num_rolled == 2:
            counter2 +=1

        if num_rolled == 3:
            counter3 +=1

        if num_rolled == 4:
            counter4 +=1

        if num_rolled == 5:
            counter5 +=1

        if num_rolled == 6:
            counter6 +=1

        rolls = {"1": counter1,"2": counter2, "3": counter3,"4":  counter4,"5": counter5, "6": counter6}

    print(rolls)



    prob1= round((counter1/amount),2)
    prob2= round((counter2/amount),2)
    prob3= round((counter3/amount),2)
    prob4= round((counter4/amount),2)
    prob5= round((counter5/amount),2)
    prob6= round((counter6/amount),2)

    print()
    print(f"Rolling the dice {amount} times{':':10}")
    print()
    print(f"Probability of rolling 1:{prob1:>10}")
    print(f"Probability of rolling 2:{prob2:>10}")
    print(f"Probability of rolling 3:{prob3:>10}")
    print(f"Probability of rolling 4:{prob4:>10}")
    print(f"Probability of rolling 5:{prob5:>10}")
    print(f"Probability of rolling 6:{prob6:>10}")





if __name__ == "__main__":
    main()