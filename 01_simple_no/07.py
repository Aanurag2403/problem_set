# Find the 2nd smallest digit

def small(n):
    n = abs(n)
    digit =set()
    if n==0:
        digit.add(0)
    small_digit = 9
    while(n>0):
        digit.add(n%10)
        n = n//10
    if len(digit)<2:
        return None
    return sorted(digit)[1]

print(f"second smallest digit is: {small(322415)}")
        

