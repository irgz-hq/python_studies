class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def set_describ_user(self):
        describ = {
            "first name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
            }
        return describ
    
    def describ_user(self, describ):
        print(describ)


user1 = User("Luigui", "Augusto", "luigui.augusto@hotmail.com")
user1.describ_user(user1.set_describ_user())