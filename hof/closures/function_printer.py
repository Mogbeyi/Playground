def function_printer(value):

    def printer():
        print(value)

    return printer

print_sample = function_printer("Sample")
print_hello = function_printer("Hello")
print_sample()
print_hello()

