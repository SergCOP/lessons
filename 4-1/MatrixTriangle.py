n = int(input("введите число:"))
num = 1
for x in range(1, n+1):
    for y in range(1, x+1):
        print (num, end=" ")
        num=num+1
    print()
