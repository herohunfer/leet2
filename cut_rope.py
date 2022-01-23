import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer

class Timer:
    def __enter__(self):
        """Start a new timer as a context manager"""
        self.start = time.time()
        return self

    def __exit__(self, *exc_info):
        """Stop the context manager timer"""
        print("Time to finish the task: ", time.time()-self.start)

@functools.lru_cache
@timer
def cutRope(n: int):
    if n <= 1:
        return n

    currentMax = n
    for i in range(1, n):
            currentMax = max(currentMax, cutRope(i)*(n-i))
    return currentMax

if __name__ == "__main__":
    with Timer():
        for _ in range(100):
            print(cutRope(5))
