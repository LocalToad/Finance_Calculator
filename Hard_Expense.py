from functools import total_ordering
import json
import os

default_dict = {
    'snake':[522, 30, 185, 175, 140.32, 168.16, 39.45],
    'toad':[0, 0, 0, 0, 0, 0, 0]
    }
#value types
#default_array = [float.00, float.00, float.00, float.00, float.00, float.00, float.00]
#value name
#default_array = [Rent, Internet, Phone, Therapy, Storage, Student Loans, Subscriptions]
def sumlist(arr):
    total = 0
    args = len(arr)
    for i in range(args):
        x = arr[i]
        if isinstance(x, (int, float)):
            total += x
        else:
            return 'TypeError'
    return total


#def grabUserData(default_data=default_dict):
  #  path = "hard_data.txt"
  #  if os.path.isfile(path):
  #      with open(path, 'rb') as f:  # Open in binary read mode ('rb')
   #         user_data = json.load(f)

  #  else:
 #       with open('hard_data.txt', 'wb') as f:  # Open in binary write mode ('wb')
 #           user_data = json.dump(default_data, f)
#    return user_data

def settings(key=None, settings_dict=None):
    if settings_dict == None:
         #if nothing imputed into settings_array return the default array
         if key == None:
            key = 'toad'
         default_array = default_dict.get(key)
         return default_array
    elif settings_dict != None:
        #replace this with a download of the data from the file
        settings_array = settings_dict.get(key)
        return settings_array
    else:
        print("Error 501000")
        return 501000

def expense(settings_array=None, arr=None):
    #check the settings_array var and see what the arr variable will be set to
    if arr == None:
        if settings_array == None:
            return 'ERROR'
        else:
            arr = settings(settings_array)

    total = sumlist(arr)

    if total == 'TypeError':
        return 'TypeError'
    else:
        return total




