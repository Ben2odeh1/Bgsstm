def reverse_number(number):
    reversed_num = 0
    while number > 0:
        remainder = number % 10
        reversed_num = (reversed_num * 10) + remainder
        number = number // 10
    return reversed_num

# Example usage
num = 12345
reversed_num = reverse_number(num)
print("The reversed number is:", reversed_num)
