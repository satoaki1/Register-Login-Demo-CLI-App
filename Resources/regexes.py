"""
All emails must be strings separated into two parts by @ symbol.
"""
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

"""
All passwords:
- Should have at least one number.
- Should have at least one uppercase and one lowercase character.
- Should have at least one special symbol.
- Should be between 6 to 20 characters long.
"""
password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

"""
All Phone Numbers must:
- Begins with 0
- Then contains 6,7 or 8 or 9.
- Then contains 9 digits
"""
phone_no_regex = "(0)?[6-9][0-9]{9}"