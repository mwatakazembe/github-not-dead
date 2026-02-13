def cache(func):
    cached_results = {}
    
    def wrapper(a, b):
        key = (a, b)
        if key in cached_results:
            print("\ncached result")
            return cached_results[key]
        else:
            result = func(a, b)
            cached_results[key] = result
            print("\nnew result")
            return result
    
    return wrapper

@cache
def multiply(a, b):
    return a * b

print("\n=== caching ===")
print("function multiply(a, b) -> will multiply two numbers")
print("for exit you should type 'exit'")

continue_program = True

while continue_program:
    print("\ninput two numbers:")
    
    a_input = input("first (a): ")
    if a_input.lower() == 'exit':
        continue_program = False
        continue
    
    b_input = input("second (b): ")
    if b_input.lower() == 'exit':
        continue_program = False
        continue
    
    a = float(a_input)
    b = float(b_input)
    
    result = multiply(a, b)
    print(f"result: {a} × {b} = {result}")

print("\nthis is the end, my beautiful friend.")