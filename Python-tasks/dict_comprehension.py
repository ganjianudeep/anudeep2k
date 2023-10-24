class dict_comprehension:
    def __init__(self, data):
        self.data = data
    def square(self):
        # method to return square of value
        return {key: value**2 for key, value in self.data.items()}

data = {"a": 2, "b": 3, "c": 4}
object = dict_comprehension(data)   # create instance of class
new_dict = object.square()      # create new_dict to store squared numbers
print(new_dict)