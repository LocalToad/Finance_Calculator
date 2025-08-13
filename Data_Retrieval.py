import json
import os
settings = {
        "toad": {'salary': False, 'wage': 0, 'hours': 0},
        "snake": {'salary': True, 'wage': 2477.12, 'hours': 0}
    }

dict = {
    'snake':[522, 30, 185, 175, 140.32, 168.16, 39.45],
    'toad':[0, 0, 0, 0, 0, 0, 0]
    }

def grabIncomeUserSettings(default_settings=settings):
    path = "Dicts.txt"
    if os.path.isfile(path):
        with open(path, 'rb') as f:  # Open in binary read mode ('rb')
            user_settings = json.load(f)

    else:
        with open('Dicts.txt', 'wb') as f:  # Open in binary write mode ('wb')
            user_settings = json.dump(default_settings, f)
    return user_settings

def grabUserData(default_data=dict):
    path = "hard_data.txt"
    if os.path.isfile(path):
        with open(path, 'rb') as f:  # Open in binary read mode ('rb')
            user_data = json.load(f)

    else:
        with open('hard_data.txt', 'wb') as f:  # Open in binary write mode ('wb')
            user_data = json.dump(default_data, f)
    return user_data