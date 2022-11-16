t = input("symbol : ")
n = int(input("size : "))
c = 0
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
    c += 2*i+1
print(f"Use {t} {c} items")
