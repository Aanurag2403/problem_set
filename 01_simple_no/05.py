#  Find the kth largest digit

def kth_larg(n,k):
    n = abs(n)
    digit = set()
    if n == 0:
        digit.add(0)
    while (n > 0):
        digit.add(n %10)
        n = n//10
    if len(digit)<k:
        return None
    sorted_digits = sorted(digit ,reverse=True)
    return sorted_digits[k-1]


n =int(input("enter your number: "))
k = int(input("enter your kth terms: "))

print(f"{k}th largest no. is : {kth_larg(n,k)}")