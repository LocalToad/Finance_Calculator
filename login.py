def login():
    User = input("Welcome, who are you logging data for").lower()
    User_List = ('toad', 'snake')
    if User in User_List:
        print("Confirmed")
        index = User_List.index(User)
        return index
    else:
        print("Error: User not found")
        login()