#how to read error codes
#first 2 digit will tell which file
#10 = main.py, 20 = login.py, 30 = errors.py, 40 = income.py
#next digit tells if it is a function or a global variable
#1-function, 2-global variable
#next digit tells error type
#
from fileinput import filename

def filename(file):
    if file == 10:
        return "main.py"
    if file == 20:
        return "login.py"
    if file == 30:
        return "errors.py"
    if file == 40:
        return "income.py"

def errtypechecker(err):
    if err == 1:
        return "function"
    if err == 2:
        return "globalvar"

def exact(err, file, type):
    if file == 10:
        if type == 1:
            return "trunk"
        if type == 2:
            return "Null"
    if file == 20:
        if type == 1:
            if err == 0:
                return "login()"
        if type == 2:
            return "Null"
    if file == 30:
        if type == 1:
            if err == 0:
                return "filename()"
            if err == 1:
                return "errtypechecker()"
            if err == 2:
                return "exact()"
            if err == 3:
                return "errors()"
        if type == 2:
            return "Null"
    if file == 40:
        if type == 1:
            if err == 0:
                return "incmain()"
        if type == 2:
            if err == 0:
                return "user_settings"

def errors(err):
    file = str(err)[0]+str(err)[1]
    filecode = int(file)
    fileName = filename(filecode)
    errtype = errtypechecker(int(str(err)[2]))
    var = exact(int(str(err)[3]), int(file), int(str(err)[2]))
    print(fileName, errtype)

