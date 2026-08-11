inputs = input().split()
choice = int(inputs[0])

list = [50, 40, -25, -15, 70, 84, 10]

if choice == 1:
    value = int(inputs[1])
    list.append(value)
    print(f"{list}")
elif choice == 2:
    for i in range(len(list) - 1, -1, -1):
        if list[i] < 0:
            list.remove(list[i])
    print(f"{list}")

elif choice == 3:
    list.sort()
    print(f"{list}")
elif choice == 4:
    list.reverse()
    print(f"{list}")
elif choice == 5:
    print(f"{list}")
else:
    pass
