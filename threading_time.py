import time
import threading
end = None
start = None
def hello():
    global start, end
    start = time.thread_time()
    x = 0
    while x < 10000000:
        pass
        x += 1
    end = time.thread_time()

t = threading.Thread(target = hello, args = ())
t.start()
t.join()

print("The time spent is {}".format(end - start))
