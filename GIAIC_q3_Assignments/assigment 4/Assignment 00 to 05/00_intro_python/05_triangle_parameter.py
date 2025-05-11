def main():
    side1 = float(input("What is the length of side 1 >>"))
    side2 = float(input("What is the length of side 2 >>"))
    side3 = float(input("What is the length of side 3 >>"))

    print(f"The perimeter of the triangle is \033[1;3m{side1 + side2 + side3}\033[0m")

if __name__ == '__main__':
    main()