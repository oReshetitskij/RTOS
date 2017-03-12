from functools import wraps


def header(title):
    def true_decorator(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            print("--- %s ---" % title)
            fn(*args, **kwargs)
        return wrapped
    return true_decorator
