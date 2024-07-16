import sys

from Calculator.multiplication_package import multiplication_module

def main():
    print("{} * {} = {}".format(sys.argv[1], sys.argv[2], multiplication_module.multiply_two_numbers(int(sys.argv[1]), int(sys.argv[2]))))

if __name__ == "__main__":
    main()