import time
import datetime

#datetime is a more human readable library for this


print(time.time())



#use this loop to make a perpetual loop that stops for a period of time to 
#stop using CPU, this makes it possible to to run jobs based on time

"""
while True:
	
	today = datetime.date.today()

	time.sleep(8600)



### cron jobs is an easier way to do this, there is a windows eqivalent

"""

import time
import datetime
print(time.time())
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
while True:
    today = datetime.date.today()
    print("Now it's:", today)
    if today != yesterday:
        yesterday = today
        # do something
        print("Now I consider {} yesterday".format(yesterday))
    else:
        time.sleep(8600)






































