# Find generic root (sum of all digits) of a number

def generic(n):
    while n >10:
        s = 0
        while n>0:
            s= s+n%10
            n=n//10
        n=s
    return n

print(generic(123))