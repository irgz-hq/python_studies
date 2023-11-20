class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def set_describ_user(self):
        describ = {
            "first name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
            }
        return describ
    
    def describ_user(self, describ):
        print(describ)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Luigui", "Augusto", "luigui.augusto@hotmail.com")
user1.describ_user(user1.set_describ_user())

print(user1.login_attempts)
for i in range(5):
    user1.increment_login_attempts()

print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)