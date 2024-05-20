import re
import uuid

from Resources.regexes import email_regex, password_regex
from Models.user_info import user_info

def generate_userid():
    user_id = uuid.uuid4()

def confirm_cpass(password, confirm_password):
    if confirm_password != password:
        return False
    else:
        return True

def is_valid_email(email_address):
    return re.match(email_regex, email_address)

def is_valid_password(password):
    return re.search(password_regex, password)

def length_validation(info_type, info):
    if info_type == "Phone Number":
        return