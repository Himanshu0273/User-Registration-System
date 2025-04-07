import re

def valid_name(s):
    if re.match(r"^[A-Z][a-zA-Z]{2,}$", s):
        return True     
    else:
        return False
    
first_name=input("Enter the First Name: ")
#Check first name
if valid_name(first_name):
    print("Valid First Name, Continue ahead!!")
    
    #Check Last Name
    last_name = input("Enter the Last Name: ")
    if valid_name(last_name):
        print("Valid Last Name, Continue ahead!!")
        
    else:
        print("Last name is invalid!")
        
        
else:
    print("First name is invalid!")