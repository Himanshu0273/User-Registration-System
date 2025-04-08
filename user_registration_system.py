import re

#Function for valid name:
def valid_name(s):
    if re.match(r"^[A-Z][a-zA-Z]{2,}$", s):
        return True     
    else:
        return False
    
#Function for valid email:
def valid_email(s):
    pattern = r"^[\w]+(\.[\w]+)?@[\w]+\.(com|co(\.in)?)$"
    if re.match(pattern, s):
        return True
    return False

first_name=input("Enter the First Name: ")
#Check first name
if valid_name(first_name):
    print("Valid First Name, Continue ahead!!")
    
    #Check Last Name
    last_name = input("Enter the Last Name: ")
    if valid_name(last_name):
        print("Valid Last Name, Continue ahead!!")
        
        #Check Valid Email
        email = input("Enter your email address: ")
        if valid_email(email):
            print("Email Valid!!")
            
        else:
            print("Invalid Email!")
        
    else:
        print("Last name is invalid!")
        
        
else:
    print("First name is invalid!")