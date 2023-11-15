ordinal_number = [i for i in range(1, 10)]

for number in ordinal_number:
    if number == 1:
        end_in = 'st'
    elif number == 2:
        end_in = 'nd'
    elif number == 3:
        end_in = 'rd'
    else:
        end_in = 'th'
    print(f'{number}{end_in}\n')
        