def main():
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"Temperature: \033[1;3m{f}\033[0m = {(f - 32) * 5.0/9.0}C")


if __name__ == '__main__':
    main()