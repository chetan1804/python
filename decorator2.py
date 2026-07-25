import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@decorator
def long_running_task():
    print("Starting long-running task...")
    time.sleep(3)  # Simulate a long-running task
    print("Long-running task completed!")

long_running_task() 