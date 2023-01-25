gen = (sum(ord(c) for c in "Close"[:i+1]) for i in range(len("Close")))

for i in gen:
    print(i)
