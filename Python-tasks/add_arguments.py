class Addition:
    def __init__(self):
        #self.name = name
        self.numbers = []               # list to save positional and keyword arguments

    def add_numbers(self, *args, **kwargs):
        for num in args:                        #loop for non keyword arguement
            self.numbers.append(num)
        for key, value in kwargs.items():       #loop for keyword arguement
            self.numbers.append(value)

    def calculate_total(self):                  # calculate_total method to get sum of arguments
        total = 0
        for num in self.numbers:
            total += num
        return total

calculator = Addition()       # creating an instance for Addition class
calculator.add_numbers (2, 4, a=6, b=8)     #calling add_numbers method
total = calculator.calculate_total()
print(f"The sum of the numbers is {total}")