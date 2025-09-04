# Find the kth smallest digit

def kth_small(n,k):
    n = abs(n)
    digit =set()
    if n ==0:
        digit.add(0)
    while n>0:
        digit.add(n%10)
        n//=10
    if len(digit)<k:
        return None
    sorted_digit=sorted(digit)
    return sorted_digit[k-1]

print(f"3rd smallest digit is: {kth_small(647243,3)}")