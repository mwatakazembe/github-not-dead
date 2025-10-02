from datetime import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.now()
            time_str = f"{current_time.year}-{current_time.month:02d}-{current_time.day:02d} {current_time.hour:02d}:{current_time.minute:02d}:{current_time.second:02d}"
            
            
            args_list = []
            for arg in args:
                args_list.append(str(arg))
            
            kwargs_list = []
            keys = list(kwargs.keys())
            i = 0
            while i < len(keys):
                key = keys[i]
                value = kwargs[key]
                kwargs_list.append(f"{key}={str(value)}")
                i += 1
            
            all_args = ", ".join(args_list + kwargs_list)
            
            
            log_entry = f"[{time_str}] {func.__name__}({all_args})\n"
            
        
            with open(filename, 'a') as f:
                f.write(log_entry)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_calls("function_log.txt")
def test_func(a, b, c=None):
    return a + b

test_func(1, 2, c=3)