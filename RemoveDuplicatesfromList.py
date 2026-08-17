list = list(map(int, input("Enter a list of numbers: ").split()))
unique_list = []
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
