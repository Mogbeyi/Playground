import uuid

def once(callback):
    has_run = False
    result = None

    # The wrapper says: "I'll take whatever you've got..."
    def wrapper(*args, **kwargs):
        nonlocal has_run, result
        if not has_run:
            result = callback(*args, **kwargs)
            has_run = True
        return result
    return wrapper



def generate_token():
    print("Generating a brand new token...")
    return str(uuid.uuid4())[:8]

value = generate_token()
print(value)


get_secret_token_once = once(generate_token)

result_1 = get_secret_token_once()
# Log: "Generating a brand new token..."
# result_1: "a1b2c3d4"
print(result_1)

result_2 = get_secret_token_once()
# No log appears! The print() inside generate_token is skipped.
# result_2: "a1b2c3d4" (The exact same value)
print(result_2)

result_3 = get_secret_token_once()
# Still no log.
# result_3: "a1b2c3d4"
print(result_3)

