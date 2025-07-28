# validate email address import re

import re  # regex operation 

def is_valid_email(email): # checks if the input string matches a basic email pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Example usage  
#In the __main__ block, it tests several email addresses and prints whether each is valid or invalid according to the pattern
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "invalid-email@",
        "another.user@domain.co.uk",
        "bad@domain",
        "good.email123@sub.domain.com"
    ]
    for email in test_emails:
        print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")

## udemy code 
# email validate function 
def is_valid_email(email):
    """ This function check the email is valid or not """
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+$'
    return re.match(pattern, email) is not None
# calling function
print(is_valid_email("test@gmail.com"))
print(is_valid_email("invalid-email"))