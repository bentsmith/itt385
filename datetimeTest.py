import datetime

now = datetime.datetime.now()

print("Hour = ", now.hour, "Minutes = ", now.minute)

# old school way
minstr = str(now.minute)
if len(minstr) < 2:
    minstr = "0" + minstr

#new school way
minstr = str(now.minute)
minstr = minstr.zfill(2)

#newer school way
hhmm = str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2)

print(hhmm)

hhmm = now.strftime("%I:%M")
print(hhmm)
# strftime has several different format options such as %B,%I,%d,%A, etc
longversion = now.strftime("%B %d, %y at %I:%M")
print(longversion)