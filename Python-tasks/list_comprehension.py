class list_comprehension:
    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        # condition here is lambda function which filters the elements in self.data
        filtered_num = [x for x in self.data if condition(x)]
        return filtered_num

# Usage
data = [1, 2, 3, 4, 5, 6]
object = list_comprehension(data)
# Using lambda function to filter even numbers
even_numbers = object.filter(lambda x: x % 2 == 0)
print("Even numbers:", even_numbers)