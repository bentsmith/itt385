import datetime
#
# now = datetime.datetime.now()
#
# class_end = datetime.datetime(2019,5,3)
#
# time_until = class_end - now
#
# convert timedelta output to days
# print(time_until.days)

in_str = input("Enter a Date:")

fmt = "%m/%d/%y"

# this would be a goodn use of regex to check different formats

then = datetime.datetime.strptime(in_str, fmt)

now = datetime.datetime.now()

time_until = then - now

print(time_until.days)


# or use dateutil pip3 install py-dateutil to handle many formats
# import dateutil.parser
# in_str = input("Enter a date (multiple formats): ")
# then = dateutil.parser.pare(in_str)
# time_until = then - now
# print("That is", time_until.days,"days to go")