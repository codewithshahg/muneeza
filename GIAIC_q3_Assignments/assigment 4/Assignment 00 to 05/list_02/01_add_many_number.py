def add_many_numbers(numbers)-> int:

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far


def main():
    numbers = [1, 2, 3, 4, 5]
    sum_of_numbers: int = add_many_numbers(numbers)
    print(sum_of_numbers)  
    

if __name__ == '__main__':
    main()