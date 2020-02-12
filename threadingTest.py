import threading
import time

def thread1():
    print("thread1 start")
    time.sleep(10)
    print("Thread1 stop")

def thread2():
    print("thread2 start")
    time.sleep(5)
    print("Thread2 cont")
    time.sleep(10)
    print("thread2 stop")

# single threaded version

thread1()
thread2()

print("-" * 40)
# multi threaded version

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()