hyp = lambda a, b: (a**2 + b**2)**(1/2)

def sort_sides(l_in):
    # Вместо pass напишите свою функцию
    l_in.sort(key = lambda a: a[0]**2 + a[1]**2)
    return l_in
            

def get_less(list_in, num):
    # Вместо pass напишите тело функции
    for n in list_in:
        return n if n < num else "None"


def split_date(date):
    # Вместо pass напишите тело функции
    return (int(date[:2]), int(date[3:4]), int(date[4:]))

print(split_date("31012019"))




def exchange(**kwargs):
    
    check_list = ["usd", "rub", "rate"]
    ntf = ""
    
    if len(kwargs) <= 1:
        raise ValueError ("Not enough arguments")
    elif len(kwargs) >= 3:
        raise ValueError ("Too many arguments")
    for s in check_list:
        if s not in kwargs:
           ntf = s
    if ntf == "rub":
        return kwargs["usd"]*kwargs["rate"]
    elif ntf == "usd":
        return kwargs["rub"]/kwargs["rate"]
    elif ntf == "rate":
        return kwargs["rub"]/kwargs["usd"]



def exchange(usd = None, rub = None, rate = None):
    # Вместо pass напишите тело функции
    # Задайте аргументы по умолчанию
    #check_args = [usd, rub, rate]
    actual_args = [0, 0, 0]
    count = 0
    if usd:
        count += 1
        actual_args[0] = usd
    else:
        pass
    if rub:
        count += 1
        actual_args[1] = rub
    else:
        pass
    if rate:
        count += 1
        actual_args[2] = rate
    else:
        pass
    if count == 0:
        raise ValueError ("No arguments given!")
    elif count == 1:
        raise ValueError ("Not enough arguments!")
    elif count == 3:
        raise ValueError ("Too many arguments!")

    
def check_date(day, month, year):

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def is_leap(year):
        if not year % 400: return True
        if not year % 100: return False
        if not year % 4: return True
        return False

    if (type(day) != int) or (type(month) != int) or (type(year) != int): 
        return False

    if (year < 1900) or (year > 2022): return False
    if (month < 1) or (month > 12): return False
    if (day < 1) or (day > 31): return False
    
    if month != 2:
        if day > month_days[month-1]: return False
    else:
        if is_leap(year):
            if day > 29: return False
        else:
            if day > month_days[month-1]: return False
    
    return True


