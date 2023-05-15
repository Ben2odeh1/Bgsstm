def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
my_list = [10, 20, 30, 40, 50]
sum_of_numbers = calculate_sum(my_list)
print("The sum of numbers in the list is:", sum_of_numbers)
