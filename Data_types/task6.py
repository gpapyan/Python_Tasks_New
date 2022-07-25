# The program has a month and a year of two dates. The user enters another date (month and year only).
# Determine if the third date ranges from the first date to the second, inclusive.
# Solve the problem using dict.

from datetime import datetime

date1 = "04.2018"
date2 = "10.2019"
date_to_check = "05.2019"


def dates():
    d1 = date1.split(".")
    d2 = date2.split(".")
    d_check = date_to_check.split(".")

    d1 = [int(d1[1]), d1[0]]
    d2 = [int(d2[1]), d2[0]]
    d_check = [int(d_check[1]), d_check[0]]
    if d1 < d_check < d2:
        print(f"Date is in between the {date1} and {date2} ")
    else:
        print(f"Date is in Not between the {date1} and {date2} ")


dates()
