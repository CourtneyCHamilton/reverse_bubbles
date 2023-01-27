import sys


# get files, read file, strip \n, create list, make list integer, close file, return list
def read_file(filename):
    numbers_file = open(filename, 'r')

    read_numbers = numbers_file.read()

    read_numbers = read_numbers.rstrip('\n')

    numbers_list = read_numbers.split()

    integer_list = []
    for x in numbers_list:
        integer_list.append(int(x))

    numbers_file.close()

    return integer_list


# filter for odd or even numbers, odd as boolean
def filter_odd_or_even(numbers, odd):
    if odd is True:
        filtered_odd = []
        while odd is True:
            for x in numbers:
                if x % 2 != 0:
                    filtered_odd.append(x)
                    x += 1
            return filtered_odd
    else:
        filtered_even = []
        for x in numbers:
            if x % 2 == 0:
                filtered_even.append(x)
                x += 1
        return filtered_even


# bubble sort in reverse
def reversed_bubble_sort(numbers):
    last_sorted = len(numbers) - 1
    sort_me = False

    while sort_me is False:
        sort_me = True
        for i in range(0, last_sorted):
            if numbers[i] < numbers[i+1]:
                sort_me = False
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers


# cmdln arg to file paths, 1st odd, 2nd even, combine lists, reverse sort, display results


def main():
    # command line arg to file paths goes here
    first_argument = sys.argv[1]
    second_argument = sys.argv[2]

    odd_file = read_file(first_argument)
    odd_nums = filter_odd_or_even(odd_file, True)

    even_file = read_file(second_argument)
    even_nums = filter_odd_or_even(even_file, False)

    nums_to_sort = odd_nums + even_nums  # type: ignore

    final_numbers = reversed_bubble_sort(nums_to_sort)

    return final_numbers


if __name__ == '__main__':
    main()
    final_numbers = main()
    print(final_numbers)
