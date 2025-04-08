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

#Function to check if valid password:
def valid_password(s):
    check1 = r"^(?=.*[A-Z]).{8,}$"
    if re.match(check1, s):
        print("Valid")
        # if re.search(r"[A-Z]", s):
        #     print("Has capital!")
    return False

def valid_number(s):
    pattern= r"[\d]{2} [0-9]{10}"
    if re.match(pattern, s):
        return True
    return False

def valid_password(s):
    check1 = r".{8,}"
    if re.match(check1, s):
        print("Valid")
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
            
            #Check Valid Phone Number:
            phn = input("Enter Phone number: ")
            
            if (valid_number(phn)):
                print("Valid phone number!!")
                
                #Valid Password
            else:
                print("Not Valid phone number!")
        else:
            print("Invalid Email!")
        
    else:
        print("Last name is invalid!")
        
        
else:
    print("First name is invalid!")