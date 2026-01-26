def make_once(fn):
    has_run = False
    result = None

    def inner_func(*args, **kwargs):
        nonlocal has_run, result

        if not has_run: 
            result = fn(*args, **kwargs)
            has_run = True
        return result
    return inner_func 

# pure, deterministic callback
def greet(name):
    print(f"greet({name!r}) executed")
    return f"Hello, {name}!"

# use the factory
f = make_once(greet)

# behavior demo
print(f("Alice"))  # → logs "greet('Alice') executed" and returns "Hello, Alice!"
print(f("Bob"))    # → silent, still returns "Hello, Alice!"
print(f("Carol"))  # → silent, still returns "Hello, Alice!"
