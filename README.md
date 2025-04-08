**User Registration Validator**

This is a simple Python program that validates user input during registration.
It checks the First Name, Last Name, Email Address, Phone Number, and Password against specific rules using regular expressions (regex).

Features
First Name and Last Name Validation

Must start with a capital letter.

Must have at least 3 letters.

Email Validation

Supports formats like abc.xyz@domain.com, abc@domain.com, etc.

Only .com and .co.in domains are allowed.

Phone Number Validation

Must be in the format: country-code mobile-number
Example: 91 9919819801

Country code should be two digits.

Password Validation

Minimum 8 characters.

Must contain at least one uppercase letter.

Must contain at least one digit.

Must contain exactly one special character from !@#$%^&*.

How It Works
The program asks the user to input their first name.

If valid, it continues to ask for last name, email, phone number, and password.

Each field is validated immediately.

If any field is invalid, an appropriate error message is displayed.

All validations use Python's re module for pattern matching.

Example
bash
Copy
Edit
Enter the First Name: John
Valid First Name, Continue ahead!!
Enter the Last Name: Doe
Valid Last Name, Continue ahead!!
Enter your email address: john.doe@example.com
Email Valid!!
Enter Phone number (Format: 91 9919819801): 91 9876543210
Valid Phone Number!!
Enter your Password: Password@1
Valid Length
Has Capital Letter
Has a Number
Has exactly 1 special character!
Registration Successful!
Requirements
Python 3.x

No external libraries are needed, only the built-in re module is used.

How to Run
Save the code in a file, e.g., registration_validator.py.

Run the file using:

bash
Copy
Edit
python registration_validator.py
Follow the prompts to enter your details.
