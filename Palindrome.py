number = int(input("Input: "))
reverse = 0
temp = number
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if (number == reverse):
    print(f"Input: {number}.    Reverse: {reverse}.      Palindrome.")
else:
    print(f"Input: {number}.    Reverse: {reverse}.      Not a Palindrome.")
