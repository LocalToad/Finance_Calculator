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
                1: {"trunk": []
                },
                2: "null"
             }
        },
        {
            "file": 20,
            "name": "login.py",
            "types": {
                1: {"login()": ["User", "User_List", "index"]
                },
                2: "null"
            }
        },
        {
            "file": 30,
            "name": "errors.py",
            "types": {
                1: {
                    "errtypechecker()": ["err"],
                    "errors()": ["errorcode", "file", "filecode", "filename", "type", "name", "code"],
                    "errfixneed()": ["code"]
                },
                2: [
                    "dictionary"
                ]
            }
        },
        {
            "file": 40,
            "name": "income.py",
            "types": {
                1: {
                    "incmain()": ["salary", "isboolean", "income", "wage", "hours"]
                },
                2: [
                    "user_settings"
                ]
            }
        }
    ]


def errtypechecker(err):
    if err == 0:
        return "other"
    if err == 1:
        return "function"
    if err == 2:
        return "globalvar"

#Incorrect Var, Unrecognized Var type,
def errfixneed(code):
    if code == 0:
        return "Incorrect Input"
    if code == 1:
        return "Unrecognized Variable type"
    if code == 2:
        return "No value returned"

def errors(err):
    errorcode = str(err)
    file = errorcode[1] + errorcode[0]
    filecode = int(file) - 1
    file = dictionary[filecode]
    filename = file.get("name")
    type = errtypechecker(int(errorcode[2]))
    name = file.get("types")[int(errorcode[2])][int(errorcode[3])]
    if file.get("typees")[int(errorcode[2])] == 1:
        code = file.get("types")[int(errorcode[2])][int(errorcode[3])][int(errorcode[4])]
        print(filename, type, name, code)
    else:
        print(filename, type, name)
    print(errfixneed(int(errorcode[5])))
