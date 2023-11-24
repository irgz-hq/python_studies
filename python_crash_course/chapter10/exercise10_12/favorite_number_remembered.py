from pathlib import Path
import json

path_str = "python_crash_course/chapter10/exercise10_12/"
path_str += "favorite_number.txt"
path = Path(path_str)


def get_stored_username(path):

    """Get favorite number if available."""
    

    if path.exists():
        favorite_number = path.read_text()
        favorite_number = json.loads(favorite_number)
        return favorite_number
    else:
        return None
    
def get_new_username(path):

    """register the number if it does not exist"""

    favorite_number = input("Enter your favorite number")
    favorite_number = json.dumps(favorite_number)
    path.write_text(favorite_number)
    print("we are registred your favorit number")

def greet_number(path):
    """say the favorite number and calls the outhers functions"""


    favorite_number = get_stored_username(path)

    if favorite_number:
        print(f"your favorit number is {favorite_number}")
    else:
        get_new_username(path)


greet_number(path)