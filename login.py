def login(user_keys):
    User = input("Welcome, who are you logging data for? ").lower()

    if User in user_keys:
        print("Confirmed")
        return User
    elif User == 'exit':
        return 'exit'
    else:
        print("Error: User not found")
        return False