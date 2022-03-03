# Example of extending (using inheritance) python built-in classes 

class OrderedList(list):
    def __init__(self, length):
        for i in range(length + 1):
            if i == 0:
                continue
            else:
                self.append(i)  # note that 'self' here is a list!


ol = OrderedList(10)
ol2 = OrderedList(5)
ol3 = OrderedList(100)

print(ol)
print(ol2)
print(ol3)
