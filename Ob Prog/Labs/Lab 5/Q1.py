


from typing_extensions import Self


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        

    
    def get_area(self):
        area = self.height * self.width
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.height) + (2 * self.width) 
        return perimeter    

    def print_rectangle(self):
        row = self.height
        col = self.width
        for i in range(row):
            for j in range(col):
                if i==0 or i==(row-1) or j==0 or j==(col-1):
                    print("*", end = " ")
                else:
                    print(" ", end=" ")
            print()
    def __str__(self):
       return f"{'Area:':17}{self.get_area()}\n{'Perimeter:':17}{self.get_perimeter()}\n"

        
class Square(Rectangle): 
    def __init__(self,length):
        super().__init__(length,length)
        self.length = length
    
    def print_square(self):
        return super().print_rectangle()
        


def main():
    print("Shape Calculator")
    
    again = "y"
    while again == "y":
        print()
        choice = input("Rectangle or square? (r/s): ")
        if choice == "r":
    
            height = int(input("Enter a height:  "))
            width = int(input("Enter a width:   "))

            rectangle = Rectangle(height, width)

            print(rectangle)
            rectangle.print_rectangle()
            print()
            again = input("Continue? (y/n) ")
            print()



        if choice == "s":
            length = int(input("Enter a length:  "))
            square = Square(length)
            print(square)
            square.print_square()
            print()
            again = input("Continue? (y/n) ")
            print()


        if choice != "s" and choice != "r":
            print()
            print("Pls choose a valid option")
            print()
            continue
        
    print("Bye!")
    

if __name__ == "__main__":
    main()
