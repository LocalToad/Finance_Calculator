
import pickle


#def infoedit(index):

def grabUserSettings():
    with open('Dicts.txt', 'rb') as f:  # Open in binary read mode ('rb')
        user_settings = pickle.load(f)
        return user_settings
    # = (
       # {'name':(str), 'salary':(bool), 'wage':(float.00), 'hours':(float.0)},
        #{'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0}
    #)


def incmain(index, settings_dict):
    salary = settings_dict[index].get('salary')
    isboolean = isinstance(salary, bool)
    while True:
        cmd = input("Would you like to continue (y/n) or (edit)? ")
        if cmd.lower() == 'y':
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
                print("Eror 402001")
                return 402001
        elif cmd.lower() == 'n':
            print("Exiting Calculator")
            break
        elif cmd.lower() == 'edit':
            inc_write(index, settings_dict)
        else:
            print("Error 401050")
            return 401050

def inc_write(index, settings_dict):
    print("name(str), salary(bool), wage(float.00), hours(float.0)")
    feature = input("Which feature do you want to edit? ").lower()
    print(settings_dict[index][feature])
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
        settings_dict[index][feature] = new
        with open('Dicts.txt', 'wb') as f:  # Open in binary write mode ('wb')
            pickle.dump(settings_dict, f)
    elif a.lower() == 'n':
        print("temp done")
        break
    else:
        print("Eror 401080")
        return 401070