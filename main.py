import Income
import login
import Hard_Expense
import Data_Retrieval

DICTS_PATH = "dicts.json"

def mainloop():
    while (True):

        settings = Data_Retrieval.grabJSONifExists(DICTS_PATH)
        keys = settings.keys()
        user = login.login(keys)
        if user == "exit":
            break
        else:
            income = Income.incmain(user, Data_Retrieval.grabJSONifExists(DICTS_PATH))
            hard_expense = Hard_Expense.expense(Hard_Expense.settings(user))
            net = income - hard_expense
            print(income)
            print(hard_expense)
            print(net)
    return True

if __name__ == "__main__":
    mainloop()