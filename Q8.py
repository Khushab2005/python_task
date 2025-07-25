# Write a program to extract all palindromic substrings (length ≥ 2) from a string of digits.
# A palindrome is a number that reads the same forward and backward, e.g., 121, 44, 2332.
# Input: 588432347423122345
# output = 88,43234,323,474,22

x = "588432347423122345"
output = []

for i in range(len(x)):
    for j in range(i + 2 , len(x) + 1):
        y = x[i:j]
        if y == y[::-1]:
            output.append(y)
print(output)







