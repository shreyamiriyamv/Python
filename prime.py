a, b = map(int, input("Enter a range of numbers (a b): ").split())
for num in range(a, b + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, end=" ")
print()
