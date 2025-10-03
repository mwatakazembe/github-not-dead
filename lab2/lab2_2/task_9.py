def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if type(args[0]) != expected_types[1] or type(args[1]) != expected_types[0]:
                raise TypeError("wrong type. int expected")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 2.2))