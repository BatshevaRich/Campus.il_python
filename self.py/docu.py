def func(num1, num2):
    """
    func to return sum of 2 nums
    input: 2 integers
    output: integer sum of both
    """
    return num1 + num2

def help():
    print("""
    func to return sum of 2 nums
    input: 2 integers
    output: sum of both integers
    """)

def main():
    print(func(1, 2))
    help()

if __name__ == "__main__":
    main()