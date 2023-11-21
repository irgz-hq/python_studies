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

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges([
            "can add post", "can delete post","can ban user",
            ])
        
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)



"""user1 = Admin("Luigui", "Augusto", "luigui.augusto@hotmail.com")
user1.describ_user(user1.set_describ_user())
user1.privileges.show_privileges()"""