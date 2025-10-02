def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            i = 0
            while i < len(args) and i < len(expected_types):
                if type(args[i]) != expected_types[i]:
                    print(f"error: argument {i} ({args[i]}) has a type {type(args[i]).__name__}, but it's expected {expected_types[i].__name__}")
                    return None
                i += 1
            
        
            param_names = []
            j = 0
            while j < len(expected_types):
                param_names.append(chr(97 + j)) 
                j += 1
            
            for name in kwargs:
                idx = 0
                found = False
                while idx < len(param_names):
                    if param_names[idx] == name:
                        found = True
                        break
                    idx += 1
                
                if found and idx < len(expected_types):
                    if type(kwargs[name]) != expected_types[idx]:
                        print(f"error: argument '{name}' ({kwargs[name]}) has a type {type(kwargs[name]).__name__}, but it's expected {expected_types[idx].__name__}")
                        return None
            
            result = func(*args, **kwargs)
            print(f"success. result: {result}")
            return result
        return wrapper
    return decorator


print("===testing===")

@type_check(int, int)
def add(a, b):
    return a + b

print("\n1. correct data:")
print("add(2, 3):")
add(2, 3)

print("\n2. incorrect first arg:")
print("add(2.5, 3):")
add(2.5, 3)

print("\n3. incorrect second arg:")
print("add(2, '3'):")
add(2, '3')

print("\n4. correct kwargs:")
print("add(a=5, b=7):")
add(a=5, b=7)

print("\n5. incorrect kwargs:")
print("add(a=5, b='7'):")
add(a=5, b='7')