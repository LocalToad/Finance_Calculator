import Income
import login
import Hard_Expense

def mainloop():
    while (True):
        settings = Income.grabUserSettings()
        keys = settings.keys()
        user = login.login(keys)
        if user == "exit":
            break
        else:
            income = Income.incmain(user, Income.grabUserSettings())
            hard_expense = Hard_Expense.expense(settings)
            net = income - hard_expense
            print(income)
            print(hard_expense)
            print(net)
        return True

if __name__ == "__main__":
    mainloop()