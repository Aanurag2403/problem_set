# Find the largest digit

def largest_digit(num):
    max_digit = 0
    while (num > 0):
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        num //= 10
    return max_digit

num = int(input("enter your no to find largest digit: "))
print(f"largest digit in {num} is : {largest_digit(num)}")
    