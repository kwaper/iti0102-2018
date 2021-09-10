"""Check if given ID code is valid."""


def check_your_id(id_code: str):
    """Check if given ID code is valid and return the result."""
    if len(id_code) != 11 or not id_code.isdecimal():
        return False
    gender = check_gender_number(int(id_code[0]))
    year = check_year_number_two_digits(int(id_code[1:3]))
    month = check_month_number(int(id_code[3:5]))
    day = check_day_number(int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7]))
    born_order = check_born_order(int(id_code[7:10]))
    control_number = check_control_number(id_code)
    return all([gender, year, month, day, born_order, control_number])


def check_gender_number(gender_number: int):
    """Check if given value is correct for gender number in ID code."""
    if 0 < gender_number <= 6:
        return True
    else:
        return False


def check_year_number_two_digits(year_number: int):
    """Check if given value is correct for year number in ID code."""
    if 0 <= year_number <= 99:
        return True
    else:
        return False


def check_month_number(month_number: int):
    """Check if given value is correct for month number in ID code."""
    if 0 < month_number <= 12:
        return True
    else:
        return False


def check_day_number(year_number: int, month_number: int, day_number: int):
    """Check if given value is correct for day number in ID code."""
    if month_number <= 7 and month_number % 2 != 0 and year_number % 4 != 0 and 1 <= day_number <= 31 and month_number != 2:
        return True
    if month_number >= 8 and month_number % 2 == 0 and year_number % 4 != 0 and 1 <= day_number <= 31:
        return True
    if month_number >= 8 and month_number % 2 != 0 and year_number % 4 != 0 and 1 <= day_number <= 30:
        return True
    if month_number <= 7 and month_number % 2 == 0 and year_number % 4 != 0 and 1 <= day_number <= 30 and month_number != 2:
        return True
    if month_number == 2 and year_number % 4 == 0 and 1 <= day_number <= 29:
        return True
    if month_number == 2 and year_number % 4 != 0 and 1 <= day_number <= 28:
        return True
    else:
        return False


def check_leap_year(year_number: int):
    """Check if given year is a leap year."""
    if year_number % 4 == 0 and year_number % 100 != 0:
        return True
    if year_number % 400 == 0:
        return True
    else:
        return False


def check_born_order(born_order: int):
    """Check if given value is correct for born order number in ID code."""
    if 0 <= born_order <= 999:
        return True
    else:
        return False


def check_control_number(id_code: str):
    """Check if given value is correct for control number in ID code."""
    kordajad_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    kordajad_2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
    sum = 0
    for i in range(10):
        sum += kordajad_1[i] * int(id_code[i])
    if sum % 11 == int(id_code[-1]) and sum != 10:
        return True
    if sum % 11 == 10:
        sum = 0
        for i in range(10):
            sum += kordajad_2[i] * int(id_code[i])
        if sum % 11 == int(id_code[-1]):
            return True
        else:
            return False
    else:
        return False


def get_data_from_id(id_code: str):
    """Get possible information about the person."""
    d = id_code[5:7]
    m = id_code[3:5]
    y = get_full_year(int(id_code[0]), int(id_code[1:3]))
    gender = get_gender(int(id_code[0]))
    id = check_your_id(id_code)
    if id:
        return f"This is a {gender} born on {d}.{m}.{y}"
    else:
        return "Given invalid ID code!"


def get_gender(gender_number: int):
    """Define the gender according to the number from ID code."""
    if gender_number % 2 != 0:
        return "male"
    if gender_number % 2 == 0:
        return "female"


def get_full_year(gender_number: int, year: int):
    """Define the 4-digit year when given person was born."""
    if gender_number == 1 or gender_number == 2:
        year = 1800 + year
        return year
    if gender_number == 3 or gender_number == 4:
        year = 1900 + year
        return year
    if gender_number == 5 or gender_number == 6:
        year = 2000 + year
        return year


if __name__ == '__main__':
    print("Full message:")
    print(get_data_from_id("39906173722"))
