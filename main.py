import Income
import login
import Hard_Expense
while (True):
    user = login.login()
    if user == "exit":
        break
    else:
        income = Income.incmain(user, Income.grabUserSettings())
        hard_expense = Hard_Expense.expense(user, settings)
        net = income - hard_expense
        print(income)
        print(hard_expense)
        print(net)
