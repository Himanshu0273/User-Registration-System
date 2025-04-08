Password Numeric Validation
This project validates a user's password based on specific rules.

The password must contain at least one numeric digit (0–9). It ensures that users create passwords that are not only alphabetic but also include numerical complexity, thereby increasing security. The password must also meet all previously defined rules to be considered valid.

The regular expression used for this validation is: ^(?=.*\d).+$.

Some examples of valid passwords are "Password1" and "Hello2World". Examples of invalid passwords include "Password" (no digit) and "HelloWorld" (no digit).