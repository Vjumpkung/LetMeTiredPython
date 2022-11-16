t = input()
x = 0
y = 0
for i in t:
    if i == "W":
        y += 1
    elif i == "A":
        x -= 1
    elif i == "S":
        y -= 1
    elif i == "D":
        x += 1
print(f"Distance : {(x**2 + y**2)**(1/2):.2f}")
