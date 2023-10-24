import re

class EmailValidator:
    def __init__(self, email):
        self.email = email

#method is_valid to check if given mailid is valid or not
    def is_valid(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        else:
            return False

if __name__ == "__main__":
    email = input("Enter an email address: ")
    validator = EmailValidator(email)

    if validator.is_valid():
        print("Valid email address")
    else:
        print("Invalid email address")