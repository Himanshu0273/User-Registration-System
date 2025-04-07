import re

def valid_first_name(s):
    if re.match("Cap([a-z] | [A-Z])", s):
        return True     
    else:
        return False
    
first_name=input("Enter Valid First Name: ")
if valid_first_name(first_name):
    print("Valid First Name, Continue ahead!!")
else:
    print("First name is invalid, does not start with 'Cap'")