def main():
    animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also \033[1;3m{animal}\033[0m")


if __name__ == '__main__':
    main()
    