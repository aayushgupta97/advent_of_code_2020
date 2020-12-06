import functools


def printsol(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print("The Solution to the problem for {} is {}".format(func.__name__, ret))
    return wrapper


def read_text_file(fname):
    with open(f"data/{fname}", "r") as f:
        return [line.replace("\n", "") for line in f.readlines()]