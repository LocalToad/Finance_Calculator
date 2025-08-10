import Income
import login
while (True):
    user = login.login()
    if user == "exit":
        break
    else:
        income = Income.incmain(user, Income.user_settings)
        print(income)