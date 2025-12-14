"""
დაწერეთ პროგრამა რომელიც მიიღებს თარიღს. პროგრამამ თარიღი უნდა
გადაიყვანოს განსხვავებულ ფორმატში და დაბეჭდოს ეკრანზე. შემომავალი და
გამომავალი თარიღების ფორმატები იხილეთ მაგალითებში.

მაგალითი 1.
Input: 2024-03-22T19:17:42.956376+00:00
Output: 22-03-2024 7:17:42 +0
მაგალითი 2.
Input: 2024-03-04T11:17:42.000123+04:00
Output: 04-03-2024 11:17:42 +4
მაგალითი 3.
Input: 2024-11-14T15:17:42.123000-03:00
Output: 14-11-2024 3:17:42 -3
"""

input_str = input('Enter a date: ')
time_zone_sign = input_str[-6]
input_str_split = input_str.split('T')

date_split = input_str_split[0].split('-')
new_date = '-'.join([date_split[-1], date_split[-2], date_split[-3]])

time_and_zone_split = input_str_split[1].split('+') if time_zone_sign == '+' else input_str_split[1].split('-')

time_split = time_and_zone_split[0].split(':')
new_time = ':'.join([str(int(time_split[0]) % 12), time_split[1], str(int(float(time_split[2])))])

new_timezone = time_zone_sign + time_and_zone_split[1][1]

formatted_date = ' '.join([new_date, new_time, new_timezone])
print(formatted_date)
