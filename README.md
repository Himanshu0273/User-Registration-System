This project validates a user's mobile number based on specific rules.

The mobile number must follow a predefined format where a country code is followed by a space and then a 10-digit mobile number. The country code must consist of exactly two digits, and the mobile number must consist of exactly ten digits without any special characters, spaces (other than the one separating the country code and number), or alphabets.

For example, a valid mobile number would be 91 9919819801, where 91 is the country code and 9919819801 is the 10-digit mobile number. Any deviation from this format, such as missing space, incorrect number of digits, or additional characters, would result in an invalid mobile number.

The regular expression used for validation is:
^\d{2}\s\d{10}$

Some examples of valid mobile numbers include:

91 9919819801

44 7894561230

Examples of invalid mobile numbers include:

919919819801 (missing space)

91 99198 (less than 10 digits)

91-9919819801 (incorrect separator)