### BEGIN Dependencies ###
import datetime
from pytz import timezone
### END Dependencies ###

TIMEZONE = timezone('America/Los_Angeles')

def time_stamp(): # YYYY-MM-DD_HH-MM-SSS, last digit is 1/10th of the second
    now = datetime.datetime.now(TIMEZONE)
    formatted_datetime = now.strftime(f"%Y-%m-%d_%H-%M-%S") + str(int( now.microsecond / 100000 ))
    return formatted_datetime

def date(): # YYYY-MM-DD
    now = datetime.datetime.now(TIMEZONE)
    formatted_datetime = now.strftime(f"%Y-%m-%d")
    return formatted_datetime
