t = input("symbol : ")
n = int(input("size : "))
c = 0
for i in range(n):
    print(f"{' '*(n-i-1)}{t*(2*i+1)}")
    c += 2*i+1
print(f"Use {t} {c} items")
