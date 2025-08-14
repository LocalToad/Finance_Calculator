from functools import total_ordering

default_dict = {
    'snake':[522, 30, 185, 175, 140.32, 168.16, 39.45],
    'toad':[0, 0, 0, 0, 0, 0, 0]
    }
#value types
#default_array = [float.00, float.00, float.00, float.00, float.00, float.00, float.00]
#value name
#default_array = [Rent, Internet, Phone, Therapy, Storage, Student Loans, Subscriptions]
def settings(key=None, settings_dict=None):
    if settings_dict == None:
         #if nothing imputed into settings_array return the default array
        if key == None:
            key = 'toad'
        default_array = default_dict.get(key)
        return default_array
    else:
        #replace this with a download of the data from the file
        settings_array = settings_dict.get(key)
        return settings_array

def expense(settings_array=None, arr=None):
    #check the settings_array var and see what the arr variable will be set to
    if arr == None:
        if settings_array == None:
            arr = settings()
        else:
            arr = settings_array

    total = 0
    args = len(arr)
    for i in range(args):
        x = arr[i]
        total += x
    return total





