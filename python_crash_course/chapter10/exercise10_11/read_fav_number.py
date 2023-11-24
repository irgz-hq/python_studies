from pathlib import Path
import json

path_str = "python_crash_course/chapter10/exercise10_11/favorite_number.txt"
path = Path(path_str)
favorite_number = path.read_text()
print(favorite_number)
favorite_number = json.loads(favorite_number)
print(f"Your favorite number is: {favorite_number}")