class Calculate:

    @staticmethod
    def square(x):
        return x * x

    @staticmethod
    def cube(x):
        return x * x * x

def main():
    print(Calculate.cube(3))

main()
