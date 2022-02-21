


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

        
         

def main():
    again = "y"
    while again == "y":
    
        height = int(input("Enter a height:  "))
        width = int(input("Enter a width:   "))

        rectangle = Rectangle(height, width)

        print(rectangle)
        rectangle.print_rectangle()
        print()
        again = input("Continue? (y/n) ")
        print()
    print("Bye!")
    

if __name__ == "__main__":
    main()
