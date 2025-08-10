#how to read error codes
#first 2 digit will tell which file
#10 = main.py, 20 = login.py, 30 = errors.py, 40 = income.py
#next digit tells if it is a function or a global variable
#1-function, 2-global variable
#next digit tells error type
#
from errno import errorcode
from fileinput import filename

dictionary = [
        {
            "file": 10,
            "name": "main.py",
            "types": {
                '1': {"trunk": []
                },
               '2': "null"
             }
        },
        {
            "file": 20,
            "name": "login.py",
            "types": {
                '1': {"login()": ["User", "User_List", "index"]
                },
                '2': "null"
            }
        },
        {
            "file": 30,
            "name": "errors.py",
            "types": {
                '1': {
                    "errtypechecker()": ["err"],
                    "errors()": ["errorcode", "file", "filecode", "filename", "type", "name", "code"],
                    "errfixneed()": ["code"]
                },
                '2': [
                    "dictionary"
                ]
            }
        },
        {
            "file": 40,
            "name": "income.py",
            "types": {
                '1': {
                    "incmain()": ["salary", "isboolean", "income", "wage", "hours"]
                },
                '2': [
                    "user_settings"
                ]
            }
        }
    ]


def errTypeChecker(err):
    if err == 0:
        return "other"
    if err == 1:
        return "function"
    if err == 2:
        return "globalvar"

#Incorrect Var, Unrecognized Var type,
def errFixNeed(code):
    if code == 0:
        return "Incorrect Input"
    if code == 1:
        return "Unrecognized Variable type"
    if code == 2:
        return "No value returned"

def errors(err):
    # Convert errcode to string
    # e.g 402001
    error_code = str(err)

    # Reverse first two numbers to get file code
    # e.g 04
    file = error_code[1] + error_code[0]

    # subtract 1 to get index
    try:
        # e.g 3
        file_code = int(file) - 1

        # look up filecode to get file
        file = dictionary[file_code]

        #grab name from file
        # e.g income.py
        file_name = file.get("name")

        #getting the type of error from the 3rd space in the error code
        # e.g 402001 -> 2 ->
        type_ = errTypeChecker(int(error_code[2]))
        er = error_code[2]
        # Get the full name of the error code from the 3rd and 4th spaces in the error code
        err = file.get("types").get(error_code[2])

        # Get name of the function from the dictionary
        name = list(err)[int(error_code[3])]

        # Grab fix needed from last space in code
        fix_needed = errFixNeed(int(error_code[5]))

        if int(error_code[2]) == 1:
            code = file.get("types").get(error_code[2]).get(name)[int(error_code[4])]
        else:
            code = None
        print(file_name, type_, name, code, fix_needed)
        return file_name, type_, name, code, fix_needed
    except KeyError:
        print("Error, malformed error code")
        raise KeyError



