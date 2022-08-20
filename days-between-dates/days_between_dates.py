# copyright (c) 2022 amit-curiosity
from datetime import datetime, date


# get days between two specified_dates
def days_between(d1, d2):

    d1 = datetime.strptime(d1, '%Y-%m-%d')
    d2 = datetime.strptime(d2, '%Y-%m-%d')

    return abs((d2 - d1).days)


if __name__ == '__main__':
    # get date_1 and date_2
    date_1 = date(year=2022, month=6, day=17)
    date_2 = date(year=2022, month=9, day=15)

    # print first_date
    print(f'First Date: {date_1}')

    # print second_date
    print(f'Second Date: {date_2}')

    # print message
    print(f'Days Between: {days_between(str(date_1), str(date_2))}')
