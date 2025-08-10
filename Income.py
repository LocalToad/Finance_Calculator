
user_settings = (
    {'name':'toad', 'salary':False, 'wage':0, 'hours':0},
    {'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0}
)


def incmain(index, settings_dict):
    salary = settings_dict[index].get('salary')
    isboolean = isinstance(salary, bool)
    if isboolean:
        if salary:
            income = settings_dict[index].get('wage')
            return income
        elif settings_dict[index].get('hours') == 0:
            print("Not working")
            return 0
        else:
            wage = settings_dict[index].get('wage')
            hours = settings_dict[index].get('hours')
            income = wage * hours
            return income
    if not isboolean:
        print("Error 402001")
        return 402001
    else:
        print("Error 401111")
        return 401111