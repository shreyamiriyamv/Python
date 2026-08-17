number = float(input("Input: "))
print("Output: Armstrong Number")
sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == number:
    print("Output: Armstrong Number")
else:
    print("Output: Not anArmstrong Number")
