def main():
    dist:dict = {}
    while True:
        num = input("Enter a numeber ")
        if num != "":
            if num in dist:
                dist[num] += 1
            else:
                dist[num] = 1
        else:
            break
    for num in dist:
        print(f"{num} appears {dist[num]} times")


if __name__ == "__main__":
    main()