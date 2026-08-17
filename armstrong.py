import math

number = float(input("Input: "))

sum = 0
temp = number
if number == 0:
    count = 1
else:
    count = math.floor(math.log10(number)) + 1
while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp //= 10
if sum == number:
    print("Output: Armstrong Number")
else:
    print("Output: Not an Armstrong Number")
