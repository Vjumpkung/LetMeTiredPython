x = -999
neg = 0
pos = 0
zero = 0
while x != 0:
    x = int(input())
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
print(f"Total Postitive Number : {pos}")
print(f"Total Negative Number : {neg}")
