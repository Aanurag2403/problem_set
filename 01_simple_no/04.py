# Find the 2nd largest digit

def larg(num):
    num = abs(num)
    digit = set()
    if num == 0:
        digit.add(0)
    while(num>0):
        digit.add(num%10)
        num //=10
    if len(digit) < 2:
        return None
    return sorted(digit ,reverse=True)[1]

num = int(input("enter your no: "))
print(f"second largest digit of the given no. is: {larg(num)}")
    