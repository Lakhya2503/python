# Debugging Function Calls

def dubbug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for args in args)
        return func(*args, **kwargs)
    return wrapper

def hello():
    print("hello")

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("Laxman", greeting="what's your poisen..??")