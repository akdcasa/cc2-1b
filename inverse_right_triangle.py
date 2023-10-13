#no.3 triangle

num2 = [1, 2, 3, 4, 5]
y = 4
x = 0
while x < 5:
    for i in num2:
        print(i, end=" ")
    print("")
    del num2[y] 
    y -= 1
    x += 1 