def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == number

def main():
    try:
        num = int(input("Enter a number: "))
        if is_armstrong(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()