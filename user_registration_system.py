import re

def valid_first_name(s):
    if re.match(r"^[A-Z][a-zA-Z]{2,}$", s):
        return True     
    else:
        return False
    
first_name=input("Enter Valid First Name: ")
if valid_first_name(first_name):
    print("Valid First Name, Continue ahead!!")
else:
    print("First name is invalid.")