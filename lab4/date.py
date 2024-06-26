#task 1 subtract five days from current date.
import datetime

def five_days_ago():
    print(datetime.date.today()- datetime.timedelta(days=5))
print(five_days_ago())
#task 2 program to print yesterday, today, tomorrow.

def today_yesterday_tomorrow():
    print(f"Today is {datetime.date.today()}\nYestarday was\
 {datetime.date.today()- datetime.timedelta(days=1)}\n\
Tomorrow will be {datetime.date.today() + datetime.timedelta(days=1)}")

#task 3 program to drop microseconds from datetime.

def delete_microseconds():
    def drop_microseconds(dt): 
        return dt.replace(microsecond=0)

    now = datetime.datetime.now()
    print(f'Original datetime {now}')

    without_microseconds = drop_microseconds(now)
    print(f'Withoud microseconds {without_microseconds}')
print(delete_microseconds())

#task 4 calculate two date difference in seconds.
def seconds_dif(date1_str, date2_str):
    date_format = '%Y-%m-%d'

    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)

    difference = date2 - date1

    return difference.total_seconds()

day1 = '2024-02-17'

day2 = '2024-02-18'

print(f'Seconds difference is {seconds_dif(day1, day2)}')
