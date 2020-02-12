import time
# before = time.time()
# for i in range(0,20000000):
#    pass
# after = time.time()
# print("that took", after-before, "seconds")

import datetime
while(True):
    dt = datetime.datetime.now()
    time.sleep(1)
    print(dt)