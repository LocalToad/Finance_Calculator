import Income
import login

user = login.login()
income = Income.incmain(user, Income.user_settings)
print(income)