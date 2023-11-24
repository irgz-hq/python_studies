from pathlib import Path
import json

favorite_number = input("Enter your favorite number: ")
path_str = "python_crash_course/chapter10/exercise10_11/favorite_number.txt"
path = Path(path_str)
favorite_number = json.dumps(favorite_number)
path.write_text(favorite_number)
