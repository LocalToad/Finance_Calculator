import json
import os
import datetime
from datetime import date

settings = {
        "toad": {'salary': False, 'wage': 0, 'hours': 0},
        "snake": {'salary': True, 'wage': 2477.12, 'hours': 0}
    }





    # = (
       # {'name':(str), 'salary':(bool), 'wage':(float.00), 'hours':(float.0)},
        #{'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0}
    #)

def incomeWageSalaryMath(s, dict, key):
    if s:
        income = dict.get(key).get('wage')
        return income
    elif dict.get(key).get('hours') == 0:
        print("Not working")
        return 0
    else:
        wage = dict.get(key).get('wage')
        hours = dict.get(key).get('hours')
        income = wage * hours
        return income
# Error cases or success cases reture True-y values
# Other cases that cause incmain to continue looping return False-y values

def incmain(key, settings_dict):
    if not settings_dict or not isinstance(settings_dict, dict) or not key:
        return True # replace with error code

    salary = settings_dict.get(key).get('salary')
    isboolean = isinstance(salary, bool)

    cmd = input("Would you like to continue (y/n) or (edit)? ")
    if cmd.lower() == 'y':
        if isboolean:
            return incomeWageSalaryMath(salary, settings_dict, key)
        else:
            print("Eror 402001")
            return 402001
    elif cmd.lower() == 'n':
        print("Exiting Calculator")
        return incomeWageSalaryMath(salary, settings_dict, key)

    elif cmd.lower() == 'edit':
        if inc_write(key, settings_dict):
            # User chose to exit, equivalent to break
            return incomeWageSalaryMath(salary, settings_dict, key)
    else:
        print("Error 401050")
        return 401050

def inc_write(key, settings_dict):
    print("name(str), salary(bool), wage(float.00), hours(float.0)")
    feature = input("Which feature do you want to edit? ").lower()
    print(settings_dict[key][feature])
    a = input("Do you want to change the value?(y/n) ")
    if a.lower() == 'y':
        new = input(f"Input the New value for {feature}? ").lower()
        if feature == 'wage' or feature == 'hours':
            new = float(new)
        elif feature == 'salary':
            if new == 'true':
                new = True
            if new == 'false':
                new = False
        settings_dict[key][feature] = new
        with open('Dicts.json', 'w') as f:  # Open in binary write mode ('wb')
            json.dump(settings_dict, f)
        return False
    elif a.lower() == 'n':
        print("temp done")
        return True
    else:
        print("Error 401080")
        return 401070




