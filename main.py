import Income
import login

user = login.login()
income = Income.incmain(user)
print(income)