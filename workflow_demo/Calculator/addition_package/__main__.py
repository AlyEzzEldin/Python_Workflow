import sys

from Calculator.addition_package import addition_module

def main():
    print("{} + {} = {}".format(sys.argv[1], sys.argv[2], addition_module.add_two_numbers(int(sys.argv[1]), int(sys.argv[2]))))

if __name__ == "__main__":
    main()