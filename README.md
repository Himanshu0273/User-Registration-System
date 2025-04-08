This project validates a user's password based on specific rules.

The password must contain exactly one special character. The accepted special characters are: !, @, #, $, %, ^, &, and *. The password should not have zero or more than one special character from this set.

The validation is performed by first ensuring the password meets all other necessary criteria (such as minimum length, presence of an uppercase letter, and a digit), and then by checking that exactly one of the specified special characters is present. If the password contains no special character or more than one, it will be considered invalid.

Some examples of valid passwords include Abcdef1@ and Xyz123$. Examples of invalid passwords include Abcdef12 (no special character) and Xyz@123$ (more than one special character).