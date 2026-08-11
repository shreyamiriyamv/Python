inputs = input().split()
choice = int(inputs[0])
dict = {"Rahul": 45000, "Priya": 50000, "Arun": 40000}

if choice == 1:
    key = inputs[1]
    print(f"Value: {dict.get(key)}")
elif choice == 2:
    print(f"Keys: {dict.keys()}")
elif choice == 3:
    print(f"Values: {dict.values()}")
elif choice == 4:
    print(f"Items: {dict.items()}")
elif choice == 5:
    key = inputs[1]
    value = inputs[2]
    dict.update({key: value})
    print(f"Dictionary Updated {dict}")
elif choice == 6:
    key = inputs[1]
    print(f"Removed Value: {dict.pop(key)} {dict}")
elif choice == 7:
    print(f"Removed Item: {dict.popitem()} {dict}")
elif choice == 8:
    dict.clear()
    print(f"Dictionary Cleared {dict}")
