from random import randint

def sort_numbers(numbers):
    sorted_list = sorted(numbers, reverse=True)
    return sorted_list

numbers = [randint(0, 100) for i in range(7)]
print(numbers);
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)