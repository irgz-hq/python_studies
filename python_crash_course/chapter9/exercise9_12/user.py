class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.describ = {}
    def set_describ_user(self):
        self.describ = {
            "first name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
            }
    
    def describ_user(self):
        print(self.describ)