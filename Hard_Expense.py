
default_dict = {
    'snake':[522, 30, 185, 175, 140.32, 168.16, 39.45],
    'toad':[0, 0, 0, 0, 0, 0, 0]
    }
#value types
#default_array = [float.00, float.00, float.00, float.00, float.00, float.00, float.00]
#value name
#default_array = [Rent, Internet, Phone, Therapy, Storage, Student Loans, Subscriptions]
def settings(key, settings_dict):
    if settings_dict == None:
         #if nothing imputed into settings_array return the default array
         default_array = default_dict.get(key)
         return default_array
    elif settings_dict != None:
        #replace this with a download of the data from the file
        settings_array = settings_dict.get(key)
        return settings_array
    else:
        print("Error 501000")
        return 501000

def expense(settings_array):
    #check the settings_array var and see what the arr variable will be set to
    arr = settings(settings_array)




