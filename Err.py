import getpass

def greet(name):
    print(f"Hello, {name}")

def main():
    # Prompt user for name
    name = input("Enter your name: ")
    greet(name)

    npm = 5
    denominator = npm * 2
    if denominator != 0:
        result = 10 / denominator
        print(f"Result: {result}")
    else:
        print("Cannot divide by zero.")

    x = 42
    print(f"The value of x is: {x}")

    try:
        total = int("5") + 10
        print(f"Sum: {total}")
    except ValueError:
        print("Invalid integer conversion.")

if __name__ == "__main__":
    main()
