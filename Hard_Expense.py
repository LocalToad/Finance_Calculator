
default_array = [522, "array"]
#value types
#default_array = [float.00, ]
def settings(settings_array):
    if settings_array == None:
        #if nothing imputed into settings_array return the default array
        return default_array
    elif settings_array != None:
        #replace this with a download of the data from the file
        return settings_array
    else:
        print("Error 501000")
        return 501000

def expense(settings_array):
    #check the settings_array var and see what the arr variable will be set to
    arr = settings(settings_array)




