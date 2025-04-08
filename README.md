Password Validation - Rule 2

This project validates a user's password based on a specific rule.

The password must contain at least one uppercase letter (A-Z) to be considered valid. It should ensure that users create passwords that are not purely lowercase, enhancing password strength and security.

The regular expression used for validation is:
^(?=.*[A-Z]).+$

Some examples of valid passwords are "Password", "HelloWorld123", and "MYpassword!".
Examples of invalid passwords include "password" (no uppercase letters) and "hello123" (all lowercase).

All defined rules must be satisfied for a password to be considered valid.