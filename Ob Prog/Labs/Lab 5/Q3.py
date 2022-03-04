
import random

class RandomList(list):
    def __init__(self, length):
        for i in range(length + 1):
            if i == 0:
                continue
            else:
                self.append(random.randint(1,100))
                

    def __str__(self) -> str:
        amount = len(self)
        total = sum(self)
        average = round((total / amount),2)
        
        
        return f"Integers:  {tuple(self)}\nCount:     {amount}\nTotal:     {total}\nAverage:   {average}"
        #If i dont put self with tuple or list it completely breaks so idk how to get it without the brackets


def main():
    again = "y"
    while again == "y":
        print("Random Integer List")
        print()
        num = int(input("How many random integers would you like?:  "))
        print()
        the_list = RandomList(num)
        print("Random Integers")
        print("=========================")
        print(the_list)
        print()
        again = input("Continue? (y/n) ")
        print()
    print("Cya!")

if __name__ == "__main__":
    main()