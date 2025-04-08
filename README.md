This function validates a user's email address based on specific rules.

The email must have three mandatory parts: the username, the domain, and the primary domain (co). It may also contain two optional parts: a subdomain and a country code (in). The structure must strictly follow the correct placement of the @ and . symbols.

For example, a valid email address would be abc.xyz@bl.co.in, where abc, bl, and co are mandatory, while xyz and in are optional parts. The email must not have misplaced dots or missing components.

The regular expression used for validation is:
^[\w]+(\.[\w]+)?@[\w]+\.co(\.in)?$

Some examples of valid emails are abc@bl.co, abc.xyz@bl.co, and abc.xyz@bl.co.in.
Examples of invalid emails include abc@blcom (missing dot), abc@bl..co (double dots), and abc.bl@co.in (wrong structure).