from pathlib import Path
import json

def get_stored_username(path):

    """Get stored username if available."""

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path_str = "python_crash_course/chapter10/exercise10_14/"
    path_str += "username.txt"
    path = Path(path_str)
    username = get_stored_username(path)

    if username:
        username2 = input("Who are you? ")
        if username == username2:
            print(f"Welcome back, {username}!")
        else:
            print("You arent autorized to enter! ")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
    


greet_user()