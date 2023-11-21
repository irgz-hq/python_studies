from user import User
from privilegis import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges([
            "can add post", "can delete post","can ban user",
            ])