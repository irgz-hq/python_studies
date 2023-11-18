number = input("Digit a number multiple of ten: ")
remainder_ten = float(number) % 10
if remainder_ten == 0:
    print("You got it right, the number is a multiply of ten!")
else:
    print("You made a mistake, the number is not multiple of ten")