string = input("Enter a string: ")

left = 0
right = len(string) - 1
is_palindrome = True

while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")