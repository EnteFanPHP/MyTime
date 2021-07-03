from datetime import datetime
from datetime import date
import time
import calendar

my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]
dateFormated = datetime.today().strftime('%d.%m.%Y')

print("Today is a: " + weekday)
print("Today is the: " + dateFormated)
