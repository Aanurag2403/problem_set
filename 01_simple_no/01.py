# Find a digit at a specific place in a number

def find_num(num,place):
    num1 = (num // 10**(place-1))%10
    return(num1)

num=int(input("enter your number:"))
place = int(input("enter your digit place:"))
digit = find_num(num,place)
print(f"Digit at Place {place} in {num} is {digit}")