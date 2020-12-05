import functools


def printsol(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print("The Solution to the problem for {} is {}".format(func.__name__, ret))
    return wrapper
