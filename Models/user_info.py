class user_info():
    user_id = None
    user_name = None
    user_email = None
    user_password = None
    user_gender = None
    user_address = None
    user_phone_no = None

    # Constructor
    def __init__(self, user_id, user_name, user_email, user_password, user_gender, user_address, user_phone_no):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_gender = user_gender
        self.user_address = user_address
        self.user_phone_no = user_phone_no