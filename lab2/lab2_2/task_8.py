import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 1000
        print(f"function timing: {elapsed_ms:.3f} ms")
        return result
    return wrapper

@timing
def example_function(n):
    print(f"executing the function with parameter n={n}")
    total = 0
    for i in range(n):
        total += i
    return total

print("=== examples ===")

result1 = example_function(1500)
print(f"first: {result1}")

result2 = example_function(1000000)
print(f"second: {result2}")

result3 = example_function(500000000)
print(f"third: {result3}")

