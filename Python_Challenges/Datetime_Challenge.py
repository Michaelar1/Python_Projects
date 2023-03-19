
import datetime
from pytz import timezone


#   Portland
portland = 'US/Pacific'
pl_time = datetime.datetime.now(timezone(portland)).time()


#   NYC
NY = 'US/Eastern'
ny_time = datetime.datetime.now(timezone(NY)).time()


#   London
london = 'UTC'
london_time = datetime.datetime.now(timezone(london)).time()

branches = {
    "Portland" : pl_time,
    "New York" : ny_time,
    "London" : london_time
    }

def time_in_range(start, end, time):
    #   Returns whether current time is in the range [start, end]
    return start <= current <= end

start = datetime.time(9, 0, 0)
end = datetime.time(17, 0, 0)

def branch_status():
    for place, time in branches:
        x = time_in_range(start, end, time)
        if x == True:
            print("\nThe {} branch is open.".format(place))
        else:
            print("\nThe {} branch is closed.".format(place))


if __name__ == "__main__":
    branch_status()
