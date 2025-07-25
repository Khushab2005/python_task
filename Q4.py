# 4. Find the even elements from an array. Respectively multiply this element in
# the array.
# For example:
# Input:
# [1, 2, 3, 4, 5]
# Output
# [4,8]
# Note: Need one line code, don't use for loop and if statement.
# --------------------------------------------------------- 
a = input("Enter elements separated by space: ")
b = a.split()
c = map(int,b)
d = list(c)
print(d)

def Even(d):
    return [x * 2 for x in d if x % 2 == 0]

result = Even(d)
print(result)