import Income
import login
import Hard_Expense
while (True):
    user = login.login()
    if user == "exit":
        break
    else:
        income = Income.incmain(user, Income.user_settings)
        hard_expense = Hard_Expense.expense()
        net = income - hard_expense
        print(income)
        print(hard_expense)
        print(net)
