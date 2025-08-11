def login():
    User = input("Welcome, who are you logging data for? ").lower()
    User_List = ('toad', 'snake')
    if User in User_List:
        print("Confirmed")
        return User
    elif User == 'exit':
        return 'exit'
    else:
        print("Error: User not found")