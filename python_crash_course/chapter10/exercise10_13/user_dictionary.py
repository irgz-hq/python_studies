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
    userlastname = input("What is your last name? ")
    age = input("What is your age? ")
    dict_username = {"username": username, "userlastname": userlastname, "age": age}
    print(dict_username["username"])
    contents = json.dumps(dict_username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path_str = "python_crash_course/chapter10/exercise10_13/"
    path_str += "favorite_number.txt"
    path = Path(path_str)
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username['username']}!")
        print(f"your information are: {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username['username']}!")
        print(f"your information are: {username}")
    


greet_user()