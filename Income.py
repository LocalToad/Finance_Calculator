import json
import os
import datetime
from datetime import date

settings = {
        "toad": {'salary': False, 'wage': 0, 'hours': 0},
        "snake": {'salary': True, 'wage': 2477.12, 'hours': 0}
    }

INCOME_FILE_SUFFIX = '_Income_Report.json'



#def infoedit(index):
def grabJSONifExists(path, default_dict=None):
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return json.load(f)

    else:
        writeJSONtoPath(path, default_dict)
        return default_dict

def writeJSONtoPath(path, dict_in):
    with open(path, 'w') as f:
        json.dump(dict_in, f)

    # = (
       # {'name':(str), 'salary':(bool), 'wage':(float.00), 'hours':(float.0)},
        #{'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0}
    #)


# Error cases or success cases reture True-y values
# Other cases that cause incmain to continue looping return False-y values

def incmain(key, settings_dict):
    if not settings_dict or not isinstance(settings_dict, dict) or not key:
        return True # replace with error code

    salary = settings_dict.get(key).get('salary')
    isboolean = isinstance(salary, bool)
    while True:
        cmd = input("Would you like to continue (y/n) or (edit)? ")
        if cmd.lower() == 'y':
            if isboolean:
                if salary:
                    income = settings_dict.get(key).get('wage')
                    return income
                elif settings_dict.get(key).get('hours') == 0:
                    print("Not working")
                    return 0
                else:
                    cmd = input("Would you like to see your income information?")
                    if cmd.lower() == 'y':
                        # Display income information from user's income information
                        inc_view(key)
                        response = 'n'
                        while response != 'y':
                            cmd = input("Ready to move on? (y/n)")
                            response = cmd.lower()
                            if response == 'y':
                                break
                            print("Okay.")
                    else:
                        print("exiting Calculator")
                        return True

                    # wage = settings_dict.get(key).get('wage')
                    # hours = settings_dict.get(key).get('hours')
                    # income = wage * hours
                    # return income
            if not isboolean:
                print("Error 402001")
                return 402001
        elif cmd.lower() == 'n':
            print("Exiting Calculator")
            return True
        elif cmd.lower() == 'edit':
            if not inc_write(key, settings_dict):
                continue
            else:
                # User chose to exit, equivalent to break
                return True
        else:
            print("Error 401050")
            return 401050

def inc_view(name):
    # will look something like "toad_Income_Report.json"
    full_json_name = f"{name}{INCOME_FILE_SUFFIX}"
    report = income_report(full_json_name)

    if report:
        # loop over every item in the report and average all the incomes
        numbers = []
        for item in report:
            numbers.append(item.value)
            print(f"\n{item.key}: {item.value}")
        average = sum(numbers) / len(numbers)
        print(f"Average Income: {average:.2f}")



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

def income_report(path, report_list=None):
    default_dict = {}
    report = grabJSONifExists(path, default_dict)

    if report_list:
        report[str(date.today())] = report_list
        writeJSONtoPath(path, report_list)

    return report


