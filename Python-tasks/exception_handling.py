class RuntimeErrorHandler:
    def __init__(self, data):
        self.data = data
    def runtime_error(self):
        #try block checks the required condition if not satisfied goes to except block
        try:
            print("Second element = %d" % (self.a[1]))
            print("Fourth element = %d" % (self.a[3]))
        except:
            print("An error occurred")

if __name__ == "__main__":
    a = [1, 2, 3]
    # Creating instance of class
    error_handler = RuntimeErrorHandler(a)
    error_handler.runtime_error()


