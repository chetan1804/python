def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper


@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Chetan")