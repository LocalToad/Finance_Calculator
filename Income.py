

user_settings = (
    {'name':'toad', 'salary':False, 'wage':9, 'hours':35},
    {'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0},
)


def incmain(index):
    salary = user_settings[index].get('salary')
    if salary:
        income = user_settings[index].get('wage')
        return income
    else:
        wage = user_settings[index].get('wage')
        hours = user_settings[index].get('hours')
        income = wage * hours
        return income