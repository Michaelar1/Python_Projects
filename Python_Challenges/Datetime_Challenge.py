
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

branch = ["Portland", "New York", "London"]
time = [pl_time, ny_time, london_time]

def time_in_range(start, end, time):
    for x in time:
        #   Returns whether current time is in the range [start, end]
        return start <= current <= end

start = datetime.time(9, 0, 0)
end = datetime.time(17, 0, 0)
current = x

def branch_status():
    for y in branch:
        if x in time = True
            print


if __name__ == "__main__":
    branch_status()
