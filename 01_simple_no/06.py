# find the smallest digit

def small_digit(n):
    n = abs(n)
    small_digit =9
    if n == 0:
        return 0
    while(n>0):
        digit =n%10
        if digit < small_digit:
            small_digit = digit
        n =n//10
    return small_digit

print(small_digit(984523))

