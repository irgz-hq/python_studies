from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Usando os valores do enumerador
print(Color.RED)     # Output: Color.RED
print(Color.RED.value)  # Output: 1
print(repr(Color.RED))  # Output: <Color.RED: 1>