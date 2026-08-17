list = list(map(int, input("Enter a list of numbers: ").split()))
print(f"Input: {list}")
max = max(list)
second_largest = list[0]
for num in list:
    if num < max and num > second_largest:
        second_largest = num
print(f"Output: {second_largest}")
