def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
my_list = [45, 67, 12, 89, 34]
largest_number = find_largest_number(my_list)
print("The largest number in the list is:", largest_number)
