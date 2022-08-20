# copyright (c) 2022 amit-curiosity
import calendar
from datetime import date

# year_to_print = 2022
# month_to_print = 8
# number_of_months_in_a_row = 3
# spaces_between_each_day_of_week = 4
# number_of_line_per_week = 1
# number_of_column_space_between_months = 6
current_date = date.today()
# print(current_date)

year_to_print = current_date.year
month_to_print = current_date.month
# print(calendar.calendar(year_to_print,
#                         spaces_between_each_day_of_week,
#                         number_of_line_per_week,
#                         number_of_column_space_between_months,
#                         number_of_months_in_a_row))

print(calendar.month(theyear=year_to_print, themonth=month_to_print, w=4, l=1))
