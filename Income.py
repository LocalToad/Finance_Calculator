
user_settings = (
    {'name':'toad', 'salary':False, 'wage':0, 'hours':0},
    {'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0},
)


def incmain(index):
    salary = user_settings[index].get('salary')
    isboolean = isinstance(salary, bool)
    if isboolean:
        if salary:
            income = user_settings[index].get('wage')
            return income
        elif user_settings[index].get('hours') == 0:
            print("Not working")
            return 0
        else:
            wage = user_settings[index].get('wage')
            hours = user_settings[index].get('hours')
            income = wage * hours
            return income
    if not isboolean:
        print("Error 402001")
        return -1
    else:
        print("Error 401111")
        return -1