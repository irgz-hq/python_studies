current_users = ['Luigui', 'Ravena', 'Trailas', 'Weza', 'Patas']
new_users = ['trailas', 'Taygaz', 'wEZA']
current_users_l = []
for users in current_users:
    current_users_l.append(users.lower())

for users in new_users:
    if users.lower() in current_users_l:
        print('will need to enter a new username')
    else:
        print('the username is available')