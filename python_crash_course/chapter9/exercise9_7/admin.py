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

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = [
            "can add post", "can delete post", "can ban user",
            ]

    def show_privileges(self):
        print(self.privileges)


user1 = Admin("Luigui", "Augusto", "luigui.augusto@hotmail.com")
user1.describ_user(user1.set_describ_user())
user1.show_privileges()