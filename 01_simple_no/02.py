# Find count of digits in a number

def count(num):
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num>0:
        count += 1
        num = num//10
    return count
    
num = int(input("enter your number to count digit: "))
print(f"given number has {count(num)} digits in it")